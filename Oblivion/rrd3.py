import sys
import rrdtool
import time

def crearGraficas():
  
  tiempo_actual = int(time.time())
  tiempo_final = tiempo_actual - 86400
  tiempo_inicial = tiempo_final - 25920000

  while 1:
    # Tráfico interfaces
    ret = rrdtool.graph( "octets.png",
      "--start",'1537441080',
  #    "--end","N",
      "--vertical-label=Bytes/s",
      "DEF:inoctets=octets.rrd:inoctets:AVERAGE",
      "DEF:outoctets=octets.rrd:outoctets:AVERAGE",
      "AREA:inoctets#00FF00:In traffic",
      "LINE1:outoctets#0000FF:Out traffic\r")

    # Ip In Receives
    ret = rrdtool.graph( "ipInReceives.png",
      "--start",'1537441080',
  #    "--end","N",
      "--vertical-label=Bytes/s",
      "DEF:inIpReceives=ipInReceives.rrd:inIpReceives:AVERAGE",
      "AREA:inIpReceives#00FF00:IP In Receives\r")

    # ICMP Msgs entrada/salida
    ret = rrdtool.graph( "icmpInMsgs.png",
      "--start",'1537441080',
  #    "--end","N",
      "--vertical-label=Bytes/s",
      "DEF:inMsgs=icmpMsgs.rrd:inMsgs:AVERAGE",
      "DEF:outMsgs=icmpMsgs.rrd:outMsgs:AVERAGE",
      "AREA:inMsgs#00FF00:ICMP In Msgs",
      "LINE1:outMsgs#0000FF:ICMP Out Msgs\r")

    # TCP Segs entrada/salida
    ret = rrdtool.graph( "tcpSegs.png",
      "--start",'1537441080',
  #    "--end","N",
      "--vertical-label=Bytes/s",
      "DEF:inTcpSegs=tcpSegs.rrd:inTcpSegs:AVERAGE",
      "DEF:outTcpSegs=tcpSegs.rrd:outTcpSegs:AVERAGE",
      "AREA:inTcpSegs#00FF00:TCP In Segs",
      "LINE1:outTcpSegs#0000FF:TCP Out Segs\r")

    # UDP Datagrams entrada/salida
    ret = rrdtool.graph( "udpDatagrams.png",
      "--start",'1537441080',
  #    "--end","N",
      "--vertical-label=Bytes/s",
      "DEF:inDatagrams=udpDatagrams.rrd:inDatagrams:AVERAGE",
      "DEF:outDatagrams=udpDatagrams.rrd:outDatagrams:AVERAGE",
      "AREA:inDatagrams#00FF00:In UDP Datgrams",
      "LINE1:outDatagrams#0000FF:Out UDP Datgrams\r")
    
    time.sleep(10)

#crearGraficas()