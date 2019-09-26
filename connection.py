from wifi import Cell, Scheme
from threading import Timer
import requests

from config import scanner_id


class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)


def heartbeat_tick():
    try:
        r = requests.post(
            'https://scancash.herokuapp.com/scanners/heatbeat',
            data={
                'scanner_id': scanner_id,
            })
    except (requests.ConnectionError, requests.Timeout) as e:
        pass


def connect(ssid, password):
    cell = Cell().from_string(ssid)
    scheme = Scheme.for_cell('wlan0', 'home', cell, password)
    scheme.save()
    scheme.activate()


# inform backend that the scanner is online
t = RepeatingTimer(30.0, heartbeat_tick)
t.start()
