'''Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

    Si los dos números son iguales
    Si los dos números son diferentes
    Si el primero es mayor que el segundo
    Si el segundo es mayor o igual que el primero
'''
a=int(input('ingrese valor entero: '))
b=int(input('ingrese valor entero: '))

print ('¿son iguales', a==b)
print('¿son distinto?', a != b)
print('¿el primero es ayor?', a>b) 
print('el segundo es mayor o igual al primero', a<=b)

