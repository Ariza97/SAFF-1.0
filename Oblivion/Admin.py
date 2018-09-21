from pysnmp.hlapi import *
from Agente import Agente
import listaagentes

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


    #Dar de baja agente (retorna booleano)
    def eliminarDeHost(self, nombre):
        #eliminar agente de array
        print('Eliminado')

"""
a1 = Admin('stefan', '1234')
print(a1.getUser())
print(a1.getPassword())
a1.agregarAHost('a1', 'stefan10')
a1.eliminarDeHost('nombre')

"""
