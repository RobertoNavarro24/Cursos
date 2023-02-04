from Clases.MundoPC.DispositivoEntrada import DispositivoEntrada
class Teclado(DispositivoEntrada):
    contador_teclados = 0
    @classmethod
    def aumentar_teclados(cls):
        cls.contador_teclados += 1
        return cls.contador_teclados

    def __init__(self, tipoEntrada: str, marca: str) -> None:
        super().__init__(tipoEntrada, marca)
        self.idTeclado = Teclado.aumentar_teclados()

    def __str__(self) -> str:
        return f"Id: {self.idTeclado}, {super().__str__()}"


if __name__ == "__main__":
    teclado1 = Teclado("usb", "HP")
    teclado2 = Teclado("bluetooth", "Acer")
    teclado3 = Teclado("usb", "Gamer")
    print(teclado1)
    print(teclado2)
    print(teclado3)