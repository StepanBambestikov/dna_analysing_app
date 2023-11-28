from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QAbstractScrollArea
from widgets import Ui_MainWindow
import view_enum as ve
from predictor_types import Predictor_types
from file_types import File_types
import controller
import pandasModel
import output_table_columns
import output_stream_classes
import pandas_adapter as pd
from PyQt5.QtCore import QTimer
from output_table_columns import DataColumns, output_column_names

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
        self.controller = controller.controller(self.managers)
        self.save_directory = None

    def _show_error_message(self, informative_text):
        self.error_message.setInformativeText(informative_text)
        self.error_message.setWindowTitle("Error!")
        self.error_message.exec_()
        raise ManagerException

    def _output_dataFrame(self, dataFrame):
        view_table_model = pandasModel.pandasModel(dataFrame)
        self.ui.tableView.setModel(view_table_model)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.show()

    def _connectSignalsSlots(self):
        self.ui.saveFileInnerFrame.hide()
        self.ui.appendDataButton.hide()
        self.ui.saveFileFrame.hide()
        self.ui.inputFileInnerFrame.hide()
        self.ui.fileSavedText.hide()
        self.ui.tableView.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
        # self.ui.saveFileCheckBox.clicked.connect(lambda: self._hide_unhide_function(self.ui.saveFileInnerFrame))
        # self.ui.writeDataCheckBox.clicked.connect(lambda: self._hide_unhide_function(self.ui.writeDataInnerFrame))
        # self.ui.inputFileCheckBox.clicked.connect(lambda: self._hide_unhide_function(self.ui.inputFileInnerFrame))
        self.ui.calculateButton.clicked.connect(lambda: self.exec_function_with_error_check(self._collect_information))
        self.ui.cleanButton.clicked.connect(lambda: self.clean_data_view())
        self.ui.appendDataButton.clicked.connect(lambda: self.append_data_query())
        self.ui.browseButton.clicked.connect(lambda: self.exec_function_with_error_check(self.browse_input_file))
        self.ui.saveToFileButton.clicked.connect(lambda: self.exec_function_with_error_check(self.save_data_browser))
        self.ui.browesSaveButton.clicked.connect(lambda: self.exec_function_with_error_check(self.browse_save_file))

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
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER]("There is no input file name")
        return input_file_name, input_file_type

    def _get_save_file(self):
        save_file_name = self.ui.saveFileNameLineEdit.text()
        save_file_type = pd.get_file_extension_by_name(save_file_name)
        if not save_file_name:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER]("There is no save file name")
        return save_file_name, save_file_type

    def _get_writed_data(self):
        dna = self.ui.dnaSequenceLineEdit.text()
        #todo change buttons in right order!
        salt_value = float(self.ui.NaLineEdit.text())
        Ct = float(self.ui.CtLineEdit.text())
        if not dna or not salt_value:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](
                "Entered data isn't complete. Some of the fields (dna, salt_value) are empty")
        return dna, salt_value, Ct

    def _collect_information(self):
        user_information = {ve.INPUT_INFO.PREDICTOR_TYPE: self._get_predictor_type()}
        if not self.ui.writeDataInnerFrame.isHidden():
            try:
                dna, salt_value, Ct = self._get_writed_data()
            except Exception:
                self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](
                    "Invalid written data")
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
                "Neither of input types are chosen. Select input file or enter the data by yourself")

        self.controller.parse_info_and_calculate_parameters(user_information)
        # if not self.ui.inputFileInnerFrame.isHidden():
        #     self.ui.inputFileInnerFrame.hide()
        #     self.ui.appendDataButton.show()

    def exec_function_with_error_check(self, function):
        try:
            function()
        except ManagerException:
            return

    def clean_data_view(self):
        self.controller.input_data = None
        self.controller.predictions = None
        self.ui.tableView.setModel(None)

    def append_data_query(self):
        self.ui.writeDataInnerFrame.show()
        self.ui.inputFileInnerFrame.hide()
        self.ui.appendDataButton.hide()

    def browse_input_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        file_name = fname[0]
        if len(file_name) == 0:
            return
        file_ext = pd.get_file_extension_by_name(file_name)
        if file_ext is None:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER]("Invalid input file type, you can use only excel and csv files!")
        read_function = pd.pandas_readers[file_ext]
        data = read_function(file_name)
        data = data.drop(columns=[col for col in data.columns if col not in ['Sequence', "[Na+] (M)", "Ct (M)"]])

        if "Sequence" not in data:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](
                "Invalid input file, there is no Sequence column!")

        if "[Na+] (M)" not in data:
            default_Na = self.get_valid_float_parameter_from_line_edit(self.ui.NaLineEdit,
                                                                       "There is no Na in file and in default text item!")
            data.insert(1, output_column_names[DataColumns.Na], [default_Na for _ in range(data.shape[0])])

        if "Ct (M)" not in data:
            default_Ct = self.get_valid_float_parameter_from_line_edit(self.ui.CtLineEdit,
                                                                       "There is no Ct in file and in default text item!")
            data.insert(2, output_column_names[DataColumns.Ct], [default_Ct for _ in range(data.shape[0])])

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
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        splitted_name = folder_path.partition(".")
        if len(splitted_name) > 3:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](
                "It is needed to choose folder, not file!")
        self.ui.saveDirectoryLineEdit.setText(folder_path)

    # def save_data_to_file(self):
    #     if self.controller.predictions is None:
    #         self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER]("Nothing to save to file yet!")
    #     save_file_name, save_file_type = self._get_save_file()
    #     predictions = pd._make_output_DataFrame(self.controller.predictions, self.controller.input_data,
    #                                             output_table_columns.output_column_str_name_list)
    #     output_stream = output_stream_classes.file_output_stream(save_file_name=save_file_name,
    #                                                              save_file_type=save_file_type,
    #                                                              error_manager=self.controller.error_manager)
    #
    #     output_stream << predictions

    def save_data_browser(self):
        if self.controller.predictions is None:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER]("Nothing to save to file yet!")
        if self.ui.saveFileInnerFrame.isHidden():
            self.ui.saveFileFrame.show()
            self.ui.saveFileInnerFrame.show()
            return
        save_file_name = self.ui.saveFileNameLineEdit.text()
        save_file_type = pd.get_file_extension_by_name(save_file_name)
        if save_file_type is None:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER]("invalid save file extention!")
        save_directory = self.ui.saveDirectoryLineEdit.text()
        if len(save_directory) == 0:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER]("no save directory!")
        save_file_name = save_directory + "/" + save_file_name
        predictions = pd._make_output_DataFrame(self.controller.predictions, self.controller.input_data,
                                                output_table_columns.output_column_str_name_list, decimals=5, column_options=output_table_columns.output_column_str_options_list)
        output_stream = output_stream_classes.file_output_stream(save_file_name=save_file_name,
                                                                 save_file_type=save_file_type,
                                                                 error_manager=self.controller.error_manager)

        output_stream << predictions
        self.showSavedInOneSecond()

    def showSavedInOneSecond(self):
        self.ui.fileSavedText.show()
        timer = QTimer()
        timer.singleShot(1000, lambda: self.ui.fileSavedText.hide())
