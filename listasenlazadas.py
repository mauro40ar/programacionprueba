class Nodo():
    def __init__(self,dato,sgt):
        self.dato=dato
        self.sgt=sgt
    def __str__(self):
        return str(self.dato)
    def lista(nodo):
        ''' Recorre todos los nodos a traves de sus enlaces,
        mostrando sus contenidos.'''
        #Cicla mientras nodo no es None
        while nodo:
            print (nodo) # muestra el dato
            nodo=nodo.sgt # ahora nodo apunta a nodo.sgt
            
v1=Nodo(12,v2)
v2=Nodo(44,v3)
v3=Nodo(33,v4)
v4=Nodo(66,v5)

lista(v1)
lista(v2)
lista(v3)

