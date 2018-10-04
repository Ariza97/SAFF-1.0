#!/usr/bin/env python

import rrdtool

def archivoRrd(numero):

       arch1Rrd = 'octets' + str(numero) + '.rrd'
       arch2Rrd = 'ipInReceives' + str(numero) + '.rrd'
       arch3Rrd = 'icmpMsgs' + str(numero) + '.rrd'
       arch4Rrd = 'tcpSegs' + str(numero) + '.rrd'
       arch5Rrd = 'udpDatagrams' + str(numero) + '.rrd'

       # Tráfico interfaces entrada/salida
       ret = rrdtool.create(arch1Rrd,
                            "--start",'N',
                            "--step",'10',
                            "DS:inoctets:COUNTER:600:U:U",
                            "DS:outoctets:COUNTER:600:U:U",
                            "RRA:AVERAGE:0.5:1:700",
                            "RRA:AVERAGE:0.5:1:600")
       # IP in Receives
       ret = rrdtool.create(arch2Rrd,
                            "--start",'N',
                            "--step",'10',
                            "DS:inIpReceives:COUNTER:600:U:U",
                            "RRA:AVERAGE:0.5:1:700")

       #IMCP Msgs entrada/salida
       ret = rrdtool.create(arch3Rrd,
                            "--start",'N',
                            "--step",'10',
                            "DS:inMsgs:COUNTER:600:U:U",
                            "DS:outMsgs:COUNTER:600:U:U",
                            "RRA:AVERAGE:0.5:1:700",
                            "RRA:AVERAGE:0.5:1:600")

       #TCP Segs entrda/salida
       ret = rrdtool.create(arch4Rrd,
                            "--start",'N',
                            "--step",'10',
                            "DS:inTcpSegs:COUNTER:600:U:U",
                            "DS:outTcpSegs:COUNTER:600:U:U",
                            "RRA:AVERAGE:0.5:1:700",
                            "RRA:AVERAGE:0.5:1:600")

       #UDP Datagramas entrada/salida
       ret = rrdtool.create(arch5Rrd,
                            "--start",'N',
                            "--step",'10',
                            "DS:inDatagrams:COUNTER:600:U:U",
                            "DS:outDatagrams:COUNTER:600:U:U",
                            "RRA:AVERAGE:0.5:1:700",
                            "RRA:AVERAGE:0.5:1:600")

       if ret:
           print (rrdtool.error())

#archivoRrd()