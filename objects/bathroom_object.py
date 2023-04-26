class Faucet:
    def __init__(self):
        self._on = False

    def turn_on(self):
        self._on = True

    def turn_off(self):
        self._on = False

    def is_on(self):
        return self._on


class Loofah:
    def __init__(self):
        self._is_soapy = False

    def soap(self):
        self._is_soapy = True

    def clean(self):
        self._is_soapy = False


class Towel:
    def __init__(self):
        self._is_dry = True

    def dry(self):
        self._is_dry = True

    def wet(self):
        self._is_dry = False