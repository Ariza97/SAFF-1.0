import time
import rrdtool
from getSNMP import consultaSNMP

#usar como ejemplo comunidad=Stefan10, ip=localhost, puerto=161
def realizarConsultas(comunidad, ip, puerto, numero):

    total_input_traffic = 0
    total_output_traffic = 0
    total_input_ipReceives = 0
    total_input_IcmpMsgs = 0
    total_output_IcmpMsgs = 0
    total_input_tcpSegs = 0
    total_output_tcpSegs = 0
    total_input_DatgramasUdp = 0
    total_output_DatgramasUdp = 0

    arch1Rrd = 'octets' + str(numero) + '.rrd'
    arch2Rrd = 'ipInReceives' + str(numero) + '.rrd'
    arch3Rrd = 'icmpMsgs' + str(numero) + '.rrd'
    arch4Rrd = 'tcpSegs' + str(numero) + '.rrd'
    arch5Rrd = 'udpDatagrams' + str(numero) + '.rrd'
    arch1Xml = 'octets' + str(numero) + '.xml'
    arch2Xml = 'ipInReceives' + str(numero) + '.xml'
    arch3Xml = 'icmpMsgs' + str(numero) + '.xml'
    arch4Xml = 'tcpSegs' + str(numero) + '.xml'
    arch5Xml = 'udpDatagrams' + str(numero) + '.xml'

    while 1:
        # Tráfico Interfaz
        total_input_traffic = int(
            consultaSNMP(comunidad, ip,
                         '1.3.6.1.2.1.2.2.1.10.3', puerto)) #El último dígito es la interfaz a trabajar
        total_output_traffic = int(
            consultaSNMP(comunidad, ip,
                         '1.3.6.1.2.1.2.2.1.16.3', puerto)) #El último dígito es la interfaz a trabajar

        valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
        print (valor)
        rrdtool.update(arch1Rrd, valor)
        rrdtool.dump(arch1Rrd,arch1Xml)
        time.sleep(1)

        # IP In Receives
        total_input_ipReceives = int(
            consultaSNMP(comunidad, ip,
                         '1.3.6.1.2.1.4.3.0', puerto)) #El último dígito es la interfaz a trabajar

        valor = "N:" + str(total_input_ipReceives)
        print (valor)
        rrdtool.update(arch2Rrd, valor)
        rrdtool.dump(arch2Rrd,arch2Xml)
        time.sleep(1)
        
        # ICMP Mensajes entrada/salida
        total_input_IcmpMsgs = int(
            consultaSNMP(comunidad, ip,
                         '1.3.6.1.2.1.5.1.0', puerto)) #El último dígito es la interfaz a trabajar
        total_output_IcmpMsgs = int(
            consultaSNMP(comunidad, ip,
                         '1.3.6.1.2.1.5.14.0', puerto)) #El último dígito es la interfaz a trabajar
        
        valor = "N:" + str(total_input_IcmpMsgs) + ':' + str(total_output_IcmpMsgs)
        print (valor)
        rrdtool.update(arch3Rrd, valor)
        rrdtool.dump(arch3Rrd,arch3Xml)
        time.sleep(1)
        
        # TCP Segs entrada/salida
        total_input_tcpSegs = int(
            consultaSNMP(comunidad, ip,
                         '1.3.6.1.2.1.6.10.0', puerto)) #El último dígito es la interfaz a trabajar
        total_output_tcpSegs = int(
            consultaSNMP(comunidad, ip,
                         '1.3.6.1.2.1.6.11.0', puerto)) #El último dígito es la interfaz a trabajar

        valor = "N:" + str(total_input_tcpSegs) + ':' + str(total_output_tcpSegs)
        print (valor)
        rrdtool.update(arch4Rrd, valor)
        rrdtool.dump(arch4Rrd,arch4Xml)
        time.sleep(1)

        # Datagramas UDP 
        total_input_DatgramasUdp = int(
            consultaSNMP(comunidad, ip,
                         '1.3.6.1.2.1.7.1.0', puerto)) #El último dígito es la interfaz a trabajar
        total_output_DatgramasUdp = int(
            consultaSNMP(comunidad, ip,
                         '1.3.6.1.2.1.7.4.0', puerto)) #El último dígito es la interfaz a trabajar

        valor = "N:" + str(total_input_DatgramasUdp) + ':' + str(total_output_DatgramasUdp)
        print (valor)
        rrdtool.update(arch5Rrd, valor)
        rrdtool.dump(arch5Rrd,arch5Xml)
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)

#realizarConsultas('Stefan10', 'localhost', 161)