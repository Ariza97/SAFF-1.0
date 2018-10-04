import sys
import rrdtool
import time

def crearGraficas(numero):
  
  tiempo_actual = int(time.time())
  tiempo_final = tiempo_actual - 86400
  tiempo_inicial = tiempo_final - 25920000

  arch1Rrd = 'octets' + str(numero) + '.rrd'
  arch2Rrd = 'ipInReceives' + str(numero) + '.rrd'
  arch3Rrd = 'icmpMsgs' + str(numero) + '.rrd'
  arch4Rrd = 'tcpSegs' + str(numero) + '.rrd'
  arch5Rrd = 'udpDatagrams' + str(numero) + '.rrd'
  arch1Png = 'octets' + str(numero) + '.png'
  arch2Png = 'ipInReceives' + str(numero) + '.png'
  arch3Png = 'icmpMsgs' + str(numero) + '.png'
  arch4Png = 'tcpSegs' + str(numero) + '.png'
  arch5Png = 'udpDatagrams' + str(numero) + '.png'

  while 1:
    # Tráfico interfaces
    ret = rrdtool.graph( arch1Png,
      "--start",'1538358221',
  #    "--end","N",
      "--vertical-label=Bytes/s",
      "DEF:inoctets=" + arch1Rrd + ":inoctets:AVERAGE",
      "DEF:outoctets=" + arch1Rrd + ":outoctets:AVERAGE",
      "AREA:inoctets#C42121:In traffic",
      "LINE1:outoctets#F2FA0B:Out traffic\r")

    # Ip In Receives
    ret = rrdtool.graph( arch2Png,
      "--start",'1538358221',
  #    "--end","N",
      "--vertical-label=Bytes/s",
      "DEF:inIpReceives=" + arch2Rrd + ":inIpReceives:AVERAGE",
      "AREA:inIpReceives#00FF00:IP In Receives\r")

    # ICMP Msgs entrada/salida
    ret = rrdtool.graph( arch3Png,
      "--start",'1538358221',
  #    "--end","N",
      "--vertical-label=Bytes/s",
      "DEF:inMsgs=" + arch3Rrd + ":inMsgs:AVERAGE",
      "DEF:outMsgs=" + arch3Rrd + ":outMsgs:AVERAGE",
      "AREA:inMsgs#C30BFA:ICMP In Msgs",
      "LINE1:outMsgs#FA0BAB:ICMP Out Msgs\r")

    # TCP Segs entrada/salida
    ret = rrdtool.graph( arch4Png,
      "--start",'1538358221',
  #    "--end","N",
      "--vertical-label=Bytes/s",
      "DEF:inTcpSegs=" + arch4Rrd + ":inTcpSegs:AVERAGE",
      "DEF:outTcpSegs=" + arch4Rrd + ":outTcpSegs:AVERAGE",
      "AREA:inTcpSegs#0BFAEA:TCP In Segs",
      "LINE1:outTcpSegs#0B4BFA:TCP Out Segs\r")

    # UDP Datagrams entrada/salida
    ret = rrdtool.graph( arch5Png,
      "--start",'1538358221',
  #    "--end","N",
      "--vertical-label=Bytes/s",
      "DEF:inDatagrams=" + arch5Rrd + ":inDatagrams:AVERAGE",
      "DEF:outDatagrams=" + arch5Rrd + ":outDatagrams:AVERAGE",
      "AREA:inDatagrams#7A807E:In UDP Datgrams",
      "LINE1:outDatagrams#151817:Out UDP Datgrams\r")
    
    time.sleep(10)

#crearGraficas()