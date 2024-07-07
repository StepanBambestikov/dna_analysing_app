import numpy as np
import torch

from project.service.base import dna_bases_count, dna_binary_view, dna_base_dict, gc_pows, length_pows
from project.service.nn import nearest_neighbors, ends


def pair_finder(pairs, text_sequence):
    pair_count = 0
    for current_pair in pairs:
        pair_count += text_sequence.count(current_pair)
    return pair_count


def end_finder(ends, text_sequence):
    end_count = 0
    if text_sequence[0] in ends:
        end_count += 1
    if text_sequence[-1] in ends:
        end_count += 1
    return end_count


def make_nn_data_from_text_dna(text_dna_array):
    nn_vector_len = 12
    data_features = np.zeros((text_dna_array.shape[0], nn_vector_len))
    for data_row_index, current_str in enumerate(text_dna_array):
        for vector_index, current_end in enumerate(ends):
            data_features[data_row_index, vector_index] = end_finder(current_end, current_str)

        for vector_index, current_nn in enumerate(nearest_neighbors):
            data_features[data_row_index, vector_index + 2] = pair_finder(current_nn, current_str)
    return data_features


def _get_sequences_lengths(text_dna_sequences):
    vector_len_function = np.vectorize(len)
    return vector_len_function(text_dna_sequences)


def _get_bases_count(text_dna_sequences, *searching_bases):
    result = torch.zeros(text_dna_sequences.shape[0])
    for current_index, current_string in enumerate(text_dna_sequences):
        for searching_base in searching_bases:
            result[current_index] += current_string.count(searching_base)
    return result


def _get_gc_concentration(text_dna_sequences):
    sequences_lengths = _get_sequences_lengths(text_dna_sequences)
    gc_count = _get_bases_count(text_dna_sequences, "g", "c", "G", "C")
    return gc_count / sequences_lengths


def _array_pow_expantion(input_column, pows):
    columns = [input_column]
    for current_pow in pows:
        columns.append(np.power(input_column, current_pow))
    return torch.from_numpy(np.column_stack((columns)))


def Na_data_function_maker(origin_preparator, yaml_data, prepare_salt=False):
    def function(dna_and_na_array):
        origin_data = torch.from_numpy(origin_preparator(dna_and_na_array[:, 0], yaml_data))
        gc_concetrations = _get_gc_concentration(dna_and_na_array[:, 0])
        sequences_lengths = _get_sequences_lengths(dna_and_na_array[:, 0])
        gc_concetrations = _array_pow_expantion(gc_concetrations, gc_pows)
        sequences_lengths = _array_pow_expantion(sequences_lengths, length_pows)
        Na_features = torch.from_numpy(dna_and_na_array[:, 1].astype(np.float64))[:, None]
        if prepare_salt:
            Na_features = Na_features * 10 ** (-0.509 * (Na_features) ** 0.5 / (1 + (Na_features) ** 0.5) - 0.2 * (Na_features))
        return origin_data, torch.cat((gc_concetrations, sequences_lengths, Na_features), dim=1)
    return function


def make_Na_data_from_text_dna(dna_and_na_array, origin_preparator, prepare_salt=False):
    origin_data = torch.from_numpy(origin_preparator(dna_and_na_array[:, 0]))
    gc_concentrations = _get_gc_concentration(dna_and_na_array[:, 0])
    sequences_lengths = _get_sequences_lengths(dna_and_na_array[:, 0])
    gc_concentrations = _array_pow_expantion(gc_concentrations, gc_pows)
    sequences_lengths = _array_pow_expantion(sequences_lengths, length_pows)
    Na_features = torch.from_numpy(dna_and_na_array[:, 1].astype(np.float64))[:, None]
    if prepare_salt:
        Na_features = Na_features * 10 ^ (-0.509 * Na_features ** 0.5 / (1 + Na_features ** 0.5) - 0.2 * Na_features)
    return origin_data, torch.cat((gc_concentrations, sequences_lengths, Na_features), dim=1)


def make_1d_data_from_text_dna(text_dna_array, yaml_data):
    max_string_size = len(max(text_dna_array, key=len)) + 1
    data_features = np.zeros((text_dna_array.shape[0], max_string_size))
    try:
        for data_row_index, current_str in enumerate(text_dna_array):
            for data_col_index, current_symbol in enumerate(current_str):
                data_features[data_row_index, data_col_index + 1] = dna_base_dict[current_symbol]
    except KeyError:
        raise ValueError(yaml_data["errors"]["unexpected_letter_in_dha_sequence"])
    return data_features


def make_2d_data_from_text_dna(text_dna_array, yaml_data):
    max_string_size = 31
    first_axis_padding = 0
    second_axis_padding = 0
    summary_padding = 0

    data_features = np.zeros((text_dna_array.shape[0], dna_bases_count + summary_padding, max_string_size))
    try:
        for data_row_index, current_str in enumerate(text_dna_array):
            for data_col_index, current_symbol in enumerate(current_str):
                data_features[data_row_index, dna_binary_view[current_symbol] + first_axis_padding,
                                              data_col_index + second_axis_padding] = 1
    except KeyError:
        raise ValueError(yaml_data["errors"]["unexpected_letter_in_dha_sequence"])
    return data_features.astype('float32')

