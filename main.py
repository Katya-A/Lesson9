from time import sleep
from datetime import datetime as dt


class TrafficLight:
    _modes = {'red': 7, 'yellow': 2, 'green': 15}
    _color = ''

    def running(self):
        for color, duration in self._modes.items():
            self._color = color
            start_time = dt.now()

            print(f"TrafficLight went into state ' {self._color}' "
                  f"on {duration} seconds")
            sleep(duration)
            print(f"TrafficLight leave state ' {self._color}' after " 
                  f"{(dt.now() - start_time).seconds} seconds ")


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
