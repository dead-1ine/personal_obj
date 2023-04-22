# 샤워 루틴

class Faucet:
    def __init__(self):
        self._on = False

    def turn_on(self):
        self._on = True

    def turn_off(self):
        self._on = False

    def is_on(self):
        return self.on

