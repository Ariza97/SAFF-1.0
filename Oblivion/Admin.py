import threading
from pysnmp.hlapi import *
from Agente import Agente
import listaagentes
import subprocess

class Admin:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        #self.agentes = []

    #Getters
    def getUser(self):
        return self.user

    def getPassword(self):
        return self.password

    #Setters
    def setUser(self, user):
        self.user = user

    def setPassword(self, password):
        self.password = password

    #Dar de alta Agente (retorna booleano)
    def agregarAHostIP(self, ip, nombre, comunidad, estado, version, puerto):

        #Verificar Version
        versionString = ""

        if version == 1:
            versionString = "SNMPv1-MIB"
        elif version == 2:
            versionString = "SNMPv2-MIB"
        else:
            versionString = "SNMPv3-MIB"

        #Verificar si el elemento es valido en la red
        errorIndication, errorStatus, errorIndex, varBinds = next(
                getCmd(SnmpEngine(),
                    CommunityData(comunidad),
                    UdpTransportTarget((ip, puerto)),
                    ContextData(),
                    ObjectType(ObjectIdentity(versionString, 'sysDescr', 0))))

        if errorIndication:
            return False
        elif errorStatus:
            return False

        #Agregar el elemento a host
        archivo = archivo = open('/etc/hosts', 'r')

        contenido = archivo.readlines()

        #Activar bandera de escritura
        puedeEscribir = True
        cadenaCopia = ""

        for cadena in contenido:
            if cadena.find('::') != -1: #Si si encuentra la cadena
                if puedeEscribir:
                    cadenaCopia += ip + "\t" + nombre + "\n"
                    puedeEscribir = False
                    cadenaCopia += cadena
                else:
                    cadenaCopia += cadena
            else:
                cadenaCopia += cadena


        #Sobreescribir el archivo en hosts
        archivo.close()
        archivo = open('/etc/hosts', 'w')
        archivo.write(cadenaCopia)
        archivo.close()

        #Agregar el agente
        nuevoAgente = Agente(ip, nombre, comunidad, estado, version, puerto)
        listaagentes.listaAgentes.append(nuevoAgente)

        return True
    #Dar de alta Agente (retorna booleano)
    def agregarAHost(self, nombre, comunidad, estado, version, puerto):
        #Verificar Version
        versionString = ""

        if version == 1:
            versionString = "SNMPv1-MIB"
        elif version == 2:
            versionString = "SNMPv2-MIB"
        else:
            versionString = "SNMPv3-MIB"

        archivo = open('/etc/hosts', 'r')
        lineasDeHost = archivo.readlines()
        lineasDeHost = [line.strip() for line in lineasDeHost
                            if not line.startswith('#') and line.strip() != '']

        arregloHost = []
        for linea in lineasDeHost:
            nombreC = linea.split('#')[0].split()[1:]
            arregloHost.extend(nombreC)

        #Crear un diccionario para almacenar
        diccionarioHosts = {}

        for i in lineasDeHost:
            if "::" not in i:
                a = i.split("\t")
                diccionarioHosts[a[1]] = a[0]
        

        #Una vez procesado el documento host se busca en diccionarioHosts
        for cad in diccionarioHosts:
            if cad == nombre:
                break   #Si se encuentra entonces puede agregarse al gestor


        #Comprobar la conexion
        errorIndication, errorStatus, errorIndex, varBinds = next(
                getCmd(SnmpEngine(),
                    CommunityData(comunidad),
                    UdpTransportTarget( (diccionarioHosts[nombre], puerto)),
                    ContextData(),
                    ObjectType(ObjectIdentity(versionString, 'sysDescr', 0))))

        if errorIndication:
            return False
        elif errorStatus:
            return False


        #Agregar el agente
        nuevoAgente = Agente(self, diccionarioHosts[nombre], nombre, comunidad, estado, version, puerto)
        listaagentes.listaAgentes.append(nuevoAgente)
        
        return True

    def obtenerEstadoDispositivo(self, nombre, comunidad, estado, version, puerto, ip):
        
        versionEnString = ""

        if version == 1 :
            versionEnString = "-v1"
        else:
            versionEnString = "-v2c"

        print("Comunidad: " + comunidad + " VersionString: " + versionEnString)

        datos = subprocess.check_output('snmpstatus ' + versionEnString +' -c' + comunidad + ' ' + ip + ' ', shell = True)
        cadena = str(datos)

        #Convertirlos a un array
        arreglo = cadena.split()

        #Obtener el numero de interfaces activas
        totalInterfaces = 0

        for i in range (0,len(arreglo)):

            #Mostrar el tiempo activo
            if arreglo[i] == "Up:":
                print("Tiempo activo: " + arreglo[i+1] + " " + arreglo[i+2])


            if "Interfaces" in arreglo[i]:
                totalInterfaces = int(arreglo[i+1][:1])

            #Obtener el numero total de interfaces
            elif i+1 != len(arreglo):
                if "interfaces" in arreglo[i+1]:
                    totalInterfaces -= int(arreglo[i][-1:])
                    print("Interfaces activas: " + str(totalInterfaces))
            
        #Obtener la localizacion fisica
        arrayDir = listaagentes.consultaSNMP(comunidad, ip, "1.3.6.1.2.1.1.6.0", puerto).split(' ')
        print("La localizacion fisica es: " + arrayDir[len(arrayDir) - 1])

        #Obtener la informacion de contacto
        arrayContactInfo = listaagentes.consultaSNMP(comunidad, ip, "1.3.6.1.2.1.1.4.0", puerto).split(' ')
        print("La localizacion fisica es: " + arrayContactInfo[len(arrayContactInfo) - 1])

        #listaagentes.listaAgentes[0].monitorear()

    #Dar de baja agente (retorna booleano)
    def eliminarDeHost(self, nombre):
        archivo = open('/etc/hosts', 'r')
        contenido = archivo.readlines()
        cadenaCopia = ""
        
        #Busca el nombre para eliminarlo
        for cadena in contenido:
            if cadena.find(nombre) == -1: #Cuando encuentre el nombre no lo copia
                cadenaCopia += cadena
        
        archivo.close()
        archivo = open('/etc/hosts', 'w')
        archivo.write(cadenaCopia)
        archivo.close()

        return True

    #Obtiene información de página de Inicio
    def infoInicio(self):

        numeroAgentes = len(listaagentes.listaAgentes)
        print("Dispositivos Monitorizados: " + str(numeroAgentes))

        #obtiene la información de cada agente monitoreado
        for i in range(0,len(listaagentes.listaAgentes)):
            nombre = listaagentes.listaAgentes[i].getNombre();
            print("Nombre: " + nombre)
            if listaagentes.listaAgentes[i].getEstado() == 1 :
                estatus = True
                print("Estatus: Up")
            else:
                estatus = False
                print("Estatus: Down")
            intActivas = listaagentes.listaAgentes[i].getInterfacesactivas()
            print("Interfaces Activas: " + str(intActivas))

    def monitorearAgentes(self):

        #arreglo de hilos
        hilos = []

        #Por cada agente se crea un hilo
        if len(listaagentes.listaAgentes) > 0 :
            for i in range(0, len(listaagentes.listaAgentes)):
                #x = i+1
                t1 = threading.Thread(target = listaagentes.listaAgentes[i].monitorear, args = [i+1])
                hilos.append(t1)

            #Se inician los hilos
            for j in range(0, len(hilos)):
                hilos[j].start()

"""
a1 = Admin('stefan', '1234')
print(a1.getUser())
print(a1.getPassword())
a1.agregarAHost('a1', 'stefan10')
a1.eliminarDeHost('nombre')

"""
