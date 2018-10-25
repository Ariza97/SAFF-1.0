import sys
import rrdtool
import time
from Notify import send_alert_attached

def grafica(base):

    nombreBase =base + ".rrd"
    nombreResultado = base + ".png"
    ultima_lectura = int(rrdtool.last(nombreBase))
    tiempo_final = ultima_lectura
    tiempo_inicial = tiempo_final - 1800

    while 1:
        ret = rrdtool.graphv( nombreResultado,
                         "--start",str(tiempo_inicial),
                         "--vertical-label=Carga CPU",
                         "--title=Uso de RAM",
                         "--color", "ARROW#009900",
                         '--vertical-label', "Uso de RAM (M)",
                         '--lower-limit', '0',
                         '--upper-limit', '100',
                         "DEF:carga=" + nombreBase + ":CPUload:AVERAGE",
                         "DEF:carga2=" + nombreBase + ":CPUload:AVERAGE",


                         "LINE1:50",
                         "AREA:5#ff000022:stack",
                         "VDEF:CPUlast=carga,LAST",
                         "VDEF:CPUmin=carga,MINIMUM",
                         "VDEF:CPUavg=carga,AVERAGE",
                         "VDEF:CPUmax=carga,MAXIMUM",

                             "COMMENT:                         Now          Min             Avg             Max//n",
                         "GPRINT:CPUlast:%12.0lf%s",
                         "GPRINT:CPUmin:%10.0lf%s",
                         "GPRINT:CPUavg:%13.0lf%s",
                         "GPRINT:CPUmax:%13.0lf%s",
                         "VDEF:a=carga,LSLSLOPE",
                         "VDEF:b=carga,LSLINT",
                         'CDEF:avg2=carga,POP,a,COUNT,*,b,+',
                         'CDEF:avg3=carga2,POP,a,COUNT,*,b,+',

                         "LINE3:3000000#000000",
                         "LINE3:6000000#00BB00",
                         "LINE3:10000000#BB0000",

                         "LINE2:avg2#FFBB00",
                         "AREA:carga#00FF00:CPU load",
                         "PRINT:carga:LAST:%6.1lf"
                         )
        print(ret['print[0]'])
        a=float(ret['print[0]'])
        if (a>float(10000000)):
            send_alert_attached("Alerta de Sobre Carga de RAM")
     #  else:
       #     send_alert_attached("Vas bien papu")

        time.sleep(15)