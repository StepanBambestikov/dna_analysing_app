from enum import IntEnum
import torch
import math
import dna_handlers
import network_classes as nn_classes

tm_additive = 1.987 * math.log(1e-5 / 4)


def _Tm_calculation(dH_values, dS_values):
    Tm_values = ((dH_values * 1000) / (dS_values + tm_additive)) - 273
    return Tm_values


class Processing(IntEnum):
    NN = 0
    D1 = 1
    D2 = 2


dna_handlers = {
    Processing.D1: dna_handlers.make_1d_data_from_text_dna,
    Processing.D2: dna_handlers.Na_data_function_maker(dna_handlers.make_2d_data_from_text_dna),
    Processing.NN: dna_handlers.Na_data_function_maker(dna_handlers.make_nn_data_from_text_dna)
}


class prediction_columns(IntEnum):
    dH_INDEX = 0
    dG_INDEX = 1
    dS_INDEX = 2
    Tm_INDEX = 3


def make_test_network():
    def test_network(processed_dna, sol_data):
        prediction = torch.ones([processed_dna.shape[0], 3])
        return prediction
    return test_network


model_names_to_saved_files = {
    "conv_rel": "conv2d_net_06_05normalized_l1_multi_loss_relative_Tm",
    "conv_abs": "conv2d_net_06_05normalized_l1_multi_loss_absolute_Tm",
    "linear_rel": "linear_net_06_05normalized_l1_multi_loss_06_05_relative_loss"
}


# todo delete test_mode
def _load_network(model_name, model_type):
    model = model_type()
    saved_model_file_name = model_names_to_saved_files[model_name]
    model.load_state_dict(torch.load(saved_model_file_name))
    return model


class Predictor:
    def __init__(self, model_name, model_type, conv_factor, dna_process_manager):
        self.model_name = model_name
        self.model_type = model_type
        self.conv_factor = conv_factor
        self.dna_process_manager = dna_process_manager

    def __call__(self, input_data):
        model = _load_network(self.model_name, self.model_type)
        processed_dna = self.dna_process_manager(input_data[:, :2])
        predictions = model([*processed_dna])
        Tm_prediction = _Tm_calculation(predictions[:, prediction_columns.dH_INDEX],
                                                  predictions[:, prediction_columns.dS_INDEX])
        return torch.cat((predictions, Tm_prediction[:, None]), dim=1)
