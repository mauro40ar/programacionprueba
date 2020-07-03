'''Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?'''
cadena = "zeréP nauJ,01"
x=cadena[::-1]

print('el alumno %s saco de nota %s'%(x[3:],x[:2]))


