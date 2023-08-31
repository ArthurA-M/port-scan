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

delta = 0

if sys.argv[0] != "port_scan.py":
    delta = 1

if sys.argv[1 - delta] == "all": #affiche l'état de tous les ports demandés
    for i in range(int(sys.argv[3 - delta]),int(sys.argv[4 - delta])+1):
        if open_port(sys.argv[2 - delta], i):
            print(f"{GREEN}[+] {sys.argv[2 - delta]}:{i} is open")
        else:
            print(f"{GRAY}[-] {sys.argv[2 - delta]}:{i} is close")

elif sys.argv[1 - delta] == "open": #affiche les ports ouverts parmis ceux demandés
    for i in range(int(sys.argv[3 - delta]),int(sys.argv[4 - delta])+1):
        if open_port(sys.argv[2 - delta], i):
            print(f"{GREEN}[+] {sys.argv[2 - delta]}:{i} is open")

elif sys.argv[1] == "listen": #affiche les changement d'états des ports
    ports = [i for i in range(int(sys.argv[3 - delta]),int(sys.argv[4 - delta])+1) if open_port(sys.argv[2 - delta], i)]
    while True:
        new_ports = [i for i in range(int(sys.argv[3 - delta]),int(sys.argv[4 - delta])+1) if open_port(sys.argv[2] - delta, i)]
        if ports != new_ports:
            add = [i for i in new_ports if i not in ports]
            delete = [i for i in ports if i not in new_ports]
            for i in add:
                print(f"{GREEN}[+] {sys.argv[2 - delta]}:{i} is opened")
            for i in delete:
                print(f"{GRAY}[-] {sys.argv[2 - delta]}:{i} is closed")
            ports = new_ports

else: #affiche l'état d'un port précis
    if open_port(sys.argv[1 - delta], sys.argv[2 - delta]):
        print(f"{GREEN}[+] {sys.argv[1]}:{sys.argv[2 - delta]} is open")
    else:
        print(f"{GRAY}[-] {sys.argv[1]}:{sys.argv[2 - delta]} is close")