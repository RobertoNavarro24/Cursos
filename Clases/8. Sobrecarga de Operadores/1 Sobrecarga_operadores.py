class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def __add__(self, otro):
        return f"{self.nombre} {otro.nombre}"


persona1 = Persona("Juan")
persona2 = Persona("Carlos")
print(persona1+persona2)