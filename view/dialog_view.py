from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from main_controller import MainController
from main_model import MainModel


class DialogView(QMainWindow):
    def __init__(self, model: MainModel, controller: MainController):
        super().__init__()
        self._model = model
        self._controller = controller

        self._ui = uic.loadUi('ui/dialog.ui', self)

        self._ui.pushButton.clicked.connect(self.close)
        self.load_weather_data()

    def load_weather_data(self):
        w = self._model.get_from_place(self._model.city).weather
        self._ui.label.setText(
            f'Город: {self._model.city}\nТемпература: {w.temperature("celsius")["temp"]}°C\nСкорость ветра: {w.wnd["speed"]} м/с\nВлажность: {w.humidity}%\nОблачность: {w.detailed_status}')
