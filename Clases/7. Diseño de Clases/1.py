class Producto:
    contador_productos = 0

    @classmethod
    def aumentar_producto(cls):
        cls.contador_productos += 1
        return cls.contador_productos

    def __init__(self, nombre: str, precio: float) -> None:
        self._id_producto = Producto.aumentar_producto()
        self._nombre: str = nombre
        self._precio: float = precio

    def __str__(self) -> str:
        return f"Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}"

    @property
    def precio(self):
        return self._precio


class Orden:
    contador_ordenes = 0
    @classmethod
    def aumentar_producto(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, productos) -> None:
        self._id_orden = Orden.aumentar_producto()
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self) -> str:
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + "\n"
        return f"Orden: {self._id_orden} \n{productos_str}"


producto1 = Producto("Camisa", 100.00)
producto2 = Producto("Pantalon", 200.00)
productos1 = [producto1, producto2]
orden1 = Orden(productos1)
print(orden1)
orden2 = Orden(productos1)
print(orden2)
print(f"Total: {orden2.calcular_total()}")