# This Python file uses the following encoding: utf-8
import sys
import math
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject
import numpy as np
import pyqtgraph as pg
import MainWindowForm
from InputDataEditor import InputDataEditor
from InputDataEditor import EnumDecisions


class MainWindow(QMainWindow, MainWindowForm.Ui_MainWindow):
    """Главное окно"""
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pbStart1.clicked.connect(self.start_1)
        self.pbStart2.clicked.connect(self.start_2)
        self.pbStart3.clicked.connect(self.start_3)
        self.pbClose.clicked.connect(self.close)
        self.pbClosePirint.clicked.connect(self.choose_decision)
        self.choose_decision()
        self.start_decision = None
        self.view = None

    def print_text(self, text, is_error):
        """Если нужно вывести ответ в виде текста"""
        self.chooseStage.hide()
        self.printStage.show()
        self.printStage.setCurrentIndex(EnumDecisions.DECISION_1)
        self.pbClosePirint.show()
        self.setFixedSize(750, 400)
        self.linePrint.setReadOnly(False)
        self.linePrint.setText(str(text))
        self.linePrint.setReadOnly(True)
        if is_error:
            self.linePrint.setStyleSheet("background-color: #f8877e")
        else:
            self.linePrint.setStyleSheet("background-color: #FFFFFF")

    def print_graph(self, type, title, list_init, list_culc):
        """Если нужно вывести ответ в виде графика"""
        self.chooseStage.hide()
        self.printStage.show()
        self.printStage.setCurrentIndex(EnumDecisions.DECISION_2)
        self.pbClosePirint.show()
        self.setFixedSize(1000, 700)
        self.setMaximumHeight(1000)
        self.setMaximumWidth(2000)
        self.view = pg.PlotWidget()
        self.view.setTitle(str(title), color="w", size="16pt")
        if type == EnumDecisions.DECISION_2:
            self.view.plot(list_init, pen=(100, 100, 100),
                           symbol='t', symbolPen=None, symbolSize=10,
                           symbolBrush=(100, 100, 100, 255))
            self.view.plot(list_culc, pen=(100, 200, 200),
                           symbol='t', symbolPen=None, symbolSize=10,
                           symbolBrush=(255, 100, 155, 255))
        elif type == EnumDecisions.DECISION_3:
            self.view.plot(list_init, list_culc,
                           pen=(130, 40, 250), symbol='t', symbolPen=None,
                           symbolSize=10, symbolBrush=(100, 100, 100, 255))
        else:
            self.print_text("Упс... что то пошло не так", True)
        self.view.showGrid(x=True, y=True)
        self.viewLayout.addWidget(self.view)

    def choose_decision(self):
        """Открытие выбора задания"""
        self.chooseStage.show()
        self.printStage.hide()
        self.pbClosePirint.hide()
        self.setFixedSize(750, 400)
        self.clear_layout(self.viewLayout)

    def start_1(self):
        """Создание класса для 1 задания"""
        self.start_decision = FirstDecision()

    def start_2(self):
        """Создание класса для 2 задания"""
        self.start_decision = SecondDecision()

    def start_3(self):
        """Создание класса для 3 задания"""
        self.start_decision = ThirdDecision()

    def clear_layout(self, layout):
        """Вспомогательная функция для очистки графиков при завершении работы"""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
#        self.decision2.culculate(3,"1,2,3,4,5,6,7,8,9,10")


class BaseDecision(QObject):
    """Базовый класс для работы с заданиями"""
    def __init__(self, parent=None):
        super().__init__()
        self.input_data_editor = None

    def inputStart(self, type):
        """Отсюда открытие окна входных данных и соединения с ним"""
        self.input_data_editor = InputDataEditor(self, type)
        self.input_data_editor.communicate.signal_acceptApp.connect(self.culculate)
        self.input_data_editor.communicate.signal_closeApp.connect(self.input_data_editor.close)
        self.input_data_editor.communicate.signal_closeApp.connect(window.show)
        self.input_data_editor.show()
        window.close()
    @classmethod
    def print_text(cls, text, is_error=False):
        """Отсюда вывод текста"""
        window.print_text(text, is_error)
    @classmethod
    def print_graph(cls, type, title, list_init, list_culc):
        window.print_graph(type, title, list_init, list_culc)
    @classmethod
    def culculate(cls):
        """В каждом унаследованном классе от базового своя реализация расчета"""
        print("culculate BASE")


