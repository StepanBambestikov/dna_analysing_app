from enum import IntEnum


class INPUT_INFO(IntEnum):
    PREDICTOR_TYPE = 0
    DNA_DATA = 1
    Ct = 2
    INPUT_FILE_NAME = 3
    INPUT_FILE_TYPE = 4
    OUTPUT_FILE_NAME = 5
    OUTPUT_FILE_TYPE = 6


class VIEW_MANAGERS(IntEnum):
    ERROR_MANAGER = 0
    OUTPUT_FUNCTION = 1
