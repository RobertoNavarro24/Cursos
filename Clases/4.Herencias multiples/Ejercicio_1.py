# Python program showing the use of
# @property

class FiguraGeometrica:
    def __init__(self, alto: float, ancho: float) -> None:
        self._alto = alto
        self._ancho = ancho

    def __str__(self) -> str:
        return f"Alto: {self._alto} Ancho: {self._ancho}"

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto: float):
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho: float):
        self._ancho = ancho


class Color: 
    def __init__(self, color: str) -> None:
        self._color = color
    
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: str):
        self._color = color

    def __str__(self) -> str:
        return f"Color: {self._color}"


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, alto: float, ancho: float, color: str) -> None:
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def area(self):
        return self._alto * self._ancho
    
    def __str__(self) -> str:
        return f"Cuadrado: {FiguraGeometrica.__str__(self)} {Color.__str__(self)}"

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto: float, ancho: float, color: str) -> None:
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def area(self):
        return self._alto * self._ancho
    
    def __str__(self) -> str:
        return f"Rectangulo: {FiguraGeometrica.__str__(self)} {Color.__str__(self)}"


cuadrado_1 = Cuadrado(10,10, "Azul")
print(cuadrado_1)
print(f"El area del cuadrado es: {cuadrado_1.area()}")


rectangulo_1 = Rectangulo(10,30, "Rojo")
print(rectangulo_1)
print(f"El area del rectangulo es: {rectangulo_1.area()}")