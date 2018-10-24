import sys
import rrdtool
import time
from Notify import send_alert_attached

def crearGrafica(numero, id):

    #print(str(numero))
    archivoRrd = 'trend' + str(numero) + '-' + str(id) + '.rrd'
    archivoPng = 'trend' + str(numero) + '-' + str(id) + '.png'
    
    ultima_lectura = int(rrdtool.last(archivoRrd))
    timepo_final = ultima_lectura
    tiempo_inicial = timepo_final - 3600

    while 1:
        ret = rrdtool.graphv( archivoPng,
                         "--start",str(tiempo_inicial), #Modifcar para tiempo incial
                         #"--end",str(tiempo_final),
                         #"--vertical-label=Carga CPU",
                         "--title=Uso de CPU",
                         "--color", "ARROW#009900",
                         '--vertical-label', "Uso de CPU (%)",
                         '--lower-limit', '0',
                         '--upper-limit', '100',
                         "DEF:carga=" + archivoRrd + ":CPUload:AVERAGE",
                         "CDEF:carga60=carga,60,GT,0,carga,IF",
                         
                         #"LINE1:30",
                         #"AREA:5#ff000022:stack",

                         #"VDEF:CPUlast=carga,LAST",
                         "VDEF:CPUmin=carga,MINIMUM",
                         #"VDEF:CPUavg=carga,AVERAGE",
                         "VDEF:cargaSTDEV=carga,STDEV",
                         "VDEF:cargaLAST=carga,LAST",
                         "VDEF:CPUmax=carga,MAXIMUM",
                         "AREA:carga#00FF00:CPU load",
                         "AREA:carga60#FF9F00:Carga menor al 60%",
                         "HRULE:60#FF0000:Umbral 1",
                         #    "COMMENT:                         Now          Min             Avg             Max//n",
                         #"GPRINT:CPUlast:%12.0lf%s",
                         #"GPRINT:CPUmin:%10.0lf%s",
                         #"GPRINT:CPUavg:%13.0lf%s",
                         #"GPRINT:CPUmax:%13.0lf%s"
                         "GPRINT:CPUmax:%6.2lf %SMAX",
                         "GPRINT:CPUmin:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "PRINT:cargaLAST:%6.2lf%S"
                         #"VDEF:a=carga,LSLSLOPE", 
                         #"VDEF:b=carga,LSLINT",
                         #'CDEF:avg2=carga,POP,a,COUNT,*,b,+',
                         #"LINE2:avg2#FFBB00" )
                         )
        print (ret)
        print(ret.keys())
        print(ret.items())

        ultimo_valor=float(ret['print[0]'])
        #print ("ultimo_valor = " + str(ultimo_valor))
        if ultimo_valor>60:
            send_alert_attached("Carga alta de nucleo: " + id, archivoPng)

        """for x in range(0,7):
            res= 'legend['+str(x)+']'
            print(ret[res])"""

        time.sleep(15)
