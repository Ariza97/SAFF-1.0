import time
from getSNMP import consultaSNMP, estatusDeConexion


#consulta =consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.2.2.1.6.3','161')



""" Estatus de la conexion de cada dispositivo
    Esta funcion devuelve un true si encuentra el equipo, caso contrario un false"""
consulta =estatusDeConexion('comunidadASR','localhost','1.3.6.1.2.1.2.2.1.6.3','161')
print ("Estatus de conexion: ",consulta)


""" Estatus de la conexion de cada dispositivo
    Esta funcion devuelve un true si encuentra el equipo, caso contrario un false"""
##consulta =consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.1.1.0','161')
##print ("Estatus de conexion: ",consulta)


