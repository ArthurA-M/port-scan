#!/usr/bin/env python

import socket, sys
from colorama import init, Fore

init()
GREEN = Fore.GREEN
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

def open_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, int(port)))
        sock.close()
    except:return False
    return True

if sys.argv[1] == "all":
    for i in range(int(sys.argv[3]),int(sys.argv[4])+1):
        if open_port(sys.argv[2], i):
            print(f"{GREEN}[+] {sys.argv[2]}:{i} is open")
        else:
            print(f"{GRAY}[-] {sys.argv[2]}:{i} is close")

elif sys.argv[1] == "open":
    for i in range(int(sys.argv[3]),int(sys.argv[4])+1):
        if open_port(sys.argv[2], i):
            print(f"{GREEN}[+] {sys.argv[2]}:{i} is open")

elif sys.argv[1] == "listen":
    ports = [i for i in range(int(sys.argv[3]),int(sys.argv[4])+1) if open_port(sys.argv[2], i)]
    while True:
        new_ports = [i for i in range(int(sys.argv[3]),int(sys.argv[4])+1) if open_port(sys.argv[2], i)]
        if ports != new_ports:
            add = [i for i in new_ports if i not in ports]
            delete = [i for i in ports if i not in new_ports]
            for i in add:
                print(f"{GREEN}[+] {sys.argv[2]}:{i} is opened")
            for i in delete:
                print(f"{GRAY}[-] {sys.argv[2]}:{i} is closed")
            ports = new_ports

else:
    if open_port(sys.argv[1], sys.argv[2]):
        print(f"{GREEN}[+] {sys.argv[1]}:{sys.argv[2]} is open")
    else:
        print(f"{GRAY}[-] {sys.argv[1]}:{sys.argv[2]} is close")