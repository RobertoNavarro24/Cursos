class Persona:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self._first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __str__(self) -> str:
        return f"Persona: {self._first_name} {self.last_name} {self.age}"

    @property
    def first_name(self):
        return self._first_name

class Empleado(Persona):
    def __init__(self, first_name: str, last_name: str, age: int, sueldo: int) -> None:
        super().__init__(first_name, last_name, age)
        self.sueldo = sueldo
    
    def __str__(self) -> str:
        return f"{super().__str__()} {self.sueldo}"




if __name__ == "__main__":
    empleado_1 = Empleado("Roberto", "Navarro", 25, 4000)
    print(empleado_1)