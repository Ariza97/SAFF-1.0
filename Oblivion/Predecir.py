import sys
import rrdtool
import time
import datetime
#from datetime import datetime

def prediccion(base, fecha_inicio, fecha_final, hora_inicio, hora_final, variable, limite):

    #ultima_lectura = int(rrdtool.last(base))
    #print("Ultimo: " + str(ultima_lectura))
    
    #Convertir fecha_incio a timestamp
    iniciar = int(time.mktime(datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y").timetuple()))

    #Convertir hora_incio a timestamp
    formato = "%H:%M:%S"
    inicio = datetime.datetime.strptime(hora_inicio, formato)
    horas = inicio.hour
    minutos = inicio.minute
    segundos = inicio.second

    #Parametro de incio de monitoreo
    iniciar += (horas * 60 * 60) + (minutos * 60) + segundos
    print("Tiempo_inicio: " + str(iniciar))

    #Convertir fecha_final a timestamp
    final = int(time.mktime(datetime.datetime.strptime(fecha_final, "%d/%m/%Y").timetuple()))

    #Convertir hora_final a timestamp
    fin = datetime.datetime.strptime(hora_final, formato)
    horas = fin.hour
    minutos = fin.minute
    segundos = fin.second
    final += (horas * 60 * 60) + (minutos * 60) + segundos

    print(str(limite))

    ret = rrdtool.graph( "Pred" + variable + ".png",
                     "--start", str(iniciar), #Modifcar para tiempo incial
                     "--end", str(final),
                 "--vertical-label=" + variable,
                 "--title=" + variable,
                 "--color", "ARROW#009900",
                 '--vertical-label', variable,
                 '--lower-limit', '0',
                 #'--upper-limit', '100',
                 "DEF:carga=" + base + ":" + variable + ":AVERAGE",
                 "AREA:carga#00FF00:" + variable,


                 "HRULE:" + str(limite) + "#FF0000:Limite",
                 "AREA:5#ff000022:stack",
                 "VDEF:CPUlast=carga,LAST",
                 "VDEF:CPUmin=carga,MINIMUM",
                 "VDEF:CPUavg=carga,AVERAGE",
                 "VDEF:CPUmax=carga,MAXIMUM",
                 #"VDEF:predMAX=carga,LAST",
                 #"VDEF:predMIN=carga,LAST",
                 "COMMENT:                         Now          Min             Avg             Max//n",
                 "GPRINT:CPUlast:%12.0lf%s",
                 "GPRINT:CPUmin:%10.0lf%s",
                 "GPRINT:CPUavg:%13.0lf%s",
                 "GPRINT:CPUmax:%13.0lf%s",
                 "VDEF:a=carga,LSLSLOPE", 
                 "VDEF:b=carga,LSLINT",

                 'CDEF:avg2=carga,POP,a,COUNT,*,b,+',
                 "CDEF:predMAX=avg2,0," + str(limite) + ",LIMIT",
                 "VDEF:max=predMAX,MAXIMUM",
                 #"CDEF:predMIN=avg2,0," + str(limite) + ",LIMIT",
                 "VDEF:min=predMAX,MINIMUM",
                 #"PRINT:PRED",
                 "GPRINT:max:%c:strftime",
                 "GPRINT:min:%c:strftime",
                 "LINE2:avg2#FFBB00" )

    time.sleep(15)