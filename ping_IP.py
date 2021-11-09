#Program to PING a target system using arguments
#It can only run in terminal after cloning

import sys
import os

print("Number of pings "+sys.argv[1])           #second argument
print("IP adress ping to "+sys.argv[2])         #third argument

#os.system('ping -c number_of_pings Target_IP')
os.system('ping -c '+sys.argv[1]+' '+sys.argv[2])
