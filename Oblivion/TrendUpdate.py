import time
import rrdtool
from getSNMP import consultaSNMP

def monitoreaProcesador(comunidad, ip, puerto, numero, id):

    archivoRrd = 'trend' + str(numero) + '-' + str(id) + '.rrd'
    archivoXml = 'trend' + str(numero) + '-' + str(id) + '.xml'
    oid = '1.3.6.1.2.1.25.3.3.1.2.' + str(id)

    carga_CPU = 0

    while 1:
        carga_CPU = int(
            consultaSNMP(comunidad,ip,
                         oid, puerto)) #Información de procesos, sirve para linux, cambiar para otros sistemas
        
        valor = "N:" + str(carga_CPU) #Hora del sistema más dato MIB obtenido
        print (valor)
        rrdtool.update(archivoRrd, valor)
        rrdtool.dump(archivoRrd,archivoXml)
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)
