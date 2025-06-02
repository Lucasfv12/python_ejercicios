# Clase Cliente
class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.compras = []

    def agregar_compra(self, producto, monto):
        self.compras.append()