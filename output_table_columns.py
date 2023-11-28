from enum import IntEnum


class DataColumns(IntEnum):
    DNA = 0
    Ct = 1
    dH = 2
    dG = 3
    dS = 4
    Tm = 5
    Na = 6


output_column_names = {
    DataColumns.DNA: "Sequence",
    DataColumns.Ct: "Ct",
    DataColumns.Na: "[Na⁺]",
    DataColumns.dH: "ΔH⁰",
    DataColumns.dG: "ΔG⁰₃₇",
    DataColumns.dS: "ΔS⁰",
    DataColumns.Tm: "Tₘ"
}


output_column_str_name_list = [[output_column_names[DataColumns.DNA], output_column_names[DataColumns.Na],
                               output_column_names[DataColumns.Ct], output_column_names[DataColumns.dH],
                               output_column_names[DataColumns.dG], output_column_names[DataColumns.dS],
                               output_column_names[DataColumns.Tm]]]

output_column_str_options_list = [["5'-3'", "M", "M", "cal/mol", "cal/mol", "cal/mol/K", "C⁰"]]

output_column_base_str_name_list = [[output_column_names[DataColumns.DNA], output_column_names[DataColumns.Na],
                                    output_column_names[DataColumns.Ct]]]
