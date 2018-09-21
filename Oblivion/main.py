import sys
import os
import subprocess
from pysnmp.hlapi import *
from Admin import Admin
import listaagentes


def main():

    #Crear un administrador con contrasenia
    administrador = Admin('root', 'root')

    #Agregar un agente
    if administrador.agregarAHostIP("192.168.0.17", "winB", "comunidad3", 0, 2, 161):
        print("Se agrego el agente 192.168.0.17")

    for i in listaagentes.listaAgentes:
        print(i.getNombre())

main()
