from localtunnel import Localtunnel
from os import environ as env
import subprocess
import requests
import time

def check_connection():
    try:
        requests.get("https://1.1.1.1/")
        return True
    except:
        return False

while not check_connection(): time.sleep(1)

destination = env.get("DESTINATION", subprocess.getoutput("ip route | grep default").split()[2])
lt = Localtunnel(int(env["PORT"]), env["DOMAIN"], destination)
print(lt.start())
while True:
    time.sleep(1)
