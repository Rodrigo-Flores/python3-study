"""
class Persona:
        self.nombre = input_nombre
        self.edad = input_edad

    def edad(self, input_edad):
        self.edad = input_edad

    def nombre(self, input_nombre):
        def __init__(self, input_nombre, input_edad):
        self.nombre = input_nombre

def saludo(sujeto):
    mensaje = "Hola, " + sujeto
    print(mensaje)

persona1 = Persona("Rodrigo", 18)
persona2 = Persona("José" , 18)

saludo(persona1.nombre)
saludo(persona2.nombre)
"""

class Calculadora:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self,num1,num2):
        self.sum = num1+num2

    def resta(self,num1,num2):
        self.res = num1-num2

    def multiplicacion(self,num1,num2):
        self.mul = num1*num2

    def division(self,num1,num2):
        self.div = num1/num2

resultado = Calculadora(1,1)
print(resultado.suma
