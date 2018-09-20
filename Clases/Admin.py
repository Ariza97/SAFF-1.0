#import Agente

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
    def agregarAHost(self, ip, nombre, comunidad):
        #Crear agente
        #Agregar agente a array
        print('Agregado')

    #Dar de alta Agente (retorna booleano)
    def agregarAHost(self, nombre, comunidad):
        #Crear agente
        #Agregar agente a array
        print('Agregado')

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
