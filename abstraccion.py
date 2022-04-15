class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque(temperatura)
        self._añadir_jabon()
        