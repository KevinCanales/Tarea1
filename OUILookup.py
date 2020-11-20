#!/usr/bin/env python
#Si se guarda
import sys
import socket
net = ""
netID = ""
ipLocal = ""
ipX = ""
if len(sys.argv) >= 2 and len(sys.argv) <= 3:
    if sys.argv[1] == "--help":
        print("Use: ./OUILookup --ip <IP> | --mac <IP>")
        print("--ip : especificar la IP del host a consultar")
        print("--mac : especificar la dirección MAC a consultar")
    elif sys.argv[1] == "--ip":
        ip = sys.argv[2]
        ipLocal = socket.gethostbyname(socket.gethostname())
        for i in ipLocal:
            if i != ".":
                net = net + i
            else:
                break
        if int(net) >= 0 and int(net) <= 127:
            netID = net + ".0.0.0"
            ip = ip.split(sep=".")
            for i in ip:
                if i != ".":
                    ipX = ipX + i
                else:
                    break
            ipX = ipX + ".0.0.0"
            if ipX == netID:
                print("La ip es valida")
            else:
                print("La direccion ip no pertenece a la red local")
            

        elif int(net) >= 128 and  int(net) <= 191:
            ipLocal = ipLocal.split(sep=".")
            a = 0
            for i in ipLocal:
                if a != 2:
                    netID = netID + i + "."
                    a = a + 1
                else:
                    break
            netID = netID + "0.0"
            ip = ip.split(sep=".")
            b = 0
            for i in ip:
                if b != 2:
                    ipX = ipX + i + "."
                    b = b + 1
                else:
                    break
            ipX = ipX + "0.0"
            if ipX == netID:
                print("La ip ingresada es valida")
            else:
                print("La ip ingresada no pertenece a la red local")
        elif int(net) >= 192 and int(net) <= 223:
            ipLocal = ipLocal.split(sep=".")
            a=0
            for i in ipLocal:
                if a != 3:
                    netID = netID + i + "."
                    a = a + 1
                else:
                    break
            netID = netID + "0"
            ip = ip.split(sep=".")
            b = 0
            for i in ip:
                if b != 3:
                    ipX = ipX + i + "."
                    b = b + 1
                else:
                    break
            ipX = ipX + "0"
            
            if ipX == netID:
                print("La ip ingresada es valida")
            else:
                print("La ip ingresada no pertenece a la red local")

    elif sys.argv[1] == "--mac":
        mac = sys.argv[2]

        print(mac)
    else:
        print("Use: ./OUILookup --ip <IP> | --mac <IP> | --help")
        print("--ip : especificar la IP del host a consultar")
        print("--mac : especificar la dirección MAC a consultar")
        print("--help : muestra este mensaje y cierra")
else:
    print("Use: ./OUILookup --ip <IP> | --mac <IP> | --help")
    print("--ip : especificar la IP del host a consultar")
    print("--mac : especificar la dirección MAC a consultar")
    print("--help : muestra este mensaje y cierra")