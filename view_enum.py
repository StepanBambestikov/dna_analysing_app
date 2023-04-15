from enum import IntEnum


class INPUT_INFO(IntEnum):
    PREDICTOR_TYPE = 0
    DNA_DATA = 1
    S1 = 2
    S2 = 3
    Ct = 4
    INPUT_FILE_NAME = 5
    INPUT_FILE_TYPE = 6
    OUTPUT_FILE_NAME = 7
    OUTPUT_FILE_TYPE = 8


class VIEW_MANAGERS(IntEnum):
    ERROR_MANAGER = 0
    OUTPUT_FUNCTION = 1
