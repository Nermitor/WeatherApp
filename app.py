import sys
from PyQt5.QtWidgets import QApplication

from main_controller import MainController
from main_model import MainModel
from view.main_view import MainView
from dotenv import dotenv_values


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = MainModel(dotenv_values()['owm_key'])
        self.main_controller = MainController(self.model)
        self.main_view = MainView(self.model, self.main_controller)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())