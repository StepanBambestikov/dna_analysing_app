import torch
import math
from network_service import dna_handlers
from service import view_enum, output_table_columns
from service.base import Processing, prediction_columns

DEFAULT_Ct = float(output_table_columns.data['default_values']['Ct_default'])


def _Tm_calculation(dH_values, dS_values, is_celsius=True, Ct=DEFAULT_Ct):
    Tm_additive = 1.987 * math.log(Ct / 4)
    if is_celsius:
        celsius_additive = 273
    else:
        celsius_additive = 0
    Tm_values = ((dH_values * 1000) / (dS_values + Tm_additive)) - celsius_additive
    return Tm_values


dna_handlers = {
    Processing.D1: dna_handlers.make_1d_data_from_text_dna,
    Processing.D2: {view_enum.INPUT_INFO.IS_ACTIVITY: dna_handlers.Na_data_function_maker(
        dna_handlers.make_2d_data_from_text_dna, output_table_columns.data, prepare_salt=False),
        view_enum.INPUT_INFO.IS_SALT: dna_handlers.Na_data_function_maker(
            dna_handlers.make_2d_data_from_text_dna,
            output_table_columns.data,
            prepare_salt=True)},
    Processing.NN: {view_enum.INPUT_INFO.IS_ACTIVITY: dna_handlers.Na_data_function_maker(
        dna_handlers.make_nn_data_from_text_dna,
        output_table_columns.data,
        prepare_salt=False),
        view_enum.INPUT_INFO.IS_SALT: dna_handlers.Na_data_function_maker(
            dna_handlers.make_nn_data_from_text_dna,
            output_table_columns.data,
            prepare_salt=True)}
}

model_names_to_saved_files = {
    "conv_rel": output_table_columns.data['model_names_to_saved_files']['conv_rel'],
    "conv_abs": output_table_columns.data['model_names_to_saved_files']['conv_abs'],
    "linear_rel": output_table_columns.data['model_names_to_saved_files']['linear_rel']
}


def _load_network(model_name, model_type):
    model = model_type()
    saved_model_file_name = model_names_to_saved_files[model_name]
    model.load_state_dict(torch.load(saved_model_file_name))
    return model


class Predictor:
    def __init__(self, model_name, model_type, conv_factor):
        self.model_name = model_name
        self.model_type = model_type
        self.conv_factor = conv_factor

    def __call__(self, input_data, dna_process_manager, Ct):
        model = _load_network(self.model_name, self.model_type)
        processed_dna = dna_process_manager(input_data[:, :2])
        predictions = model([*processed_dna])
        Tm_prediction = _Tm_calculation(predictions[:, prediction_columns.dH_INDEX],
                                        predictions[:, prediction_columns.dS_INDEX], Ct=Ct)
        predictions = predictions[:,
                      [prediction_columns.dH_INDEX, prediction_columns.dS_INDEX, prediction_columns.dG_INDEX]]
        return torch.cat((predictions, Tm_prediction[:, None]), dim=1)
