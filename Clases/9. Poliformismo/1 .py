class Empleado:
    def __init__(self, nombre: str, sueldo: str) -> None:
        self.nombre = nombre
        self.sueldo = sueldo
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} Sueldo: {self.sueldo}"

class Gerente(Empleado):
    def __init__(self, nombre: str, sueldo: str, departamento: str) -> None:
        super().__init__(nombre, sueldo)
        self.departamento = departamento
    
    def __str__(self) -> str:
        return f"{super().__str__()} Departamento: {self.departamento}"


def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))

empleado = Empleado("Raul", 100)
gerente = Gerente("Pedro", 200, "Ali")
imprimir_detalles(empleado)
imprimir_detalles(gerente)

