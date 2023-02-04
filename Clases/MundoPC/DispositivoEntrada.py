class DispositivoEntrada:
    def __init__(self, tipoEntrada: str, marca: str) -> None:
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    def __str__(self) -> str:
        return f"marca: {self._marca}, tipo_entrada: {self._tipoEntrada}"

    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    @property
    def marca(self):
        return self._marca

    @tipoEntrada.setter
    def tipoEntrada(self, marca):
        self._marca = marca
