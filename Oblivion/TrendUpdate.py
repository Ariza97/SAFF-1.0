import time
import rrdtool
from getSNMP import consultaSNMP

def monitoreaProcesador(comunidad, ip, puerto, numero):

    archivoRrd = 'trend' + str(numero) + '.rrd'
    archivoXml = 'trend' + str(numero) + '.xml'

    carga_CPU = 0

    while 1:
        carga_CPU = int(
            consultaSNMP(comunidad,ip,
                         '1.3.6.1.2.1.25.3.3.1.2.196608', puerto)) #Información de procesos, sirve para linux, cambiar para otros sistemas
        # cambiar aquí dependiendo el número de procesadores que tiene el agente

        valor = "N:" + str(carga_CPU) #Hora del sistema más dato MIB obtenido
        print (valor)
        rrdtool.update(archivoRrd, valor)
        rrdtool.dump(archivoRrd,archivoXml)
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)
