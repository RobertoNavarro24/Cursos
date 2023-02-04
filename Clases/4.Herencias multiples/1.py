class FiguraGeometrica:
    def __init__(self, ancho: float, alto: float) -> None:
        self.ancho = ancho
        self.alto = alto


class Color:
    def __init__(self, color: str) -> None:
        self.color = color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, ancho: float, alto: float, color: str) -> None:
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto*self.ancho

cuadrado_1 = Cuadrado(10, 30, "azul")
print(f"Calculo area cuadrado: {cuadrado_1.calcular_area()}")
print(cuadrado_1.__class__.__mro__)