class Monitor:
    contador_monitores = 0
    @classmethod
    def aumentar_monitores(cls):
        cls.contador_monitores += 1
        return cls.contador_monitores

    def __int__(self, marca: str, tamano: int):
        self.idMonitor = Monitor.aumentar_monitores()
        self._marca = marca
        self._tamano = tamano

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca: str):
        self._marca = marca

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, tamano: str):
        self._tamano = tamano

    def __str__(self):
        return f"Id: {self.idMonitor}, marca: {self._marca}, tamaño: {self._tamano} pulgadas"

if __name__ == "__main__":
    monitor1 = Monitor("HP", 15)
    monitor2 = Monitor("Acer", 27)
    monitor3 = Monitor("Gamer", 45)

    print(monitor1)
    print(monitor2)
    print(monitor3)