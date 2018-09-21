from pysnmp.hlapi import *
resultado =""
varAux =""

#Declaracion de la variable global
listaAgentes = []

def consultaSNMP(comunidad,host,oid,puerto):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(comunidad),
               UdpTransportTarget((host, puerto)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))))

    if errorIndication:
        return errorIndication

    elif errorStatus:
        return '%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?') 

    else:
        for varBind in varBinds:
          varAux=' = '.join([x.prettyPrint() for x in varBind])
            
        return varAux

def estatusDeConexion(comunidad,host,oid,puerto):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(comunidad),
               UdpTransportTarget((host, puerto)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))))

    if errorStatus:
        return False

    return True