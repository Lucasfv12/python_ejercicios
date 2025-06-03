class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} estoy hablando")
        
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
    
    def dejar_de_hablar(self):
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} mi nacionalidad es {self.nacionalidad}, soy {self.trabajo} y cobro {self.salario}")
        

empleado1 = Empleado("Lucas", 34, "Argentino", "Desarrollador", 10000)

empleado1.dejar_de_hablar()

