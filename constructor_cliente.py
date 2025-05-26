# Clase Cliente
class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.compras = []

    def agregar_compra(self, producto, monto):
        self.compras.append({"producto": producto, "monto": monto})

    def total_gastado(self):
        return sum(compra["monto"] for compra in self.compras)

    def info(self):
        print(f"Cliente: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")
        print(f"Total gastado: ${self.total_gastado()}")
        
# Crear algunos clientes
cliente1 = Cliente("María López", "maria@gmail.com", "123456789")
cliente2 = Cliente("Juan Pérez", "juan@gmail.com", "987654321")

# Agregar compras
cliente1.agregar_compra("Notebook", 1200)
cliente1.agregar_compra("Mouse", 25)

cliente2.agregar_compra("Monitor", 300)

# Mostrar info
cliente1.info()
print("------")
cliente2.info()

