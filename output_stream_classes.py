import pandas_adapter as pd
import abc
from abc import ABC, abstractmethod


class output_stream(ABC):
    @abstractmethod
    def __lshift__(self, saving_dataframe):
        pass


class file_output_stream(output_stream):
    def __init__(self, save_file_name, save_file_type, error_manager=None):
        self.save_file_name = save_file_name
        self.save_file_type = save_file_type
        self.error_manager = error_manager

    def __lshift__(self, saving_dataframe):
        try:
            writer = pd.pandas_writers[self.save_file_type]
            writer(saving_dataframe, self.save_file_name)
        except Exception:
            self.error_manager("Problems with saving data into save file, please check save file validity")


class function_output_stream:
    def __init__(self, output_function=None, error_manager=None):
        self.output_function = output_function
        self.error_manager = error_manager

    def __lshift__(self, saving_dataframe):
        self.output_function(saving_dataframe)