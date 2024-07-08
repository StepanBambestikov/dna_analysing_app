import yaml
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QAbstractScrollArea
from widgets import Ui_MainWindow
from service import view_enum as ve, output_table_columns
from service.base import Predictor_types, DataColumns
from service.file_types import File_types
import controller
from table_service import pandasModel
import output_stream_classes
from predictor import pandas_adapter as pd
from PyQt5.QtCore import QTimer
from service.output_table_columns import output_column_names
from PyQt5 import QtCore

predictor_text_to_enum = {
    "linear_rel_processing": Predictor_types.LINEAR_REL_PREDICTOR,
    "conv_abs_processing": Predictor_types.CONV_ABS_PREDICTOR,
    "conv_rel_processing": Predictor_types.CONV_REL_PREDICTOR
}

text_file_type_to_enum = {
    "csv": File_types.CSV,
    "excel": File_types.EXCEL,
}


class ManagerException(Exception):
    """
    Special Exception type for view error_manager, generated only by error manager and catches in main button function
    (view_window.collect_information_with_error_check)
    """
    pass


def exec_function_with_error_check(function):
    try:
        function()
    except ManagerException:
        return


class view_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.visibility_current_states = {self.ui.saveFileInnerFrame: False, self.ui.writeDataInnerFrame: True,
                                          self.ui.inputFileInnerFrame: False}
        self._connectSignalsSlots()

        self.error_message = QMessageBox()
        self.error_message.setIcon(QMessageBox.Critical)

        self.managers = {ve.VIEW_MANAGERS.OUTPUT_FUNCTION: self._output_dataFrame,
                         ve.VIEW_MANAGERS.ERROR_MANAGER: self._show_error_message}
        with open('config.yaml', 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        self.controller = controller.controller(self.managers, data)
        self.save_directory = None

        self.yaml_data = data
        self.set_tool_tips()
        self.setWindowTitle(
            QtCore.QCoreApplication.translate("MainWindow", self.yaml_data["main_window"]["program_name"]))

    def set_tool_tips(self):
        """
        The function loads all the tips to the widget applications. The hints are taken from the yaml file
        """
        _translate = QtCore.QCoreApplication.translate
        self.ui.inputFileFrame.setToolTip(
            _translate("MainWindow", self.yaml_data["tool_tips"]["input_file_tip"]))
        self.ui.saveToFileButton.setToolTip(
            _translate("MainWindow", self.yaml_data["tool_tips"]["save_file_tip"]))

    def _show_error_message(self, informative_text):
        """
        The function presents any program error as a pop-up error window
        """
        self.error_message.setInformativeText(informative_text)
        self.error_message.setWindowTitle(self.yaml_data["errors"]["error_title"])
        self.error_message.exec_()
        raise ManagerException

    def _output_dataFrame(self, dataFrame):
        """
        The function connects the output data table to the visible widget
        """
        view_table_model = pandasModel.pandasModel(dataFrame)
        self.ui.tableView.setModel(view_table_model)
        self.ui.tableView.show()

    def _connectSignalsSlots(self):
        """
        The function connects actions to the visible buttons of the application
        """
        self.ui.saveFileInnerFrame.hide()
        self.ui.appendDataButton.hide()
        self.ui.saveFileFrame.hide()
        self.ui.inputFileInnerFrame.hide()
        self.ui.fileSavedText.hide()
        self.ui.tableView.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
        self.ui.calculateButton.clicked.connect(lambda: exec_function_with_error_check(self._collect_information))
        self.ui.cleanButton.clicked.connect(lambda: self.clean_data_view())
        self.ui.appendDataButton.clicked.connect(lambda: self.append_data_query())
        self.ui.browseButton.clicked.connect(lambda: exec_function_with_error_check(self.browse_input_file))
        self.ui.saveToFileButton.clicked.connect(lambda: exec_function_with_error_check(self.save_data_browser))
        self.ui.browesSaveButton.clicked.connect(lambda: exec_function_with_error_check(self.browse_save_file))

    def _hide_unhide_function(self, widget):
        if not self.visibility_current_states[widget]:
            widget.show()
            self.visibility_current_states[widget] = True
        else:
            widget.hide()
            self.visibility_current_states[widget] = False

    def _get_predictor_type(self):
        predictor_name = self.ui.processingTypeComboBox.currentText()
        return predictor_text_to_enum[predictor_name]

    def _get_input_file(self):
        input_file_name = self.ui.inputFileNameLineEdit.text()
        input_file_type = pd.get_file_extension_by_name(input_file_name)
        if not input_file_name or not input_file_type:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](self.yaml_data["errors"]["no_input_file_error"])
        return input_file_name, input_file_type

    def _get_save_file(self):
        """
        The function tries to read the file for saving and validates its extension
        """
        save_file_name = self.ui.saveFileNameLineEdit.text()
        save_file_type = pd.get_file_extension_by_name(save_file_name)
        if not save_file_name:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](self.yaml_data["errors"]["no_save_file_error"])
        return save_file_name, save_file_type

    def _get_writted_data(self):
        """
        The function tries to read the input data only from the values entered by the user
        """
        dna = self.ui.dnaSequenceLineEdit.text()
        salt_value = float(self.ui.NaLineEdit.text())
        Ct = float(self.ui.CtLineEdit.text())
        if not dna or not salt_value:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](
                self.yaml_data["errors"]["invalid_input_data_error"])
        return dna, salt_value, Ct

    def _collect_information(self):
        """
        The function prepares all input data and gives it to the main controller unit
        """
        user_information = {ve.INPUT_INFO.PREDICTOR_TYPE: self._get_predictor_type()}
        if not self.ui.writeDataInnerFrame.isHidden():
            try:
                dna, salt_value, Ct = self._get_writted_data()
            except Exception:
                self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](
                    self.yaml_data["errors"]["invalid_written_data_error"])
            user_information[ve.INPUT_INFO.DNA_DATA] = dna
            user_information[ve.INPUT_INFO.Ct] = Ct
            user_information[ve.INPUT_INFO.SALT_VALUE] = salt_value
            user_information[ve.INPUT_INFO.IS_ACTIVITY] = False
            user_information[ve.INPUT_INFO.IS_SALT] = True
        elif not self.ui.inputFileInnerFrame.isHidden():
            input_file_name, input_file_type = self._get_input_file()
            user_information[ve.INPUT_INFO.INPUT_FILE_NAME] = input_file_name
            user_information[ve.INPUT_INFO.INPUT_FILE_TYPE] = input_file_type
        else:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](
                self.yaml_data["errors"]["no_input_types_error"])

        self.controller.parse_info_and_calculate_parameters(user_information)

    def clean_data_view(self):
        """
        The function clears the output table in the application if there are any
        """
        self.controller.input_data = None
        self.controller.predictions = None
        self.ui.tableView.setModel(None)

    def append_data_query(self):
        self.ui.writeDataInnerFrame.show()
        self.ui.inputFileInnerFrame.hide()
        self.ui.appendDataButton.hide()

    def browse_input_file(self):
        """
        The function tries to read data from a file entered by the user
        """
        Secuence_label, Na_label, Ct_label = self.yaml_data["input_data_labels"]["sequence"], \
            self.yaml_data["input_data_labels"]["Na_m"], \
            self.yaml_data["input_data_labels"]["Ct_m"]
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        file_name = fname[0]
        if len(file_name) == 0:
            return
        file_ext = pd.get_file_extension_by_name(file_name)
        if file_ext is None:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](self.yaml_data["errors"]["invalid_input_file_type_error"])
        read_function = pd.pandas_readers[file_ext]
        data = read_function(file_name)
        try_with_names_data = data.drop(
            columns=[col for col in data.columns if col not in [Secuence_label, Na_label, Ct_label]])

        if Secuence_label not in try_with_names_data:
            data = self.try_without_names(data)
        else:
            data = self.prepare_data_with_names(try_with_names_data)

        output_streams = self.controller._make_output_streams()
        output_streams[0] << data
        self.controller.predictions = None
        self.controller.input_data = None

        self.controller.input_file_data = data
        self.ui.inputFileNameLineEdit.setText(file_name)
        self.ui.inputFileInnerFrame.show()
        self.ui.writeDataInnerFrame.hide()
        self.ui.appendDataButton.show()

    def get_valid_float_parameter_from_line_edit(self, line_edit, error_message):
        try:
            valid_parameter = float(line_edit.text())
        except Exception:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](error_message)
        return valid_parameter

    def browse_save_file(self):
        """
        The function allows you to select the path to the file in the browser and draws it in the application
        """
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        split_name = folder_path.partition(".")
        if len(split_name) > 3:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](
                self.yaml_data["errors"]["folder_not_choosen_error"])
        self.ui.saveDirectoryLineEdit.setText(folder_path)

    def save_data_browser(self):
        """
        The function saves the output data to a file
        """
        if self.controller.predictions is None:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](self.yaml_data["errors"]["nothing_to_save_error"])
        if self.ui.saveFileInnerFrame.isHidden():
            self.ui.saveFileFrame.show()
            self.ui.saveFileInnerFrame.show()
            return
        save_file_name = self.ui.saveFileNameLineEdit.text()
        save_file_type = pd.get_file_extension_by_name(save_file_name)
        if save_file_type is None:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](self.yaml_data["errors"]["invalid_save_file_error"])
        save_directory = self.ui.saveDirectoryLineEdit.text()
        if len(save_directory) == 0:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](self.yaml_data["errors"]["no_save_directory_error"])
        save_file_name = save_directory + "/" + save_file_name
        predictions = pd._make_output_DataFrame(self.controller.predictions, self.controller.input_data,
                                                output_table_columns.output_column_str_name_list, decimals=5,
                                                column_options=output_table_columns.output_column_str_options_list)
        output_stream = output_stream_classes.file_output_stream(save_file_name=save_file_name,
                                                                 save_file_type=save_file_type,
                                                                 error_manager=self.controller.error_manager,
								 yaml_data=self.yaml_data)

        output_stream << predictions
        self.showSavedInOneSecond()

    def showSavedInOneSecond(self):
        self.ui.fileSavedText.show()
        timer = QTimer()
        timer.singleShot(1000, lambda: self.ui.fileSavedText.hide())

    def calculateNaAndCt(self, data, Na_label, Ct_label):
        if Na_label not in data:
            default_Na = self.get_valid_float_parameter_from_line_edit(self.ui.NaLineEdit,
                                                                       self.yaml_data["errors"]["no_Na_in_file"])
            data.insert(1, output_column_names[DataColumns.Na], [default_Na for _ in range(data.shape[0])])

        if Ct_label not in data:
            default_Ct = self.get_valid_float_parameter_from_line_edit(self.ui.CtLineEdit,
                                                                       self.yaml_data["errors"]["no_Ct_in_file"])
            data.insert(2, output_column_names[DataColumns.Ct], [default_Ct for _ in range(data.shape[0])])
        return

    def prepare_data_with_names(self, data):
        Na_label, Ct_label = self.yaml_data["input_data_labels"]["Na_m"], self.yaml_data["input_data_labels"]["Ct_m"]
        self.calculateNaAndCt(data, Na_label, Ct_label)
        return data

    def try_without_names(self, data):
        Sequence_label, Na_label, Ct_label = self.yaml_data["input_data_labels"]["sequence"], \
            self.yaml_data["input_data_labels"]["Na_m"], \
            self.yaml_data["input_data_labels"]["Ct_m"]
        if len(data.columns) == 3:
            data.columns = [Sequence_label, Na_label, Ct_label] + [f'Column_{i}' for i in range(3, len(data.columns))]
        elif len(data.columns) == 2:
            data.columns = [Sequence_label, Na_label] + [f'Column_{i}' for i in range(2, len(data.columns))]
        elif len(data.columns) == 1:
            data.columns = [Sequence_label] + [f'Column_{i}' for i in range(1, len(data.columns))]
        self.calculateNaAndCt(data, Na_label, Ct_label)
        return data
