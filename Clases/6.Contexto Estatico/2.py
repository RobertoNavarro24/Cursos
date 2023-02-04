class MiClase:
    # Variables de la clase
    variables_clase = "Valor variable clase"
    
    def __init__(self, variable_instancia: str) -> None:
        # Variables del objeto
        self.variable_instancia = variable_instancia

    # Metodo Estatico
    @staticmethod
    def metodo_estatico():
        print(MiClase.variables_clase)

    # Metodo de Clase, cls es como el self para las variables o metodos de la clase
    # No de variables o metodos de objetos
    @classmethod
    def metodo_clase(cls):
        print(cls.variables_clase)

MiClase.metodo_clase()
