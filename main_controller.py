from PyQt5.QtCore import QObject, pyqtSlot

from main_model import MainModel


class MainController(QObject):
    def __init__(self, model: MainModel):
        super().__init__()
        self._model = model

    @pyqtSlot(str)
    def change_city(self, city):
        self._model.city = city
