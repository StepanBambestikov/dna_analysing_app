import numpy as np
from dna_enumeration import *

dna_bases_count = 4
dna_base_dict = {'a': BASE_1D.A, 't': BASE_1D.T, 'c': BASE_1D.C, 'g': BASE_1D.G}
dna_binary_view = {'a': BASE_2D.A, 't': BASE_2D.T, 'c': BASE_2D.C, 'g': BASE_2D.G}


def make_nn_data_from_text_dna():
    #TODO!!!!
    return None


def make_1d_data_from_text_dna(text_dna_array):
    #todo make constant related to max length of test dna!!!!
    max_string_size = len(max(text_dna_array, key=len)) + 1
    data_features = np.zeros((text_dna_array.shape[0], max_string_size))
    try:
        for data_row_index, current_str in enumerate(text_dna_array):
            for data_col_index, current_symbol in enumerate(current_str):
                data_features[data_row_index, data_col_index + 1] = dna_base_dict[current_symbol]
    except KeyError:
        raise ValueError("Unexpected letter in dna sequence")
    return data_features


def make_2d_data_from_text_dna(text_dna_array):
    #todo make constant related to max length of test dna!!!!
    max_string_size = len(max(text_dna_array, key=len)) + 1
    # first_axis_padding = 1
    # second_axis_padding = 1
    first_axis_padding = 0
    second_axis_padding = 0
    summary_padding = 0

    data_features = np.zeros((text_dna_array.shape[0], dna_bases_count + summary_padding, max_string_size))
    for data_row_index, current_str in enumerate(text_dna_array):
        for data_col_index, current_symbol in enumerate(current_str):
            data_features[data_row_index, dna_binary_view[current_symbol] + first_axis_padding,
                                          data_col_index + second_axis_padding] = 1
    return data_features