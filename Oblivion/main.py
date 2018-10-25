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

    #Mostrar datos de página de Inicio
    #administrador.infoInicio()
    #Agregar un agente
    """if administrador.agregarAHostIP("localhost", "Stefan", "Stefan10", 1, 2, 161):
        print("Se agrego el agente 192.168.0.12")
    else:
        print("No se agrego el agente error")"""
    
    print(administrador.cargarAgentesGuardados())

    #if administrador.agregarAHostIP("192.168.0.12", "Stefan Windows", "Stefan", 1, 2, 161):
    #    print("Se agrego el agente 192.168.0.12")

    #Mostrar datos de página de Inicio
    #administrador.infoInicio()

    #Monitorear 
    # administrador.obtenerEstadoDispositivo("Stefan", "Stefan10", 1, 1, 161, "localhost" )

    # administrador.obtenerEstadoDispositivo("Stefan Windows", "Stefan", 1, 1, 161, "192.168.0.12" )

    #Monitorear todos los agentes
    #administrador.monitorearAgentes()

    #Monitorear los procesadores de cada agente
    #administrador.predecirProcesadores()

main()