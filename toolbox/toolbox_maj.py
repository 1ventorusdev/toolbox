#!/usr/bin/env python

import os
import time
import sys
import platform
import subprocess
import urllib.request

def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def install_toolbox():
    system = platform.system()
    if system == "Windows":

        if os.path.exists("toolbox_win.py"):
            os.remove("toolbox_win.py")
            time.sleep(0.5)
            fetch_file("https://raw.githubusercontent.com/1ventorusdev/toolbox/main/toolbox/toolbox_win.py", "toolbox_win.py")
            print("toolbox_win.py a été récupéré depuis GitHub.")
            print("installation terminé !")
        else:
            print("Le fichier n'existe pas.")
        
    elif system == "Linux":

        if os.path.exists("toolbox_linux.py"):
            os.remove("toolbox_linux.py")
            time.sleep(0.5)
            fetch_file("https://raw.githubusercontent.com/1ventorusdev/toolbox/main/toolbox/toolbox_linux.py", "toolbox_linux.py")
            print("toolbox_linux.py a été récupéré depuis GitHub.")
            print("installation terminé !")
        else:
            print("Le fichier n'existe pas.")
            
    else:
        print("Système non pris en charge. recommencez lorsque votre systeme sera pris en charge")
        return

if __name__ =="__main__":
    try:
        install_toolbox()
    except OSError:
        print("impossible de se connecter pour faire la mise a jour")
