from enum import IntEnum


class BASE_1D(IntEnum):
    A = 2
    T = 3
    C = 4
    G = 5


class BASE_2D(IntEnum):
    A = 0
    T = 1
    C = 2
    G = 3


dna_bases_count = 4

dna_binary_view = {'a': BASE_2D.A, 't': BASE_2D.T,
                   'c': BASE_2D.C, 'g': BASE_2D.G,
                   'A': BASE_2D.A, 'T': BASE_2D.T,
                   'C': BASE_2D.C, 'G': BASE_2D.G}

dna_base_dict = {'a': BASE_1D.A, 't': BASE_1D.T,
                 'c': BASE_1D.C, 'g': BASE_1D.G}


class Predictor_types(IntEnum):
    LINEAR_REL_PREDICTOR = 0
    CONV_ABS_PREDICTOR = 1
    CONV_REL_PREDICTOR = 2


gc_pows = [0, 2, 3]
length_pows = [2, 3]
dna_column = 0


class DataColumns(IntEnum):
    DNA = 0
    Ct = 1
    dH = 2
    dG = 3
    dS = 4
    Tm = 5
    Na = 6


class Processing(IntEnum):
    NN = 0
    D1 = 1
    D2 = 2


class prediction_columns(IntEnum):
    dH_INDEX = 0
    dG_INDEX = 1
    dS_INDEX = 2
    Tm_INDEX = 3