class FirstDecision(BaseDecision):
    """Класс задания - энтропия"""
    def __init__(self):
        super().__init__()
        self.inputStart(EnumDecisions.DECISION_1)
        print(EnumDecisions.DECISION_1)

    def culculate(self, data):
        # Подсчет для первого задания
        var_a = np.fromstring(data, dtype=int, sep=',')
        var_a = list(filter(lambda x: x != 0, var_a))
        if not len(var_a) == 0:
            p_var_a = var_a / sum(var_a)
            shannon = -np.sum(p_var_a * np.log2(p_var_a))
            self.print_text(str(shannon))
        else:
            self.print_text("Ну с такими входными данными "
                           "тут нечего смотреть...", True)


class SecondDecision(BaseDecision):
    """Класс задания - скользящие средние"""
    def __init__(self):
        super().__init__()
        self.inputStart(EnumDecisions.DECISION_2)
        self.list_init = []

    def culculate(self, data,  window_size):
        """Подсчет для второго задания"""
        window_size = int(window_size)
        self.list_init = [float(i) for i in data.split(",")]
        try:
            culc_sma = self._sma(self.list_init, window_size)
        except Exception as exp:
            self.print_text("Такой результат, потому что: ->  "
                           + str(exp) + "  <-", True)
        try:
            culc_ema = self._ema(self.list_init, window_size)
        except Exception as exp:
            self.print_text("Такой результат, потому что: ->  "
                           + str(exp) + "  <-", True)
        else:
            self.print_graph(EnumDecisions.DECISION_2, "SMA", self.list_init, culc_sma)
            self.print_graph(EnumDecisions.DECISION_2, "EMA", self.list_init, culc_ema)

    def _sma(self, data, period):
        """Подсчет простой скользящей средней"""
        if len(data) == 0:
            raise Exception("Что кто-то и зачем-то не дает мне данные")
        if period <= 0:
            raise Exception("Слишком маленький период, "
                            "так не получится посчитать SMA")

        interm = 0
        result = []
        for i, _v in enumerate(data):
            interm += _v
            if (i+1) < period:
                result.append(math.nan)
            else:
                result.append(interm/float(period))
                interm -= data[i+1-period]
        return result

    def _ema(self, data, period):
        """Подсчет экпон скользящей средней"""
        if period <= 1:
            raise Exception("Слишком маленький период, "
                            "так не получится посчитать EMA")

        sma = self._sma(data, period)
        multiplier = 2/(float(period+1))
        result = []

        for k, _v in enumerate(sma):
            if math.isnan(_v):
                result.append(math.nan)
            else:
                prev = result[k-1]
                if math.isnan(prev):
                    result.append(_v)
                    continue
                ema = (data[k]-prev)*multiplier + prev
                result.append(ema)
        return result


class ThirdDecision(BaseDecision):
    """Класс задания - монте-карло"""
    def __init__(self):
        super().__init__()
        self.min_a = 100
        self.max_a_1 = 100
        self.max_a_2 = 1000
        self.max_a_3 = 5000
        self.max_a_4 = 10000
        self.max_a_5 = 50000
        self.max_a_6 = 100000
        self.max_a_7 = 150000
        self.max_a_8 = 300000
        self.max_a_9 = 500000
        self.max_a_10 = 1000000
        self.max_a_11 = 2500000
        self.max_a_12 = 5000000
        self.max_a_13 = 10000000

        self.culc_list = []
        self.list = [self.max_a_1, self.max_a_2, self.max_a_3,
                     self.max_a_4, self.max_a_5, self.max_a_6,
                     self.max_a_7, self.max_a_8, self.max_a_9,
                     self.max_a_10, self.max_a_11, self.max_a_12]
        for i in self.list:
            self.culculate(i)
        self.print_graph(EnumDecisions.DECISION_3, "Монте-Карло",
                        self.list, self.culc_list)

    def culculate(self, max_a):
        """Подсчет для третьего задания"""
        self._pi = 0.0
        for i in range(max_a):
            _x = random.random()
            _y = random.random()
            self._pi += (_x * _x + _y * _y < 1.0)
        self.culc_list.append(4 * self._pi / max_a)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
