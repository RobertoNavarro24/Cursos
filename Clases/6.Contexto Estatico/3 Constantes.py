class Persona:
    numero_de_personas = 0

    @classmethod
    def nueva_persona(cls):
        cls.numero_de_personas += 1
        return cls.numero_de_personas

    def __init__(self, nombre: str, edad: int) -> None:
        self.id_persona = Persona.nueva_persona()
        self._nombre = nombre
        self._edad = edad

    def __str__(self) -> str:
        return f"Persona: {self.id_persona} Nombre: {self._nombre} Edad: {self._edad}"


persona_1 = Persona("Roberto", 25)
persona_2 = Persona("Rubi", 23)

print(persona_1)
print(persona_2)
