from main import Aobscan
from keyauth import api
import webbrowser
import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime
def water(text):
    os.system(""); faded = ""
    green = 10
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded

thex = 0 

def purple(text):
    os.system("")
    faded = ""
    down = False

    for line in text.splitlines():
        red = 40
        for character in line:
            if down:
                red -= 3
            else:
                red += 3
            if red > 254:
                red = 255
                down = True
            elif red < 1:
                red = 30
                down = False
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
    return faded


banner = f"""



            ██████  ██ ███    ███ ███████  ██████   ██████  ██████   ██████  ██      
            ██   ██ ██ ████  ████ ██      ██    ██ ██      ██    ██ ██    ██ ██      
            ██████  ██ ██ ████ ██ ███████ ██    ██ ██      ██    ██ ██    ██ ██      
            ██   ██ ██ ██  ██  ██      ██ ██    ██ ██      ██    ██ ██    ██ ██      
            ██████  ██ ██      ██ ███████  ██████   ██████  ██████   ██████  ███████ 
                                                                                                                                                       

           {purple(f"[>] Create by bimsocool")}
"""


print(water(banner))

def clear():
    if platform.system() == 'Windows':
        os.system('cls & title Python Example')  # clear console, change title
    elif platform.system() == 'Linux':
        os.system('clear')  # clear console
        sys.stdout.write("\x1b]0;Python Example\x07")  # change title
    elif platform.system() == 'Darwin':
        os.system("clear && printf '\e[3J'")  # clear console
        os.system('''echo - n - e "\033]0;Python Example\007"''')  # change title

print("Initializing")


def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "",
    ownerid = "",
    secret = "",
    version = "",
    hash_to_check = getchecksum()
)

def answer():
    try:
        print("""1.Login
2.Register
3.License Key Only
        """)
        ans = input("Select Option: ")
        if ans == "1":
            user = input('Username: ')
            password = input('Password: ')
            keyauthapp.login(user, password)
        elif ans == "2":
            user = input('Provide username: ')
            password = input('Provide password: ')
            license = input('Provide License: ')
            keyauthapp.register(user, password, license)
        elif ans == "100":
            user = input('Provide username: ')
            license = input('Provide License: ')
            keyauthapp.upgrade(user, license)
        elif ans == "3":
            key = input('Enter your license: ')
            keyauthapp.license(key)
        else:
            print("\nInvalid option")
            sleep(1)
            clear()
            answer()
           # menu_game()
    except KeyboardInterrupt:
        os._exit(1)


answer()

#print("Expires at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'))




def menu_game():
    clear()
    try:
        print("""
1.Menu Hack
2.Support
3.Information
        """)
        ans = input("Select Option: ")
        if ans == "1":

            


                print("""
1.Aob Scan (login)
2.Back 
3.exit

        """)   
                key = input("Select Option: ")    
                if key == "1":
                    Aobscan.aobscan()            
                
                
                elif key == "2":
                    menu_game()   
                elif key == "8":
                    thex = 8           
        elif ans == "3":
            print("\nUser data: ")
            print("Username: " + keyauthapp.user_data.username)
            print("IP address: " + keyauthapp.user_data.ip)
            print("Hardware-Id: " + keyauthapp.user_data.hwid)

            #subs = keyauthapp.user_data.subscriptions  # Get all Subscription names, expiry, and timeleft
            
            #sub = subs[i]["subscription"]  # Subscription from every Sub
            print("Created at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S'))
            print("Last login at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S'))
            
            print("""
1.Back 
2.Exit
                  """)
            key2 = input("Select Option: ")  
            if key2 ==  "1":
                menu_game()
            elif key2 == "2":
                os._exit(1)
        
        elif ans == "2":
            webbrowser.open('https://discord.gg/Q28hbdGwWv')
        else:
            print("\nInvalid option")
            sleep(1)
            clear()
            menu_game()
            
    except KeyboardInterrupt:
        os._exit(1)

menu_game()






