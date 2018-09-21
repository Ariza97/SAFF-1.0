import threading
from rrd1 import archivoRrd
from rrd2 import realizarConsultas
from rrd3 import crearGraficas

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
		self.ip =ip;

	def getNombre(self):
		return self.nombre
	def setIp(self, nombre):
		self.nombre =nombre;

	def getComunidad(self):
		return self.comunidad
	def setComunidad(self, comunidad):
		self.comunidad =comunidad;

	def getEstado(self):
		return self.estado
	def setEstado(self, estado):
		self.estado =estado;

	def getInterfacesactivas(self):
		return self.interfacesactivas
	def setInterfacesactivas(self, interfacesactivas):
		self.interfacesactivas =interfacesactivas;

	def getVersion(self):
		return self.version
	def setVersions(self, interfacesactivas):
		self.version =version;

	def getPuerto(self):
		return self.puerto
	def setPuerto(self, puerto):
		self.puerto =puerto;

	def monitorear(self):
		archivoRrd()
		t1 = threading.Thread(target = realizarConsultas, args = (self.comunidad, self.ip, self.puerto))
		t2 = threading.Thread(target = crearGraficas)
		t1.start()
		print('inicia')
		t2.start()





Salomon =Agente('localhost', 'Salomon', 'Stefan10', True, 1, 161)

print (Salomon.getIp())
print (Salomon.getNombre())
print (Salomon.getComunidad())
print (Salomon.getEstado())
print (Salomon.getInterfacesactivas())
print (Salomon.getVersion())
print (Salomon.getPuerto())

Salomon.monitorear()
