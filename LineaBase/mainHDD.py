import subprocess
import threading
import sys
from trendLineal import crearBase
from HDDUpdate import actualizarBase
from HDDGraph import grafica

comunidad  = "comunidadEquipo8_grupo4cm3"
nombrehost = "linux"
version ="-v2c"
puerto ="161"

consulta = subprocess.check_output(
    'snmpwalk ' + version + ' ' + '-c' + comunidad + ' ' + nombrehost + ' ' + '1.3.6.1.2.1.25.2.3.1.6', shell=True)
#Convertimos el dato consulta a una cadena
cadena = str(consulta)
#Convertimos el dato cadena a un array
arreglo = cadena.split()

particiones = []
#Obtenemos el numero de cada procesador
for i in range (0,len(arreglo)):
#Si hay un oid de procesador
    if arreglo[i] == "=":
        temp = arreglo[i-1].split(".")
        particiones.append(temp[-1])
print("Numero de Particion: " + str(len(particiones)))


#Ahora que tenemos los numero de los particiones vamor a crear las bases para cada unidad
for i in range(0, len(particiones)):
    nombrebase =nombrehost+"_ParticionNum_"+particiones[i]+".rrd"
    respuesta =crearBase(nombrebase)
    if respuesta == False:
        print('Error al crear la base: '+nombrebase)
        sys.exit()
    else:
        print("Se creo exitosamente Base: "+nombrebase)

#Ahora actualizaremos el contenido de las bases, de una manera constante
#Crearemos hilos
hilosActualizarDatos = []
hilosgrafico = []
for i in range(0, len(particiones)):
    nombrebase =nombrehost+"_ParticionNum_"+particiones[i]
    t1 = threading.Thread(target = actualizarBase, args=(nombrebase, particiones[i],comunidad,nombrehost))
    hilosActualizarDatos.append(t1)
    t2 = threading.Thread(target = grafica, args=(nombrebase, ))
    hilosgrafico.append(t2)

for i in range(0, len(hilosActualizarDatos)):
    hilosActualizarDatos[i].start()

for j in range(0, len(hilosgrafico)):
    hilosgrafico[j].start()