from PyQt5.QtCore import QObject, pyqtSignal
from pyowm import OWM
from pyowm.weatherapi25.observation import Observation
from pyowm.utils import config as cfg

class MainModel(QObject):
    city_changed = pyqtSignal(str)

    def __init__(self, owm_api_key):
        config = cfg.get_default_config()
        config['language'] = 'ru'
        self.weather = OWM(owm_api_key, config).weather_manager()
        self._city = ''
        super().__init__()

    def get_from_place(self, place: str) -> Observation:
        return self.weather.weather_at_place(place)

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
        self.city_changed.emit(value)



