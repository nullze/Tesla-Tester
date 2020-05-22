import socket
from os import system, name
from telnetlib import Telnet

# make it clean
def clear():

    # winduwz
    if name == 'nt':
        _ = system('cls')

    # nix
    else:
        _ = system('clear')

#UDP_IP = ''
#UDP_PORT = 4321
#MESSAGE = ''
#MESSAGE = \x0b\xd3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00

#clear the garbage
clear()

#plug
print('-------------------------------------------------------------------')
print('-------------------------------------------------------------------')
print('*****[[ Safekeep Security: Tesla UDP Internal Network Test ]]******')
print('-------------------------------------------------------------------')
print('-------------------------------------------------------------------\n')

UDP_IP = '192.168.90.255'
UDP_PORT = 63277
print ("UDP target IP:", UDP_IP, "\n")
print ("UDP target port:", UDP_PORT, "\n")

while True:

    print('--------Please select one of the following:----------')
    print('0: Telnet Test')
    print('1: 24474e474c4c2c2c2c2c2c2c562c4e2a37410d0a')
    print('2: 12131025000000000000')
    print('3: 12132035000000000000')
    print('4: 12133045000000000000')
    print('5: 12134055000000000000')
    print('6: 12135065000000000000')
    print('7: 12136075000000000000')
    print('8: 12137085000000000000')
    print('9: 12138095000000000000')
    print('10: 121390a5000000000000')
    print('11: 1213a0b5000000000000')
    print('12: 1213b0c5000000000000')
    print('13: 1213c0d5000000000000')
    print('14: 1213d0e5000000000000')
    print('15: 1213e0f5000000000000')
    print('16: 1213f005000000000000')
    print('17: 13bb1e0f000000000000')
    print('18: 13d89f04000000000000')


    selection = input('Please select a number:')

    if selection == '0':
        try:
            with Telnet('192.168.90.104', 23) as tn:
                tn.interact('genealogy 3\r\n')
                print('Successful: Sent Telnet to 192.168.90.104\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '1':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x24\x47\x4e\x47\x4c\x4c\x2c\x2c\x2c\x2c\x2c\x2c\x56\x2c\x4e\x2a\x37\x41\x0d\x0a', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 24474e474c4c2c2c2c2c2c2c562c4e2a37410d0a\n\n')
            print(' ')
        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '2':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x12\x13\x10\x25\x00\x00\x00\x00\x00\x00', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 12131025000000000000\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '3':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x12\x13\x20\x35\x00\x00\x00\x00\x00\x00', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 12132035000000000000\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '4':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x12\x13\x30\x45\x00\x00\x00\x00\x00\x00', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 12133045000000000000\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '5':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x12\x13\x40\x55\x00\x00\x00\x00\x00\x00', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 12134055000000000000\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '6':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x12\x13\x50\x65\x00\x00\x00\x00\x00\x00', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 12135065000000000000\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '7':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x12\x13\x60\x75\x00\x00\x00\x00\x00\x00', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 12136075000000000000\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '8':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x12\x13\x70\x85\x00\x00\x00\x00\x00\x00', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 12137085000000000000\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '9':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x12\x13\x80\x95\x00\x00\x00\x00\x00\x00', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 12138095000000000000\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '10':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x12\x13\x90\xa5\x00\x00\x00\x00\x00\x00', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 121390a5000000000000\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '11':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x12\x13\xa0\xb5\x00\x00\x00\x00\x00\x00', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 1213a0b5000000000000\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '12':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x12\x13\xb0\xc5\x00\x00\x00\x00\x00\x00', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 1213b0c5000000000000\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass

    elif selection == '13':
        try:
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # stupid permissions fix for linux
            sock.sendto(b'\x12\x13\xc0\xd5\x00\x00\x00\x00\x00\x00', (UDP_IP, UDP_PORT))
            clear()
            print('Successful: Sent 1213c0d5000000000000\n\n')

        except sock.error as e:
            print('Error: creating socket: %s' + e)
            pass


