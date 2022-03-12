from multiprocessing.sharedctypes import Value
import socket
import sys
import time #https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution

#constants
chunk_Size = 1000
min_Port = 1024
max_Port = 65535

#Create and confirm 3 arguments we want passed in - hostname, port, time
def client_args():
    args = sys.argv[1,2,3]

    server_Hostname = args[0]
    server_Port = args[1]
    server_Time = args[2]

    if len(args) !=3:
        print("Error: missing or additional arguments")
        exit()
    if len(args) == 2:
        server_args()
        exit()
    if len(args) == 3:
    #confirm server_Hostname is real
        try:
            socket.inet_aton(server_Hostname)
        except OSError:
            print("Error missing or additional arguments")

    #confirm server_Port is in range
        try:
            server_Port = int(server_Port)
            if server_Port < min_Port or server_Port > max_Port:
                print("Error: port number must be in the range {} to {}").format(min_Port, max_Port)
                exit()
            # confirm time is valid (float for import time)
            server_Time = float(server_Time)
        except ValueError:
            print("Error: missing or additional arguments")
            exit()

    return server_Hostname, server_Port, server_Time
#-------------------------------------3 ARGS CREATED AND CHECKED->>>>>---SEND DATA, CALCUALTE, RETURN DATA+BANDWIDTH-------------------------------------------------------

def server_args():
    args = sys.argv[1,2]
    
    s_tag = args[0]
    listen_Port = args[1]

    #check if -s is set as tag
    s_tag = str(s_tag)
    if s_tag != "-s":
        print("Error: missing or additional arguments")
        exit()

    try:
        listen_Port = int(listen_Port)
        if listen_Port < min_Port or listen_Port > max_Port:
            print("Error: port number must be in the range {} to {}").format(min_Port, max_Port)
            exit()
    except ValueError:
        print("Error: missing or additional arguments")
        exit()

    return listen_Port
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


def server_Run(listen_port):
    init_Chunk = bytes(chunk_Size)
    
    #create server socket
    server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind port with socket
    server_Socket.bind(listen_port)
    #wait for 1 minimum client
    server_Socket.listen(1)
    #create connection socket
    connection_socket, addr = server_Socket.accept()
    while 1:
        data = server_Socket.recv(init_Chunk)

    connection_socket.close()
    
    return data

    



def client_Run(server_Hostname, server_Port, server_SetTime):
    init_Chunk = bytes(chunk_Size)
    counter = 0
    #           connection will be     IPV4(INET)         TCP(STREAM)                       -> IPV6(INET6)  UDP(DGRAM)
    client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_Socket.connect((server_Hostname,server_Port))
    #calc run time and bytes sent- close connection when done
    init_Time = time.time()
    while time.time() - init_Time < server_SetTime:
        client_Socket.sendall(init_Chunk)
        counter += 1
    iperf_runtime = time.time() - init_Time
    client_Socket.close
    #calc rate
    send_Rate = (counter * 8 / 1000) / iperf_runtime

    print("sent={} KB rate={} Mbps".format(counter, send_Rate))
    exit()
   


   


