from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from main_controller import MainController
from main_model import MainModel
from view.dialog_view import DialogView


class MainView(QMainWindow):
    def __init__(self, model: MainModel, controller: MainController):
        super().__init__()
        self.dialog = None
        self._model = model
        self._controller = controller

        self._ui = uic.loadUi('ui/main.ui', self)
        self._ui.pushButton.clicked.connect(self.on_button_clicked)
        self._ui.lineEdit.textChanged.connect(self._controller.change_city)

    @pyqtSlot(str)
    def on_city_changed(self, value):
        self._ui.lineEdit.setText(self._model.city)

    def on_button_clicked(self):
        self.dialog = DialogView(self._model)
        self.dialog.show()






