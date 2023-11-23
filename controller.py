import torch

import predictor_adapter
from view_enum import *
import pandas_adapter as pd
import predictor_adapter as pa
import numpy as np
import output_table_columns
import output_stream_classes
import predictor


def _load_data_from_file(input_file_name, input_file_type):
    read_function = pd.pandas_readers[input_file_type]

    data = read_function(input_file_name)
    first_row_index = 0
    return data.to_numpy()[first_row_index:, :]


def _get_entered_data(enum_input_data):
    dna = np.array([enum_input_data[INPUT_INFO.DNA_DATA]])
    Ct = enum_input_data[INPUT_INFO.Ct]
    salt_factor_value = np.array([enum_input_data[INPUT_INFO.SALT_VALUE]])
    data = np.concatenate((dna, salt_factor_value))
    if enum_input_data[INPUT_INFO.IS_ACTIVITY]:
        salt_factor_type = INPUT_INFO.IS_ACTIVITY
    else:
        salt_factor_type = INPUT_INFO.IS_SALT
    return np.expand_dims(data, axis=0), Ct, salt_factor_type


def _get_predictor(enum_input_data):
    enum_predictor_type = enum_input_data[INPUT_INFO.PREDICTOR_TYPE]
    return pa.predictor_to_object[enum_predictor_type]


def _get_data_manager(enum_input_data, Ct_factor):
    dna_analysis_type = predictor_adapter.predictor_to_dna_analisys_type[enum_input_data[INPUT_INFO.PREDICTOR_TYPE]]
    data_manager = predictor.dna_handlers[dna_analysis_type][Ct_factor]
    return data_manager


class controller:
    def __init__(self, view_managers):
        self.error_manager = view_managers[VIEW_MANAGERS.ERROR_MANAGER]
        self.output_function = view_managers[VIEW_MANAGERS.OUTPUT_FUNCTION]
        self.predictions = None
        self.input_file_data = None
        self.input_data = None

    def parse_info_and_calculate_parameters(self, enum_input_data):
        """
        Calculate parameters using input information and pass it to output view functions
        :param enum_input_data: information from view
        :param view_managers: output methods provided by view
        """
        data, Ct, salt_factor_type = self._load_data_for_predictor(enum_input_data)
        data_manager = _get_data_manager(enum_input_data, salt_factor_type)
        predictor_ = _get_predictor(enum_input_data)
        output_streams = self._make_output_streams()
        self._calculate_and_pass_predictions(predictor_, data, output_streams, data_manager, Ct)

    def _calculate_and_pass_predictions(self, predictor, input_data, output_streams, data_manager, Ct):
        try:
            predictions = predictor(input_data, data_manager, Ct)
        except Exception:
            self.error_manager("There is invalid data for analysis. Please, check all the data "
                                                       "validity")
        if self.predictions is None:
            self.predictions = predictions
            self.input_data = input_data
        else:
            self.predictions = torch.cat((self.predictions, predictions), dim=0)
            self.input_data = np.concatenate((self.input_data, input_data), axis=0)

        predictions = pd._make_output_DataFrame(self.predictions, self.input_data,
                                                output_table_columns.output_column_str_name_list)

        for current_output_stream in output_streams:
            current_output_stream << predictions

    def _make_output_streams(self):
        output_streams = []
        output_streams.append(output_stream_classes.function_output_stream(output_function=self.output_function,
                                                                           error_manager=self.error_manager))
        return output_streams

    def _load_data_for_predictor(self, enum_input_data):
        if INPUT_INFO.INPUT_FILE_NAME in enum_input_data.keys():
            input_file_name = enum_input_data[INPUT_INFO.INPUT_FILE_NAME]
            input_file_type = enum_input_data[INPUT_INFO.INPUT_FILE_TYPE]
            if not input_file_name or not input_file_type:
                self.error_manager("Invalid data about input file!")
            try:
                return self.input_file_data.to_numpy()[0:, :], 1e-5, INPUT_INFO.IS_ACTIVITY
            except Exception:
                self.error_manager("Invalid input file")
        return _get_entered_data(enum_input_data)
