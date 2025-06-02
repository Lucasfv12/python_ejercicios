import random

class Dados():
    
    def tirar(self):
        self.valor = random.randint(1,6)
        
    def imprimir(self):
        print("El dado salió: ", self.valor)
    
    def retornar_valor(self):
        return self.valor
    
class JuegoDeDados():
    def __init__(self):
        self.dado1 = Dados()
        self.dado2 = Dados()
        self.dado3 = Dados()
        
    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        
        v1 = self.dado1.retornar_valor()
        v2 = self.dado2.retornar_valor()
        v3 = self.dado3.retornar_valor()
    
        if v1 == v2 == v3:
            print("🎉 ¡Ganaste! Los tres dados salieron iguales.")
        else:
            print("❌ Perdiste. Los dados no son todos iguales.")
            

juego = JuegoDeDados()
juego.jugar()