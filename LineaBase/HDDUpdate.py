import time
import rrdtool
from getSNMP import consultaSNMP

def actualizarBase(nombrebase, numParticion, comunidad, nombrehost):
    OIDparaParticion = "1.3.6.1.2.1.25.2.3.1.6"

    #Consultar carga de un procesador
    carga_CPU = 0
    OIDParticion =OIDparaParticion + "." +numParticion
    print(OIDParticion)
    while 1:
        carga_CPU = int(
            consultaSNMP(comunidad, nombrehost, #COMUNIDAD , hostname
                     OIDParticion)) #Nodo de la MIB a consultar, el ID del procesador cambiará

        valor = "N:" + str(carga_CPU)
        print (valor)
        baseRRD = nombrebase + ".rrd"
        baseXML = nombrebase + ".xml"
        rrdtool.update(baseRRD, valor)
        rrdtool.dump(baseRRD, baseXML)
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)
