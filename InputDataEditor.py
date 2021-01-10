# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QObject
import pandas as pd
import InputDataEditorForm


class Communicate(QObject):
    """Свои сигналы для передачи информации"""
    signal_closeApp = pyqtSignal()
    signal_acceptApp = pyqtSignal((str), (str))


class EnumDecisions():
    """Номера заданий"""
    DECISION_1 = 0
    DECISION_2 = 1
    DECISION_3 = 2


class EnumStages():
    """Номера ступеней для правильного оторажения"""
    ERROR = -1
    STAGE_START = 0
    STAGE_END = 1
    STAGE_CLOSE = -2


class InputDataEditor(QDialog, InputDataEditorForm.Ui_Dialog):
    """Диалоговое окно"""
    def __init__(self, parent, type):
        super().__init__(None)
        parent = None
        self._data = ""
        self.communicate = Communicate()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.set_type(type)
        self.set_stage(EnumStages.STAGE_START)
        self.pbClose.clicked.connect(self.close_dialog)
        self.pbAccept.clicked.connect(self.accept_action)
        self.pbDefaultWin.clicked.connect(self.set_default_win)
        self.pbOpenDialog.clicked.connect(self.open_dialog)
        self.pbClean.clicked.connect(self.dialogData.clear)
        self.sbVariant.valueChanged.connect(self.dialogData.clear)
        self.data1.textChanged.connect(self.set_data)
        self.data1.clear()
        self.str_list = [""]

    def close_dialog(self):
        """Закрытие текущего окна,
           cигнал для передачи в главное окно сигнала о закрытие"""
        self.communicate.signal_closeApp.emit()

    def set_default_win(self):
        """Кнопка *По умолчанию*"""
        self.windowSize.setValue(3)

    def set_data(self, text):
        """Заполнение данных из текущей формы для проверки и отправки"""
        self._data = text

    def get_stage(self):
        """Получаем этап для правильного отображения на экране"""
        stage = EnumStages.ERROR
        if self.stage1.isVisible():
            stage = EnumStages.STAGE_START
        if self.stage2.isVisible() or self._type == EnumDecisions.DECISION_1:
            stage = EnumStages.STAGE_END
        return stage

    def set_stage(self, stage):
        """Задаем этап для правильного отображения на экране"""
        if stage == EnumStages.STAGE_START:
            self.stage1.show()
            self.stage2.hide()
        elif stage == EnumStages.STAGE_END:
            self.stage1.hide()
            self.stage2.show()
        elif stage == EnumStages.STAGE_CLOSE:
            self.close_dialog()
        else:
            self.close_dialog()

    def set_type(self, type):
        """Задаем отображение"""
        self._type = type
        self.stage1.setCurrentIndex(self._type)

    def open_dialog(self):
        """Открытие выбора файла"""
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '/home', ".xls(*.xls)")[0]
        if fname:
            file = (fname)
            open_xl = pd.ExcelFile(file)
            dfs = pd.read_excel(file, sheet_name=open_xl.sheet_names[0])
            i = 1
            self.str_list.clear()
            while i < len(dfs.columns):
                self.str_list.append(str(dfs.at[self.sbVariant.value() - 1, i]))
                i += 1
            self.dialogData.clear()
            self.dialogData.setReadOnly(False)
            self.dialogData.setText(str(self.str_list))
            self.dialogData.setReadOnly(True)
            self.set_data(self.dialogData.text())
        self.validator_fields()

    def validator_fields(self):
        """Проверка полей введенных пользователем"""
        is_valid = False
        if not self._data == "":
            self._data = self._data.replace("'", "")
            self._data = self._data.replace(" ", "")
            self._data = self._data.replace("[", "")
            self._data = self._data.replace("]", "")
            self.data1.setStyleSheet("background-color: #FFFFFF")
            self.dialogData.setStyleSheet("background-color: #FFFFFF")
            is_valid = True
        else:
            self.data1.setStyleSheet("background-color: #f8877e")
            self.dialogData.setStyleSheet("background-color: #f8877e")
            is_valid = False
        return is_valid

    def accept_action(self):
        """Действие при кнопке подтвердить"""
        stage = self.get_stage()
        if not stage == EnumStages.ERROR:
            if stage == EnumStages.STAGE_START:
                if self.validator_fields():
                    self.set_stage(EnumStages.STAGE_END)
            elif stage == EnumStages.STAGE_END:
                if self.validator_fields():
                    self.communicate.signal_acceptApp.emit(self._data, str(self.windowSize.value()))
                    self.set_stage(EnumStages.STAGE_CLOSE)
        else:
            self.close_dialog()
