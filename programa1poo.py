class Persona():
    def __init__(self,nombre):
        self.nombre=nombre
    def imprimir(self):
        print ('hola sr %s' % self.nombre)
p1=Persona(input('ingrese nombre completo: '))
p1.imprimir()
