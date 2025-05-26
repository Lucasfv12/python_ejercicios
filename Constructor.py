class Auto():
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca
        
    def arrancar(self):
        print("El auto está encendido")
        
mi_auto = Auto("rojo", "Toyota")

print(f"Yo tengo un auto color {mi_auto.color} de la marca {mi_auto.marca}")



