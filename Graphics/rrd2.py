import time
import rrdtool
from getSNMP import consultaSNMP

total_input_traffic = 0
total_output_traffic = 0
total_input_ipReceives = 0
total_input_IcmpMsgs = 0
total_output_IcmpMsgs = 0
total_input_tcpSegs = 0
total_output_tcpSegs = 0
total_input_DatgramasUdp = 0
total_output_DatgramasUdp = 0


while 1:
    # Tráfico Interfaz
    total_input_traffic = int(
        consultaSNMP('Stefan10','localhost',
                     '1.3.6.1.2.1.2.2.1.10.3')) #El último dígito es la interfaz a trabajar
    total_output_traffic = int(
        consultaSNMP('Stefan10','localhost',
                     '1.3.6.1.2.1.2.2.1.16.3')) #El último dígito es la interfaz a trabajar

    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    print (valor)
    rrdtool.update('octets.rrd', valor)
    rrdtool.dump('octets.rrd','octets.xml')
    time.sleep(1)

    # IP In Receives
    total_input_ipReceives = int(
        consultaSNMP('Stefan10','localhost',
                     '1.3.6.1.2.1.4.3.0')) #El último dígito es la interfaz a trabajar

    valor = "N:" + str(total_input_ipReceives)
    print (valor)
    rrdtool.update('ipInReceives.rrd', valor)
    rrdtool.dump('ipInReceives.rrd','ipInReceives.xml')
    time.sleep(1)
    
    # ICMP Mensajes entrada/salida
    total_input_IcmpMsgs = int(
        consultaSNMP('Stefan10','localhost',
                     '1.3.6.1.2.1.5.1.0')) #El último dígito es la interfaz a trabajar
    total_output_IcmpMsgs = int(
        consultaSNMP('Stefan10','localhost',
                     '1.3.6.1.2.1.5.14.0')) #El último dígito es la interfaz a trabajar
    
    valor = "N:" + str(total_input_IcmpMsgs) + ':' + str(total_output_IcmpMsgs)
    print (valor)
    rrdtool.update('icmpMsgs.rrd', valor)
    rrdtool.dump('icmpMsgs.rrd','icmpMsgs.xml')
    time.sleep(1)
    
    # TCP Segs entrada/salida
    total_input_tcpSegs = int(
        consultaSNMP('Stefan10','localhost',
                     '1.3.6.1.2.1.6.10.0')) #El último dígito es la interfaz a trabajar
    total_output_tcpSegs = int(
        consultaSNMP('Stefan10','localhost',
                     '1.3.6.1.2.1.6.11.0')) #El último dígito es la interfaz a trabajar

    valor = "N:" + str(total_input_tcpSegs) + ':' + str(total_output_tcpSegs)
    print (valor)
    rrdtool.update('tcpSegs.rrd', valor)
    rrdtool.dump('tcpSegs.rrd','tcpSegs.xml')
    time.sleep(1)

    # Datagramas UDP 
    total_input_DatgramasUdp = int(
        consultaSNMP('Stefan10','localhost',
                     '1.3.6.1.2.1.7.1.0')) #El último dígito es la interfaz a trabajar
    total_output_DatgramasUdp = int(
        consultaSNMP('Stefan10','localhost',
                     '1.3.6.1.2.1.7.4.0')) #El último dígito es la interfaz a trabajar

    valor = "N:" + str(total_input_DatgramasUdp) + ':' + str(total_output_DatgramasUdp)
    print (valor)
    rrdtool.update('udpDatagrams.rrd', valor)
    rrdtool.dump('udpDatagrams.rrd','udpDatagrams.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)
