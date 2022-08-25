import os
os.system('clear')

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[0m"

Side="otaku"

def listop(side):
    print('''
            [1]      list            Listar dispositivos conectados
            [2]      start           Espelhar celular agora
            [3]      config          Conectar disposito via WI-FI

            [4] Feichar programa
    ''')
    insertquery =input(side+ g+" option number: "+w)
    option(insertquery)

def header():
    print (g+"                        dP "+b+"                   oo                             "+w)
    print (g+"                        88 "+b+"                                                  "+w)
    print (g+" .d8888b. 88d888b. .d888b88"+b+" .d8888b. dP   .dP dP .d8888b. .d8888b. .d8888b.  "+w)
    print (g+" 88'  `88 88'  `88 88'  `88"+b+" 88ooood8 88   d8' 88 88'  `"" 88ooood8 Y8ooooo.  "+w) 
    print (g+" 88.  .88 88    88 88.  .88"+b+" 88.  ... 88 .88'  88 88.  ... 88.  ...       88  "+w) 
    print (g+" `88888P8 dP    dP `88888P8"+b+" `88888P' 8888P'   dP `88888P' `88888P' `88888P'  "+w) 

def script(comando):
    os.system(comando)
    insert=b+"\n[otaku]"
    insertquery =input(insert+ g+" option number: "+w)
    option(insertquery)

def wifi(port,ip):
    os.system("\nadb tcpip "+port+"; adb connect "+ip+"; adb devices")
    insert=str("\n["+ip+":"+port+"]")
    Side=str(ip+":"+port)
    insertquery =input(insert+ g+" option number: "+w)
    option(insertquery)

def option(query):
    if query == "1" or query == "list" or query == "listar":
        script("adb devices")
    if query == "2" or query == "start" or query == "iniciar" or query == "scrcpy":
        script("scrcpy")
    if query == "3" or query == "config" or query == "configurar" or query == "wifi":
        insert=r+"\n[scrcpy wi-fi]"
        setport =input(insert+ g+" Set port: "+w)
        print("set port "+y+setport)
        setip =input(insert+ g+" Set ip: "+w)
        print("set ip "+y+setip+w)
        wifi(setport,str(setip))
    if query == "4" or query == "exit" or query == "close" or query == "feichar":
        os.system('exit')

    if query == "0" or query == "help" or query == "ajuda":
       listop(b+"\n["+Side+"]")
    if query == "cls" or query == "clear" or query == "clean" or query == "limpar":
       os.system('clear')
       home()

def home():                                                                                         
    header()
    listop(b+"\n["+Side+"]")

home()

