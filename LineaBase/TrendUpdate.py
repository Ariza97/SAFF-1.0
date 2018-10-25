import time
import rrdtool
from getSNMP import consultaSNMP

def actualizarBase(nombrebase, numprocesador, comunidad, nombrehost):
    OIDparaProcesador = "1.3.6.1.2.1.25.3.3.1.2"

    #Consultar carga de un procesador
    carga_CPU = 0
    OIDNucleo =OIDparaProcesador + "." +numprocesador
    print(OIDNucleo)
    while 1:
        carga_CPU = int(
            consultaSNMP(comunidad, nombrehost, #COMUNIDAD , hostname
                     OIDNucleo)) #Nodo de la MIB a consultar, el ID del procesador cambiará

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
