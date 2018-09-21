# lo más probable es que siempre se tenga que ejecutar con sudo

import subprocess
import listaagentes


datos = subprocess.check_output('snmpstatus -v2c -c ASR 192.168.43.212', shell = True)

cadena = str(datos)
#Convertirlos a un array
arreglo = cadena.split()
print(arreglo)

#Obtener el numero de interfaces activas
totalInterfaces = 0

for i in range (0,len(arreglo)):

    #Mostrar el tiempo activo
    if arreglo[i] == "Up:":
        print("Tiempo activo: " + arreglo[i+1] + " " + arreglo[i+2])


    if "Interfaces" in arreglo[i]:
        totalInterfaces = int(arreglo[i+1][:2])

    #Obtener el numero total de interfaces
    elif i+1 != len(arreglo):
        if "interfaces" in arreglo[i+1]:
            totalInterfaces -= int(arreglo[i][-1:])
            print("Interfaces activas: " + str(totalInterfaces))
    
#Obtener la localizacion fisica
arrayDir = listaagentes.consultaSNMP("ASR", "192.168.43.212", "1.3.6.1.2.1.1.6.0", 161).split(' ')
print("La localizacion fisica es: " + arrayDir[len(arrayDir) - 1])

#Obtener la informacion de contacto
arrayContactInfo = listaagentes.consultaSNMP("ASR", "192.168.43.212", "1.3.6.1.2.1.1.4.0", 161).split(' ')
print("La localizacion fisica es: " + arrayContactInfo[len(arrayContactInfo) - 1])
