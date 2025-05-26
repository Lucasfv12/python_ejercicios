class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def saludar(self):
        print(f"Hola, {self.nombre}. Gracias por registrarte con el email {self.email}.")


# Pedimos datos al usuario
nombre_usuario = input("Ingresá tu nombre: ")
email_usuario = input("Ingresá tu email: ")
telefono_usuario = input("Ingrese su número de telefono")

# Creamos el cliente con los datos ingresados
cliente = Cliente(nombre_usuario, email_usuario, telefono_usuario)

# Usamos el método
cliente.saludar()