import threading

from trendLineal import crearBase
from RAMUpdate import actualizarBase
from RAMGraph import grafica

comunidad  = "comunidadEquipo8_grupo4cm3"
nombrehost = "linux"
version ="-v2c"
puerto ="161"

#Crear Base para almacenar datos de RAM
nombrebase = nombrehost + "_RAM"
respuesta = crearBase(nombrebase+".rrd")

hilos = []

#Agregamos al Hilo la actualizacion de la base
t1 = threading.Thread(target = actualizarBase, args=(nombrebase, comunidad, nombrehost))
hilos.append(t1)
#Agregamos al hilo el proceso de Graficacion
t2 = threading.Thread(target = grafica, args=(nombrebase, ))
hilos.append(t2)

for  i in range(0, len(hilos)):
    hilos[i].start()