from predictor import pandas_adapter as pd
from abc import ABC, abstractmethod


class output_stream(ABC):
    @abstractmethod
    def __lshift__(self, saving_dataframe):
        pass


class file_output_stream(output_stream):
    def __init__(self, save_file_name, save_file_type, yaml_data, error_manager=None):
        self.save_file_name = save_file_name
        self.save_file_type = save_file_type
        self.error_manager = error_manager
        self.yaml_data = yaml_data

    def __lshift__(self, saving_dataframe):
        try:
            writer = pd.pandas_writers[self.save_file_type]
            writer(saving_dataframe, self.save_file_name)
        except Exception:
            self.error_manager(self.yaml_data["errors"]["saving_data_into_save_file_error"])


class function_output_stream(output_stream):
    def __init__(self, output_function=None, error_manager=None):
        self.output_function = output_function
        self.error_manager = error_manager

    def __lshift__(self, saving_dataframe):
        self.output_function(saving_dataframe)
