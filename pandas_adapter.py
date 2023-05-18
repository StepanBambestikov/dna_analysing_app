import pandas
import pandas as pd
from file_types import File_types
import numpy as np


def make_csv_reader():
    def csv_reader(input_file_name):
        return pd.read_csv(input_file_name, header=None, sep=";")
    return csv_reader


def make_excel_reader():
    def csv_reader(input_file_name):
        return pd.read_excel(input_file_name)
    return csv_reader


pandas_readers = {
    File_types.CSV: make_csv_reader(),
    File_types.EXCEL: make_excel_reader()
}


pandas_writers = {
    File_types.CSV: pd.DataFrame.to_csv,
    File_types.EXCEL: pd.DataFrame.to_excel,
}


def _make_output_DataFrame(predictions_tensor, input_data_numpy, column_names):
    output_data = np.concatenate((input_data_numpy, predictions_tensor.detach().numpy()), axis=1)
    output_dataFrame = pandas.DataFrame(data=output_data, columns=column_names)
    return output_dataFrame
