class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

productos_disponibles = [
    Producto("Placa de video", 2000),
    Producto("Memoria RAM", 1500),
    Producto("Placa de red", 500),
    Producto("Monitor", 3000),
    Producto("Mouse", 150)
]

class Persona():
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        print(f"Hola {self.nombre}, de apellido {self.apellido} y DNI {self.dni}, ¿qué vas a llevar hoy?")

persona1 = Persona("Lucas", "Vergara", 35406133)

Carrito_persona_1 = []

print("\nEstos son los productos disponibles:\n")
for item in productos_disponibles:
    print(item)

eleccion = input("\nPodés elegir un producto para agregarlo a tu carrito: ")

producto_encontrado = None

for producto in productos_disponibles:
    if producto.nombre.lower() == eleccion.lower():
        producto_encontrado = producto
        break

if producto_encontrado:
    Carrito_persona_1.append(producto_encontrado)
    print(f"✅ El producto {producto} se ha agregado a tu carrito.")
else:
    print("❌ No tenemos ese producto en nuestro stock.")

# Mostrar el contenido del carrito
print("\n🛒 En tu carrito tenés:")
for item in Carrito_persona_1:
    print(item)




