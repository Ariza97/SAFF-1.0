import threading
from rrd1 import archivoRrd
from rrd2 import realizarConsultas
from rrd3 import crearGraficas
from trendLineal import archivoProcesador
from TrendUpdate import monitoreaProcesador
from TrendGraph import crearGrafica
import subprocess

class Agente:
	def __init__(self, ip, nombre, comunidad, estado, version, puerto): 
		self.ip =ip
		self.nombre =nombre
		self.comunidad =comunidad
		self.estado =estado
		self.interfacesactivas =-1
		self.version =version
		self.puerto =puerto

	def getIp(self):
		return self.ip
	def setIp(self, ip):
		self.ip =ip

	def getNombre(self):
		return self.nombre

	def setNombre(self, nombre):
		self.nombre =nombre

	def getComunidad(self):
		return self.comunidad
	def setComunidad(self, comunidad):
		self.comunidad =comunidad

	def getEstado(self):
		return self.estado
	def setEstado(self, estado):
		self.estado =estado

	def getInterfacesactivas(self):
		return self.interfacesactivas
	def setInterfacesactivas(self, interfacesactivas):
		self.interfacesactivas =interfacesactivas

	def getVersion(self):
		return self.version

	def setInterfaces(self, interfacesactivas):
		self.version = interfacesactivas

	def getPuerto(self):
		return self.puerto
	def setPuerto(self, puerto):
		self.puerto =puerto

	#Generar gráficas de 5 datos de la MIB
	def monitorear(self, numero):
		archivoRrd(numero)
		t1 = threading.Thread(target = realizarConsultas, args = (self.comunidad, self.ip, self.puerto, numero))
		t2 = threading.Thread(target = crearGraficas, args = [numero])
		t1.start()
		t2.start()

	#Consultar actividad en nucleos del procesador
	def infoProcesadores(self, numero):

		versionEnString = ""

		if self.version == 1 :
			versionEnString = "-v1"
		else:
			versionEnString = "-v2c"

		print("Comunidad: " + self.comunidad + " VersionString: " + versionEnString)

		# obtener resultado de snmpwalk
		datos = subprocess.check_output('snmpwalk ' + versionEnString +' -c' + self.comunidad + ' ' + self.ip + ' 1.3.6.1.2.1.25.3.3.1.2', shell = True)
		cadena = str(datos)

		#Convertirlos a un array
		arreglo = cadena.split()
		procesadores = []
		hilos = []

        # Agregar a arreglo los procesadores en la MIB
		for i in range (0,len(arreglo)):
		    #Si hay un oid de procesador
		    if arreglo[i] == "=":
		        temp = arreglo[i-1].split(".")
		        procesadores.append(temp[-1])

		for i in range(0,len(procesadores)):
			archivoProcesador(numero, procesadores[i])
			t1 = threading.Thread(target = monitoreaProcesador, args = (self.comunidad, self.ip, self.puerto, numero, procesadores[i]))
			t2 = threading.Thread(target = crearGrafica, args = (numero, procesadores[i]))
			hilos.append(t1)
			hilos.append(t2)
			#t1.start()
			#t2.start()

		for i in range(0,len(hilos)):
			hilos[i].start()