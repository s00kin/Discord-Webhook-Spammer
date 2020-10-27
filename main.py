import requests, time
import sys
import os
import json

os.system('cls' if os.name == 'nt' else 'clear')
print("Loading...")
time.sleep(5)
sys.stdout.write("\x1b]2;Discord Webhook Spammer - Made by sokin#2016\x07")
end = False
menu = 0

class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[  1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

while not end:
    if menu == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(color.GREEN)
        print("  _____  _                       _                  __        _    _       ")
        print(" |  __ \(_)                     | |                / /       | |  (_)      ")
        print(" | |  | |_ ___  ___ ___  _ __ __| |  __ _  __ _   / /__  ___ | | ___ _ __  ")
        print(" | |  | | / __|/ __/ _ \| '__/ _` | / _` |/ _` | / / __|/ _ \| |/ / | '_ \ ")
        print(" | |__| | \__ \ (_| (_) | | | (_| || (_| | (_| |/ /\__ \ (_) |   <| | | | |")
        print(" |_____/|_|___/\___\___/|_|  \__,_(_)__, |\__, /_/ |___/\___/|_|\_\_|_| |_|")
        print("                                     __/ | __/ |                           ")
        print("                                    |___/ |___/                            ")
        print(color.END)
        print(color.CYAN, "Discord: "+color.RED+"sokin#2016")
        print(color.CYAN, "Invite: "+color.RED+"discord.gg/sokin")
        print("")
        print(color.BLUE,"[",color.RED+"1",color.BLUE+"]",color.PURPLE,"Start Webhook Spammer")
        print(color.BLUE,"[",color.RED+"2",color.BLUE+"]",color.PURPLE,"Start Webhook Spammer From Config File")
        print(color.BLUE,"[",color.RED+"3",color.BLUE+"]",color.PURPLE,"Exit")
        print("")
        opt = input("Please Select an option (1-2): ")
        if opt == "1":
            print(color.END)
            menu = 1
        if opt == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(color.END)
            menu = 2
        if opt == "3":
            print(color.END)
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()

    if menu ==1:
        os.system('cls' if os.name == 'nt' else 'clear')
        #Webhook Link
        print ("Webhook Link:") 
        link = input("Paste Link > ")
        os.system('cls' if os.name == 'nt' else 'clear')
        #Message Content
        print("Message ")
        message = input("Message Content > ")
        os.system('cls' if os.name == 'nt' else 'clear')
        #Webhook Name
        print("Name ")
        name = input("Webhook Username > ")
        os.system('cls' if os.name == 'nt' else 'clear')
        #Webhook Profile PIC
        print("Profile Pic ")
        pp = input("Paste Image Link > ")

        payload = {
            'content': message,
            'username': name,
            'avatar_url': pp,
        }

        while True:
            try:
                time.sleep(0.5)
                r = requests.post(link, json=payload)
                if r.status_code == 204:
                    print("Message Sent!")
                else:
                    print("Ratelimit/Error")
            except requests.exceptions.MissingSchema:
                print(" Bad Link/Url");break


    if menu == 2:
        print ("Webhook Link:") 
        link = input("Paste Link > ")
        os.system('cls' if os.name == 'nt' else 'clear')
        with open('config.json') as f:
            data = json.load(f)
        while True:
            try:
                time.sleep(0.5)
                r = requests.post(link, data)
                if r.status_code == 204:
                    print("Message Sent! Ctrl-C to stop!")
                else:
                    print("Ratelimit/Error")
            except requests.exceptions.MissingSchema:
                print(" Bad Link/Url");break         
