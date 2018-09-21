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
    if administrador.agregarAHostIP("192.168.43.212", "Dehesa", "ASR", 0, 2, 161):
        print("Se agrego el agente 192.168.0.17")


    #Monitorear 
    administrador.obtenerEstadoDispositivo("Dehesa", "ASR", 1, 2, 161, "192.168.43.212" )

main()
