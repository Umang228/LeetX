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

  print(color.CYAN+ """
  .▄▄ · .▄▄▄  ▄▄▌  ▄▄▄ .▄▄▄ .▄▄▄▄▄
  ▐█ ▀. ▐▀•▀█ ██•  ▀▄.▀·▀▄.▀·•██
  ▄▀▀▀█▄█▌·.█▌██▪  ▐▀▀▪▄▐▀▀▪▄ ▐█.▪
 ▐█▄▪▐█▐█▪▄█·▐█▌▐▌▐█▄▄▌▐█▄▄▌ ▐█▌·
  ▀▀▀▀ ·▀▀█. .▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀
                          """)

import time
import os
import platform
import sys

current_time = color.RED + str([time.asctime()])  #gives day,date,time,year


def screen_clear():
   if os.name == 'posix': #for linux,unix,mac
      _ = os.system('clear')
   else:   #windows
      _ = os.system('cls')

def exiting():
  ask = input(color.BOLD+ color.Black + '\nDo You Want To Exit The Program(y:n) : ' + color.RED )
  def close():
    time.sleep(2)
    print(current_time + color.GREEN + "  Exiting the program.....")
    time.sleep(0.3)
    print(current_time + color.GREEN + "  Thanks for using SQLEET")
    time.sleep(2)
    screen_clear()
    logo()
  if ask == 'y':
    close()
  else:
    print("There is nothing more in the Program we are closing program... " + color.YELLOW+":)")
    close()

def dependencies_check():
  screen_clear()
  print(current_time + color.BOLD + color.GREEN +  "  Checking for dependencies.....")
  import mechanize
  import webbrowser
  time.sleep(1)
  print(current_time + color.BOLD  + color.GREEN + "  Dependencies satsfied.....")
  time.sleep(0.5)
  screen_clear()

def error_import():
  print("\n\n")
  print(color.BOLD + color.RED + color.UNDERLINE + "*"*50)
  print(color.BOLD + color.UNDERLINE + color.RED+ "INSTALLATION ERROR ===>" + color.Black + "It Seems Dependencies are not getting properly installed on your system. \nWe recommend you to Install " + color.RED + "webbrowser and mechanize" + color.Black +" module by our own according to your respective system'\n" + color.RED +"SOME KNOWN COMMANDS YOU CAN TRY : " + color.Black + "\n==> For Linux and Mac : \n* sudo pip3 install mechainze  \n* sudo pip3 install webbrowser \n==> For Termux and Windows  : \n* pip3 install mechanize \n* pip3 install webbrowser \nIf still Bug Remains Contact the develpor :)"+ color.END)
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

except ImportError :
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
        print(current_time + color.BOLD + color.GREEN + "  installing Mechanize module...\n" + color.END)
        time.sleep(0.5)
        os.system('pip3 install mechanize')        
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
        print(current_time + color.BOLD + color.GREEN + "  installing Mechanize module..." + color.END)
        time.sleep(0.5)
        os.system('sudo pip3 install mechanize')
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
        print(current_time + color.BOLD + color.GREEN + "  installing Mechanize module..." + color.END)
        time.sleep(0.5)
        os.system('pip3 install mechanize')
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
          
import mechanize  #module to deal with website
import webbrowser  #module to open website in browser

logo()
print(color.RED + "========================================================================")
print(color.GREEN +"\nLEGAL DISCLAIMER: This Tool contains materials that can be potentially damaging or dangerous.It is the end users responsibility to obey all applicable local, state and federal laws.Developers assume no liability and are not responsible for any misuse or damage caused by this program.\n")
print(color.RED+ "========================================================================" )
br = mechanize.Browser()  #making browser from mechanize
print(color.BOLD + color.Black + "Compulsory Format : http://www.xyz.com/php?id=n ")
url = input(color.BOLD + color.Black + "Enter-The-URL : " + color.RED )
screen_clear()

print(current_time +color.RED + "  Byassing Robots.txt........")
br.set_handle_robots(False) #setting default robots.txt to False for bypass and adding header to repsonse send to site
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
time.sleep(1)

def wafdetection():
  ask3 = input(color.BOLD + color.Black + "\nDo you want a WAF detection in site enter(y:n) : " + color.RED)
  if ask3 == 'y':
    print(current_time + color.GREEN + "  fetching URL.....")
    time.sleep(0.5)
    print(current_time + color.GREEN + "  Applying injection for WAF Detection...")
    time.sleep(0.5)
    url2 = url  + " union select " #union select command is blocked by firewalls so we use it to detect them

    def browser():
      ask4 = input(color.BOLD + color.Black + '\nDo You Want to See WAF Detection Result in your Browser(y:n) : ' + color.RED)
      if ask4 == 'y':
        print(current_time + color.GREEN + "Opening Site in suitable web browser.....")
        webbrowser.open(url2) #open url in browser
        exiting()
      else:
        exiting()

    print(current_time + color.GREEN + "  (union select) injection applied")
    response2 = br.open(url2)
    print(current_time + color.GREEN + "  Opening the URL......")
    time.sleep(0.5)
    body2 = response2.read() #reading response
    print(current_time + color.GREEN + "  Reading the Response...")
    time.sleep(0.5)
    fullbody2 = body2.decode('utf-8') #converting it into utf-8 format
    print(current_time + color.GREEN + "  Decoding the Response...")
    time.sleep(0.5)

    if "An appropriate representation of the requested resource could not be found on this server. This error was generated by Mod_Security." in fullbody2: #error in Mod_Security
      print(fullbody2)
      print(current_time + color.BOLD + color.Black+ "  Mod_Security Web Firewall is detected in the site !!!")
      browser()
    elif "Access Denied" in fullbody2: #error in Sucuri Firewall used to detect them
      print(fullbody2)
      print(current_time + color.BOLD + color.Black + "  Sucuri Website Firewall detected !!!")
      browser()
    else :
      print(current_time + color.BOLD + color.Black + "  No Web Firewall is detected in site")
      browser()
  else:
    exiting()

