import yaml

from project.service.base import DataColumns

with open('../config.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)

output_column_names = {
    DataColumns.DNA: data["output_column_names"]["DNA"],
    DataColumns.Ct: data["output_column_names"]["Ct"],
    DataColumns.Na: data["output_column_names"]["Na"],
    DataColumns.dH: data["output_column_names"]["dH"],
    DataColumns.dG: data["output_column_names"]["dG"],
    DataColumns.dS: data["output_column_names"]["dS"],
    DataColumns.Tm: data["output_column_names"]["Tm"],
}

output_column_str_name_list = [[output_column_names[DataColumns.DNA], output_column_names[DataColumns.Na],
                                output_column_names[DataColumns.Ct], output_column_names[DataColumns.dH],
                                output_column_names[DataColumns.dS], output_column_names[DataColumns.dG],
                                output_column_names[DataColumns.Tm]]]

output_column_str_options_list = [[data["output_column_str_options_list"]["DNA"],
                                   data["output_column_str_options_list"]["Ct"],
                                   data["output_column_str_options_list"]["Na"],
                                   data["output_column_str_options_list"]["dH"],
                                   data["output_column_str_options_list"]["dG"],
                                   data["output_column_str_options_list"]["dS"],
                                   data["output_column_str_options_list"]["Tm"]]]

output_column_base_str_name_list = [[output_column_names[DataColumns.DNA], output_column_names[DataColumns.Na],
                                     output_column_names[DataColumns.Ct]]]
