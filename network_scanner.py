#!/usr/bin/env python

import scapy.all as scapy

import argparse

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=10, verbose=False)[0]
    clients = []
    for e in answered:
        client_dict = {"ip": e[1].psrc, "mac": e[1].hwsrc}
        clients.append(client_dict)
    return clients

def printscan(clients):
    print("\n+-----------------------+-------------------------+\n|IP\t\t\t| MAC Adress              |\n+-----------------------+-------------------------+")
    for e in clients:
        print("|"+e["ip"]+" \t\t| "+e["mac"]+"       |")
        print("+-----------------------+-------------------------+")
    print("\n")

def get_arguments():
    # parser pour passer des arguments kima n7abo f cmd
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--ip", dest="ip", help="L'adress ip li nl9aw mac t3ha")
    options = parser.parse_args()
    if not options.ip:
        parser.error("Nsit tmed ama ip kho dir --help w chouf")
    return options
try:

    printscan(scan(get_arguments().ip))
except KeyboardInterrupt:

    print("\n [-] rak 3abzt ctrl+c dok nquiti...   BOOM. lol ")

