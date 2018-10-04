import sys
import os
import subprocess
from pysnmp.hlapi import *
from Admin import Admin
import listaagentes
from Agente import Agente

def main():

    #Crear un administrador con contrasenia
    administrador = Admin('root', 'root')

    #Agregar un agente
    if administrador.agregarAHostIP("localhost", "Stefan", "Stefan10", 1, 2, 161):
        print("Se agrego el agente 192.168.0.12")


    #Monitorear 
    administrador.obtenerEstadoDispositivo("Stefan", "Stefan10", 1, 1, 161, "localhost" )

main()