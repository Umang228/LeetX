#!/usr/bin/env python
import socket
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

def logo():
    print(color.PURPLE + """
   _____                     _____   ____  _____ _______
  / ____|        /\         |  __ \ / __ \|  __ \__   __|
 | (___   ___   /  \   _ __ | |__) | |  | | |__) | | |
  \___ \ / __| / /\ \ | '_ \|  ___/| |  | |  _  /  | |
  ____) | (__ / ____ \| | | | |    | |__| | | \ \  | |
 |_____/ \___/_/    \_\_| |_|_|     \____/|_|  \_\ |_|

                                                            """ + color.END)

def screen_clear():
    if os.name == 'posix': #for linux,unix,mac
      _ = os.system('clear')
    else:   #windows
      _ = os.system('cls')

screen_clear()
logo()

try :
    print(color.lightblue + "="*50)
    ask = input(color.pink + color.BOLD + "Target To Scan : " + color.END)
    target = socket.gethostbyname(ask)

except KeyboardInterrupt :
    print("")
    print(color.BLUE + "*"*50)
    print(color.RED + "\nOops You Cloesd The Program.....!!!")
    sys.exit()

except socket.gaierror as gaierror:
    print("")
    print(gaierror)
    print("")
    print(color.pink +"*"*50)
    print(color.RED +"It seems invalid target is entered ")
    print("")
    sys.exit()

def long_scan():
    print(color.BOLD+ color.DARKCYAN +"It will take long time to complete.\nYou can Go for Binge-Watching or continue your work side by.")
    try:
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((target,port))
            if result ==0:
                print("")
                print(color.RED + "Port Open : "+color.YELLOW+ "%s" %port + color.END )
                print("")
            else :
                print(color.GREEN + "Port Closed : " +color.YELLOW+ "%s" %port + color.END )

            s.close()

    except KeyboardInterrupt :
        print("")
        print(color.BLUE + "*"*50)
        print(color.RED + "\nOops You Cloesd The Program.....!!!")
        sys.exit()

    except socket.gaierror as gaierror:
        print("")
        print(gaierror)
        print("")
        print(color.pink +"*"*50)
        print(color.RED +"It seems invalid target is entered ")
        print("")
        sys.exit()

    except socket.error:
        print(color.BLUE + "\n Server Not Responding...!!!" + color.END)
        sys.exit()

    except socket.timeout:
        print(color.BLUE + "\n Server TimeOut...!!!" + color.END)
        sys.exit()

def fast_scan():
    print(color.lightgreen + "Wait For While to start......")
    try:
        for port in [20, 22, 25, 53, 80, 110, 143, 443] :
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((target,port))
            if result == 0:
                print(color.RED + "Port Open   : "+color.YELLOW+ "%s" %port + color.END )

            else :
                print(color.GREEN + "Port Closed : " +color.YELLOW+ "%s" %port + color.END )

            s.close()

    except KeyboardInterrupt :
        print("")
        print(color.BLUE + "*"*50)
        print(color.RED + "\nOops You Cloesd The Program.....!!!")
        sys.exit()

    except socket.error:
        print(color.BLUE + "\n Server Not Responding...!!!" + color.END)
        sys.exit()

    except socket.timeout:
        print(color.BLUE + "\n Server TimeOut...!!!" + color.END)
        sys.exit()

    except socket.gaierror as gaierror:
        print("")
        print(gaierror)
        print("")
        print(color.pink +"*"*50)
        print(color.RED +"It seems invalid target is entered ")
        print("")
        sys.exit()

def banner():
    screen_clear()
    logo()
    print(color.RED  +   "\n\n+********************************************************+ " )
    print(color.BLUE +   "      Scanning Target : %s                                     " %target )
    print(color.RED  +   "+********************************************************+ " + color.END)

def banner2():
    screen_clear()
    logo()
    print(color.lightgreen +
          """
          +************************************+
          *                                    *
          *  1) Fast Scan                      *
          *   =>scans some common known ports  *
          *                                    *
          *  2) Full Scan                      *
          *   =>Scan all ports from 1 to 65535 *
          *                                    *
          +************************************+
           """ + color.END)
try:
    banner2()
    ask2 = input(color.DARKCYAN + color.BOLD + "Choose a Scan : " + color.END)
    if ask2 == "1":
        banner()
        fast_scan()
    elif ask2 == "2" :
        banner()
        long_scan()
    else:
        print(color.RED + color.BOLD +"\nOops Wrong Scan choosed..!!\nRe-RUN the program :)")
        sys.exit()
except:
    pass