def test():
  screen_clear()
  logo()
  time.sleep(1)
  print(current_time + color.GREEN + "  Sucessfully Bypassed Robots.txt")
  time.sleep(0.5)
  print(current_time + color.GREEN +  "  SQL injection testing started......")
  time.sleep(0.5)
  try:
        url1 = url + "'" #injection
        print(current_time + color.GREEN + "  injection (') injected in URL")
        response = br.open(url1)
        time.sleep(0.5)
        print(current_time + color.GREEN + "  Opening URL")
        body = response.read()
        time.sleep(0.5)
        print(current_time + color.GREEN + "  Reading Response from URL")
        fullbody = body.decode('utf-8')
        time.sleep(0.5)
        print(current_time + color.GREEN + "  Decoding URL into UTF-8 format")
        time.sleep(0.5)
        print(current_time + color.GREEN + "  Checking for the vulenrability in response")

        def error_msg():
          ask = input(color.BOLD + color.Black + "\nDo You Want to see full error message(y:n) : " + color.RED)
          if ask == 'y':
            print(current_time + color.GREEN + "  Reading the full error meaasge from site.....")
            time.sleep(0.5)
            print(current_time + color.GREEN + "  Printing Full Error Message....")
            time.sleep(0.5)
            print(current_time+ color.GREEN + "\nThis is the Response from %s after testing the site" %(url1)  )
            time.sleep(1)
            print("\n")
            print(color.Black + (fullbody))
            ask2 = input(color.BOLD + color.Black + "\nDo You Want to view Error Result in Browser(y:n) : " + color.RED)
            if ask2 == 'y':
              print(current_time + color.GREEN + "Opening Site in suitable web browser.....")
              webbrowser.open(url1)
              wafdetection()
            else:
              wafdetection()
          else:
            ask2 = input(color.BOLD + color.Black + "\nDo You Want to view Error Result in Browser(y:n) : " + color.RED)
            if ask2 == 'y':
              print(current_time + color.GREEN + "Opening Site in suitable web browser.....")
              webbrowser.open(url1)
              wafdetection()
            else:
              wafdetection()
#These all Traditonal types of Error in the respective server used to detect server and vulenrability
        if "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near " in fullbody:
          print(current_time +color.BOLD + color.Black + "  This site is Vulnerable to Error based SQL injection  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site uses MySQL Server  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site give traditional MySQL Error Style ")
          time.sleep(0.5)
          error_msg()
        elif "Server Error in " in fullbody:
          print(current_time +color.BOLD + color.Black + "  This site is Vulnerable to Error based SQL injection  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site uses MSSQL ASPX Server  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site give traditional MSSQL ASPX Style ")
          time.sleep(0.5)
          error_msg()
        elif "Fatal error: Uncaught exception " in fullbody :
          print(current_time +color.BOLD + color.Black + "  This site is Vulnerable to Error based SQL injection  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site uses MSAccess (Apache PHP) Server ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site give traditional MSAcess(Apache PHP) Error Style  ")
          time.sleep(0.5)
          error_msg()
        elif "Microsoft JET Database Engine" in fullbody :
          print(current_time +color.BOLD + color.YELLOW + "  This site is Vulnerable to Error based SQL injection  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site uses MSAccesss (IIS ASP) Server ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site give traditional MSAccesss (IIS ASP) Error Style  ")
          time.sleep(0.5)
          error_msg()
        elif "SQL command not properly ended" in fullbody :
          print(current_time +color.BOLD + color.Black + "  This site is Vulnerable to Error based SQL injection  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site uses Oracle Server ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site give traditional Oracle Error Style  ")
          time.sleep(0.5)
          error_msg()
        elif "Microsoft OLE DB Provider" in fullbody:
          print(current_time +color.BOLD + color.Black + "  This site is Vulnerable to Error based SQL injection  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site uses ODBC Server  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site give traditional ODBC Error Style  ")
          time.sleep(0.5)
          error_msg()
        elif "PSQLException: ERROR: unterminated quoted string at or near" in fullbody:
          print(current_time +color.BOLD + color.Black + "  This site is Vulnerable to Error based SQL injection  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site uses PostgreSQL Server  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site give traditional PostgreSQL Error Style  ")
          time.sleep(0.5)
          error_msg()
        elif "Microsoft SQL Native Client error" in fullbody:
          print(current_time +color.BOLD + color.Black + "  This site is Vulnerable to Error based SQL injection  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site uses MS SQL Server  ")
          time.sleep(0.5)
          print(current_time +color.BOLD + color.GREEN + "  This site give traditional MS SQL Error Style  ")
          time.sleep(0.5)
          error_msg()
        else:
          print(current_time +color.BOLD + color.Black + "  This site is not Vulnerable to Error based SQL injection  ")
          exiting()
#if any senseless data or wrong url, entered in url  this is to deal with error
  except :
    print("\n\n")
    print(color.BOLD + color.RED + color.UNDERLINE + "*"*50)
    print(color.BOLD + color.RED +color.UNDERLINE+ "ERROR ===>" + color.Black + " There is Error either in the URL given or Error in Site itself \nTry with another site.\nSOME TRICKS: \n* Add http/https to url. \n* Recheck the url. \n* Manually open the site and test it with sqli. \nIf bug remain contact the Developer :)")
    print(color.BOLD + color.RED + "*"*50)
    print("")
    time.sleep(4)

test()
