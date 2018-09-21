# lo más probable es que siempre se tenga que ejecutar con sudo

import subprocess, shlex

datos = subprocess.check_output('snmpstatus -v2c -c Stefan10 192.68.0.15', shell = True)
print(datos)

# Tratar cadena para obtener los datos que queremos


# Agregar una excepción por si no se ejecuta bien y cambien el status del agente a False
