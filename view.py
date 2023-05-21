from PyQt5.QtWidgets import QMainWindow, QMessageBox
from widgets import Ui_MainWindow
import view_enum as ve
from predictor_types import Predictor_types
from file_types import File_types
import controller
import pandasModel

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
        self.visibility_current_states = {self.ui.saveFileInnerFrame: False, self.ui.writeDataInnerFrame: False,
                                          self.ui.inputFileInnerFrame: False}
        self._connectSignalsSlots()

        self.error_message = QMessageBox()
        self.error_message.setIcon(QMessageBox.Critical)

        self.managers = {ve.VIEW_MANAGERS.OUTPUT_FUNCTION: self._output_dataFrame,
                         ve.VIEW_MANAGERS.ERROR_MANAGER: self._show_error_message}
        self.controller = controller.controller(self.managers)

    def _show_error_message(self, informative_text):
        self.error_message.setInformativeText(informative_text)
        self.error_message.setWindowTitle("Error!")
        self.error_message.exec_()
        raise ManagerException

    def _output_dataFrame(self, dataFrame):
        view_table_model = pandasModel.pandasModel(dataFrame)
        self.ui.tableView.setModel(view_table_model)
        self.ui.tableView.show()

    def _connectSignalsSlots(self):
        self.ui.saveFileInnerFrame.hide()
        self.ui.writeDataInnerFrame.hide()
        self.ui.inputFileInnerFrame.hide()
        self.ui.saveFileCheckBox.clicked.connect(lambda: self._hide_unhide_function(self.ui.saveFileInnerFrame))
        self.ui.writeDataCheckBox.clicked.connect(lambda: self._hide_unhide_function(self.ui.writeDataInnerFrame))
        self.ui.inputFileCheckBox.clicked.connect(lambda: self._hide_unhide_function(self.ui.inputFileInnerFrame))
        self.ui.calculateButton.clicked.connect(lambda: self.collect_information_with_error_check())

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
        input_file_type_str = self.ui.inputFileTypeComboBox.currentText()
        if not input_file_name or not input_file_type_str:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER]("There is no input file name")
        return input_file_name, text_file_type_to_enum[input_file_type_str]

    def _get_save_file(self):
        save_file_name = self.ui.saveFileNameLineEdit.text()
        save_file_type_str = self.ui.saveFileTypeComboBox.currentText()
        if not save_file_name or not save_file_type_str:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER]("There is no save file name")
        return save_file_name, text_file_type_to_enum[save_file_type_str]

    def _get_writed_data(self):
        dna = self.ui.dnaSequenceLineEdit.text()
        #todo change buttons in right order!
        salt_value = float(self.ui.ValueLineEdit.text())
        Ct = float(self.ui.CtLineEdit.text())
        is_activity = self.ui.IsActivityRadioButton.isChecked()
        is_salt = self.ui.IsSaltRadioButton.isChecked()
        if not dna or not salt_value:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](
                "Entered data isn't complete. Some of the fields (dna, salt_value) are empty")
        return dna, salt_value, Ct, is_activity, is_salt

    def _collect_information(self):
        user_information = {ve.INPUT_INFO.PREDICTOR_TYPE: self._get_predictor_type()}
        if self.visibility_current_states[self.ui.writeDataInnerFrame]:
            dna, salt_value, Ct, is_activity, is_salt = self._get_writed_data()
            user_information[ve.INPUT_INFO.DNA_DATA] = dna
            user_information[ve.INPUT_INFO.Ct] = Ct
            user_information[ve.INPUT_INFO.SALT_VALUE] = salt_value
            user_information[ve.INPUT_INFO.IS_ACTIVITY] = is_activity
            user_information[ve.INPUT_INFO.IS_SALT] = is_salt
        elif self.visibility_current_states[self.ui.inputFileInnerFrame]:
            input_file_name, input_file_type = self._get_input_file()
            user_information[ve.INPUT_INFO.INPUT_FILE_NAME] = input_file_name
            user_information[ve.INPUT_INFO.INPUT_FILE_TYPE] = input_file_type
        else:
            self.managers[ve.VIEW_MANAGERS.ERROR_MANAGER](
                "Neither of input types are chosen. Select input file or enter the data by yourself")

        if self.visibility_current_states[self.ui.saveFileInnerFrame]:
            save_file_name, save_file_type = self._get_save_file()
            user_information[ve.INPUT_INFO.OUTPUT_FILE_NAME] = save_file_name
            user_information[ve.INPUT_INFO.OUTPUT_FILE_TYPE] = save_file_type

        self.controller.parse_info_and_calculate_parameters(user_information)

    def collect_information_with_error_check(self):
        try:
            self._collect_information()
        except ManagerException:
            return
