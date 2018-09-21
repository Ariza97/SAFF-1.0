#!/usr/bin/env python

import rrdtool

# Tráfico
ret = rrdtool.create("octets.rrd",
                     "--start",'N',
                     "--step",'10',
                     "DS:inoctets:COUNTER:600:U:U",
                     "DS:outoctets:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:700",
                     "RRA:AVERAGE:0.5:1:600")

ret = rrdtool.create("ipInReceives.rrd",
                     "--start",'N',
                     "--step",'10',
                     "DS:inIpReceives:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:700")

ret = rrdtool.create("icmpMsgs.rrd",
                     "--start",'N',
                     "--step",'10',
                     "DS:inMsgs:COUNTER:600:U:U",
                     "DS:outMsgs:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:700",
                     "RRA:AVERAGE:0.5:1:600")

ret = rrdtool.create("tcpSegs.rrd",
                     "--start",'N',
                     "--step",'10',
                     "DS:inTcpSegs:COUNTER:600:U:U",
                     "DS:outTcpSegs:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:700",
                     "RRA:AVERAGE:0.5:1:600")

ret = rrdtool.create("udpDatagrams.rrd",
                     "--start",'N',
                     "--step",'10',
                     "DS:inDatagrams:COUNTER:600:U:U",
                     "DS:outDatagrams:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:700",
                     "RRA:AVERAGE:0.5:1:600")

if ret:
    print (rrdtool.error())

