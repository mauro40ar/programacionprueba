class Calculadora():
    def __init__(self,para1,para2):
        self.para1=para1
        self.para2=para2
    def suma(self):
        print (self.para1 + self.para2)
    def resta(self):
        print (self.para1-self.para2)
    def multiplicacion(self):
        print (self.para1*self.para2)
    def division(self):
        print (self.para1/self.para2)
c1=Calculadora(int(input('ingrese valor numerico: ')),int(input('ingrese valor numerico: ')))
c1.suma()
c1.resta()
c1.multiplicacion()
c1.division()

