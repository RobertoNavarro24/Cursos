from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton

class Computadora:
    contador_computadoras = 0

    @classmethod
    def aumentar_computadoras(cls):
        cls.contador_computadoras += 1
        return cls.contador_computadoras

    def __int__(self, Nombre:str, Monitor: Monitor, Teclado: Teclado, Raton: Raton):
        self.idComputadora = Computadora.aumentar_computadoras()
        self._Nombre = Nombre
        self._Monitor = Monitor
        self._Teclado = Teclado
        self._Raton = Raton

    @property
    def Monitor(self):
        return self._Monitor

    @Monitor.setter
    def Monitor(self, Monitor: Monitor):
        self._Monitor = Monitor

    @property
    def Monitor(self):
        return self._Monitor

    @Monitor.setter
    def Monitor(self, Monitor: Monitor):
        self._Monitor = Monitor

    @property
    def Teclado(self):
        return self._Teclado

    @Teclado.setter
    def Teclado(self, Teclado: Teclado):
        self._Teclado = Teclado

    @property
    def Raton(self):
        return self._Teclado

    @Raton.setter
    def Raton(self, Raton: Raton):
        self._Raton = Raton


if __name__ == '__main__':
    monitor1 = Monitor("HP", 15)
    monitor2 = Monitor("Acer", 27)
    monitor3 = Monitor("Gamer", 45)
    raton1 = Raton("usb", "HP")
    raton2 = Raton("bluetooth", "Acer")
    raton3 = Raton("usb", "Gamer")
    teclado1 = Teclado("usb", "HP")
    teclado2 = Teclado("bluetooth", "Acer")
    teclado3 = Teclado("usb", "Gamer")
