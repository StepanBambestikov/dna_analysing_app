import pandas
import pandas as pd
from file_types import File_types
import numpy as np


pandas_readers = {
    File_types.CSV: pd.read_csv,
    File_types.EXCEL: pd.read_excel
}


pandas_writers = {
    File_types.CSV: pd.DataFrame.to_csv,
    File_types.EXCEL: pd.DataFrame.to_excel,
}


def _make_output_DataFrame(predictions_tensor, input_data_numpy, column_names):
    output_data = np.concatenate((input_data_numpy, predictions_tensor.numpy()), axis=1)
    output_dataFrame = pandas.DataFrame(data=output_data, columns=column_names)
    return output_dataFrame
