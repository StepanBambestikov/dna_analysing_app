from enum import IntEnum


class DataColumns(IntEnum):
    DNA = 0
    Ct = 1
    S1 = 2
    S2 = 3
    dH = 4
    dG = 5
    dS = 6
    Tm = 7


output_column_names = {
    DataColumns.DNA: "dna",
    DataColumns.Ct: "Ct",
    DataColumns.S1: "s1",
    DataColumns.S2: "s2",
    DataColumns.dH: "dH",
    DataColumns.dG: "dG",
    DataColumns.dS: "dS",
    DataColumns.Tm: "Tm",
}

output_column_str_name_list = [output_column_names[DataColumns.DNA], output_column_names[DataColumns.Ct],
                               output_column_names[DataColumns.S1], output_column_names[DataColumns.S2],
                               output_column_names[DataColumns.dH], output_column_names[DataColumns.dG],
                               output_column_names[DataColumns.dS], output_column_names[DataColumns.Tm]]
