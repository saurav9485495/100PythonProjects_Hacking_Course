import socket

target=input("enter target ip address")
port_min=int(input("enter port_min"))
port_max=int(input("enter port_max"))
ports = range(port_min,port_max)

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[OPEN] Port {port}")
    else:
    	print("port is closed")
    
    s.close()
