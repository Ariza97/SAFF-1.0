import time
import rrdtool
from getSNMP import consultaSNMP

def actualizarBase(nombrebase, comunidad, nombrehost):
    OIDparaRAM = "1.3.6.1.4.1.2021.4.6.0"

    #Consultar carga de un procesador
    carga_CPU = 0
    print(OIDparaRAM)
    while 1:
        carga_CPU = int(
            consultaSNMP(comunidad, nombrehost, #COMUNIDAD , hostname
                     OIDparaRAM)) #Nodo de la MIB a consultar, el ID del procesador cambiará

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
