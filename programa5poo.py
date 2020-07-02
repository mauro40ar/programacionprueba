'''Realizar una clase que administre una agenda. Se debe almacenar para cada
contacto el nombre, el teléfono y el email. Además deberá mostrar un menú
con las siguientes opciones
a Añadir ontacto.
b Lista de contactos
c Buscar contacto
d Editar contacto
e Cerrar agenda '''

class Agenda():
    #constructor
    def __init__ (self,contacto):
        self.contacto=[]

    #menu
    def menu(self):
        print ()
        menu=[
                ['1- agregarcontacto'],
                ['2- listacontacto']
                ]
        for i in range (2):
            print (menu[i][0])
        opcion=int(input('ingrese opcion: '))
        if opcion == 1:
            self.agregarcontacto()
        elif opcion==2:
            self.listacontacto()



                

    #agregar contactos en la agenda
    def agregarcontactos(self):
        nombre=input('ingrese nombre: ')
        telefono=int(input('ingrese telefono: '))
        email=input('ingrese email: ')
        contacto.append({'nombre':nombre,'telefono':telefono,'email':email})


    #muestra una lista de contacto
    def listacontacto(self):
        if len(self.contacto)==0:
            print ('la lista esta vacia')
        else:
            for i in range(len(self.contacto)):
                print (self.contacto[i]['nombre'])




agen=Agenda()
agen.menu()
