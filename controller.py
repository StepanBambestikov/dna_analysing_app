from view_enum import *
import pandas_adapter as pd
import predictor_adapter as pa
import numpy as np
import output_table_columns
import output_stream_classes


def _load_data_from_file(input_file_name, input_file_type):
    read_function = pd.pandas_readers[input_file_type]
    data = read_function(input_file_name, header=None)
    first_row_index = 1
    return data.to_numpy()[first_row_index:, :]


def _get_entered_data(enum_input_data):
    dna = np.array([enum_input_data[INPUT_INFO.DNA_DATA]])
    s1 = np.array([enum_input_data[INPUT_INFO.S1]])
    s2 = np.array([enum_input_data[INPUT_INFO.S2]])
    Ct = np.array([enum_input_data[INPUT_INFO.Ct]])
    data = np.concatenate((dna, s1, s2, Ct))
    return np.expand_dims(data, axis=0)


def _get_predictor(enum_input_data):
    enum_predictor_type = enum_input_data[INPUT_INFO.PREDICTOR_TYPE]
    return pa.predictor_to_object[enum_predictor_type]


class controller:
    def __init__(self, view_managers):
        self.error_manager = view_managers[VIEW_MANAGERS.ERROR_MANAGER]
        self.output_function = view_managers[VIEW_MANAGERS.OUTPUT_FUNCTION]

    def parse_info_and_calculate_parameters(self, enum_input_data):
        """
        Calculate parameters using input information and pass it to output view functions
        :param enum_input_data: information from view
        :param view_managers: output methods provided by view
        """
        data = self._load_data_for_predictor(enum_input_data)
        predictor = _get_predictor(enum_input_data)
        output_streams = self._make_output_streams(enum_input_data)
        self._calculate_and_pass_predictions(predictor, data, output_streams)

    def _calculate_and_pass_predictions(self, predictor, input_data, output_streams):
        try:
            predictions = predictor(input_data)
        except Exception:
            self.error_manager("There is invalid data for analysis. Please, check all the data "
                                                       "validity")
        predictions = pd._make_output_DataFrame(predictions, input_data,
                                                output_table_columns.output_column_str_name_list)
        for current_output_stream in output_streams:
            current_output_stream << predictions

    def _make_output_streams(self, enum_input_data):
        output_streams = []
        if INPUT_INFO.OUTPUT_FILE_NAME in enum_input_data.keys():
            save_file_name = enum_input_data[INPUT_INFO.OUTPUT_FILE_NAME]
            save_file_type = enum_input_data[INPUT_INFO.OUTPUT_FILE_TYPE]
            output_streams.append(output_stream_classes.file_output_stream(save_file_name=save_file_name,
                                                                           save_file_type=save_file_type,
                                                                           error_manager=self.error_manager))
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
                return _load_data_from_file(input_file_name, input_file_type)
            except Exception:
                self.error_manager("Invalid input file")

        return _get_entered_data(enum_input_data)
