import pandas
import pandas as pd
from Bio import SeqIO
from file_types import File_types
import numpy as np


def make_csv_reader():
    def csv_reader(input_file_name):
        return pd.read_csv(input_file_name, header=None, sep=";")
    return csv_reader


def make_excel_reader():
    def excel_reader(input_file_name):
        return pd.read_excel(input_file_name, engine='openpyxl')
    return excel_reader


def make_fasta_reader():
    def fasta_reader(input_file_name):
        sequences = []
        for record in SeqIO.parse(input_file_name, "fasta"):
            sequences.append(str(record.seq))
        df = pd.DataFrame(sequences, columns=['Sequences'])
        return df
    return fasta_reader


pandas_readers = {
    File_types.CSV: make_csv_reader(),
    File_types.EXCEL: make_excel_reader(),
    File_types.FASTA: make_fasta_reader()
}

def make_csv_writer():
    def csv_writer(saving_dataframe, input_file_name):
        return pd.DataFrame.to_csv(saving_dataframe, input_file_name, sep=",")
    return csv_writer


def make_excel_writer():
    def excel_writer(saving_dataframe, input_file_name):
        return pd.DataFrame.to_excel(saving_dataframe, input_file_name, engine='openpyxl')
    return excel_writer

pandas_writers = {
    File_types.CSV: make_csv_writer(),
    File_types.TXT: make_csv_writer(),
    File_types.DAT: make_csv_writer(),
    File_types.EXCEL: make_excel_writer(),
}

pandas_file_extensions = {
    "csv": File_types.CSV,
    "dat": File_types.DAT,
    "txt": File_types.TXT,
    "xlsx": File_types.EXCEL,
    "fa": File_types.FASTA,
}


def get_file_extension_by_name(file_name):
    splitted_name = file_name.partition(".")
    if len(splitted_name) != 3:
        return None
    if file_name.partition(".")[2] not in pandas_file_extensions:
        return None
    return pandas_file_extensions[file_name.partition(".")[2]]


def _make_output_DataFrame(predictions_tensor, input_data_numpy, column_names, column_options, decimals):
    output_data = np.concatenate((input_data_numpy, np.round(predictions_tensor.detach().numpy(), decimals=decimals)), axis=1)
    output_data = np.concatenate((np.array(column_names), np.array(column_options), output_data), axis=0)
    # output_dataFrame = pandas.DataFrame(data=output_data, columns=column_names)
    output_dataFrame = pandas.DataFrame(data=output_data)
    return output_dataFrame
