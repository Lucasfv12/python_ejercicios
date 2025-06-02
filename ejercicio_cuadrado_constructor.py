#Desarrollar una clase que represente un punto en el plano y tenga los siguientes metodos: inicializar los valores
#de x e y, y que lleguen como parametros. Imprimir en que cuadrante se encuentra dicho punto (concepto matemático
# primer cuadrante si x e y son positivos, si x<0 e y>0 segunda cuadrante, etc)

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("Pertenece al primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print("Pertenece al segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print("Pertenece al tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            print("Pertenece al cuarto cuadrante")
        else:
            print("Estás en el EJE")

punto1=Punto(-4,-2)
punto1.cuadrante()
        
