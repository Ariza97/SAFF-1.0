import rrdtool
def crearBase(nombre_de_la_base):
    ret = rrdtool.create(nombre_de_la_base,
                     "--start",'N-3600', #Tomara la hora actual del sistema
                     "--step",'30', #cada 30 segundos
                     "DS:CPUload:GAUGE:600:U:U", #Se almacenar{a en CPULoad
                     "RRA:AVERAGE:0.5:1:24") #solo tendrá un archivo RRA que ocuapra un AVERAGE, tomará cada 0-5 muestras y obtendrá un promedio
    return True

    if ret:
        print (rrdtool.error())
        return False