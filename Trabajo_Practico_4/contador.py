'''En este ejercicio deberás crear un script llamado contador.py que realice varias
tareas sobre un fichero llamado contador.txt que almacenará un contador de visitas
(será un número):
 Nuestro script trabajará sobre el fichero contador.txt. Si el fichero no existe o
está vacío lo crearemos con el número 0. Si existe simplemente leeremos el valor
del contador.
 Luego a partir de un argumento:
 Si se envía el argumento inc, se incrementará el contador en uno y se
mostrará por pantalla.
 Si se envía el argumento dec, se decrementará el contador en uno y se
mostrará por pantalla.
Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará
el valor del contador por pantalla.
Finalmente guardará de nuevo el valor del contador de nuevo en el fichero.



Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: Error:
Fichero corrupto.'''
from io import open
import sys

archivo=open('contador.txt','a+')
archivo.seek(0)
informacion=archivo.readline()
if len(informacion)==0:
    informacion='0'
    archivo.write(informacion)
archivo.close()
try:
    contador = int(informacion)
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1
    print(contador)

    fichero = open("contador.txt", "w")
    fichero.write( str(contador) )
    fichero.close()
except:
    print ('Error: el fichero esta corrupto')

