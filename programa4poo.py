'''Realizar un programa que tenga una clase Persona con las siguientes
características. Implementar los métodos necesarios para inicializar los
atributos, mostrar los datos e indicar si la persona es mayor de edad o no'''
class Persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
#setter se utiliza para introducir datos
    def setNombre(self):   
        self.nombre=nombre
    
    def setEdad(self):
        self.edad=edad
    
#getter se utiliza para obtener datos
    def getNombre(self):   
        return self.nombre
    
    def getEdad(self):
        return self.edad
    
#__str__ metodo para convertir al objeto a cadena
    def __str__(self):         
        return str(self.nombre)

#imprimir define si es adulto o no
    def imprimir(self):
        if self.edad>=20:
            print ('el sr/a %s cuya edad  es %s es mayor de edad'% (self.nombre, self.edad))
        else:        
            print ('el sr/a %s cuya edad  es %s es no mayor de edad'% (self.nombre, self.edad))

per=Persona(nombre=input('ingrese nombre: '),edad=int(input('ingrese edad: ')))
per.imprimir()

