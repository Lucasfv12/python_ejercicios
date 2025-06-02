class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f"el estudiante {self.nombre} está estudiando")
    
class Docente(Estudiante):
    def __init__(self, nombre, edad, grado, trabajo, sueldo):
        super().__init__(nombre, edad, grado)
        self.trabajo = trabajo
        self.sueldo = sueldo
        
        
    
        
        
Estudiante1 = Estudiante("Lucas", 12, "6to")

Estudiante1.estudiar()




