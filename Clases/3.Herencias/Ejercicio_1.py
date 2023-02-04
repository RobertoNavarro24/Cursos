class Vehiculo:
    def __init__(self, color: str, ruedas: int) -> None:
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self) -> str:
        return f"Color: {self.color} Ruedas: {self.ruedas}"


class Coche(Vehiculo):
    def __init__(self, color: str, ruedas: int, velocidad: int) -> None:
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self) -> str:
        return f"{super().__str__()} Velocidad: {self.velocidad}"


class Bicicleta(Vehiculo):
    def __init__(self, color: str, ruedas: int, tipo: str) -> None:
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self) -> str:
        return f"{super().__str__()} Tipo: {self.tipo}"


coche_1 = Coche("Rojo", 4, 100)
print(coche_1)
bicicleta_1 = Bicicleta("Azul", 2, "Montañas")
print(bicicleta_1)