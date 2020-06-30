''' Declarar una segunda clase llama Empleado que hereda de la clase Persona y
agrega el atributo sueldo. Debe mostrar si tiene que pagar impuestos o no
(sueldo superior a 3000). Crear un objeto de cada clase '''

class Persona():
    def __init__(self, nombre):
        self.nombre=nombre
    def setNombre(self):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    def imprimir(self):
        print(self.nombre)

class Empleado(Persona):
    def __init__(self,nombre,sueldo):        
        super().__init__(nombre)
        self.sueldo=sueldo
    def setSueldo(self):
        self.suedo=Sueldo 
    def getSueldo(self):
        return self.sueldo
    def __str__(self):
        return str(self.sueldo)
    def imprimir(self):
        if self.sueldo<'3000':
            print('el empleado %s cobra %s que es superior a los 3000 asi que paga impuesto'%(self.nombre,self.sueldo))
        else:
            print('no paga impuesto')
        

per=Persona(input('ingrese nombre: '))
per.imprimir()
emp=Empleado(per,input('ingrese monto : '))
emp.imprimir()
