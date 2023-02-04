from Clases.MundoPC.DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0
    @classmethod
    def aumentar_ratones(cls):
        cls.contador_ratones += 1
        return cls.contador_ratones
    
    def __init__(self, tipoEntrada: str, marca: str) -> None:
        super().__init__(tipoEntrada, marca)
        self.idRaton = Raton.aumentar_ratones()

    def __str__(self) -> str:
        return f"Id: {self.idRaton}, {super().__str__()}"


if __name__ == "__main__":
    raton1 = Raton("usb", "HP")
    raton2 = Raton("bluetooth", "Acer")
    raton3 = Raton("usb", "Gamer")
    print(raton1)
    print(raton2)
    print(raton3)