import socket
import sys
import time #https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
#VERSION 321091029301230129 COMPLETE, SIMPLIFIED REDO WITH NO SERVER, NO MODULES/FUNCTIONS, ONLY FOR AUTOGRADER
#UPDATE: THIS VERSION WORKS FOR TASKS 1-3, BUT, REALIZED I TOOK OUT MY MAIN EXECUTOR FOR THE MODULAR DESIGN, SO PROBABLY GO BACK TO THAT IF THIS DOESNT WORK WITH SERVER
#Create and confirm 3 arguments we want passed in - hostname, port, time

if (len(sys.argv) != 4) and (len(sys.argv) != 3):
    print("Error: missing or additional arguments")
    sys.exit()

#server part
if (len(sys.argv) == 3):
    if (sys.argv[1] == '-s'):
        port = int(sys.argv[2])
        if((port < 1024) or (port > 65535)):
            print("Error: port number must be in the range 1024 to 65535")
            exit()
        data_sum = 0
        host_name = '127.0.0.1'
        init_Chunk = bytearray(1000)
        #create server socket
        server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #bind port with socket
        server_Socket.bind(host_name, port)
        #wait for 1 minimum client
        server_Socket.listen(1)
        #create connection socket
        connection_socket, addr = server_Socket.accept()
        with connection_socket:
            start_time = time.time()
            while True:
                data = server_Socket.recv(init_Chunk)
                data_sum += 1
                if not data:
                    break
            stop = time.time()
            total_time = start_time - stop
            rate = (data_sum / 125) / total_time
            rate = float("%0.3f" % (rate))
            print("received=" + str(data_sum) + " KB rate=" + str(rate) + " Mbps")

            connection_socket.close()
    else:
        print("Error: missing or additional arguments")
        sys.exit()
    
    

#client part
if (len(sys.argv) == 4):
    if (sys.argv[1] == '-s'):
        print("Error: missing or additional arguments")
        sys.exit()

    server_Hostname = str(sys.argv[1])
    server_Port = int(sys.argv[2])
    server_Time = int(sys.argv[3])
    #confirm server_Port is in range
    if((server_Port < 1024) or (server_Port > 65535)):
        print("Error: port number must be in the range 1024 to 65535")
        exit()

    #-------------------------------------3 ARGS CREATED AND CHECKED->>>>>---SEND DATA, CALCUALTE, RETURN DATA+BANDWIDTH-----------------------------------------------------

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    address = (server_Hostname, server_Port)#           connection will be     IPV4(INET)         TCP(STREAM)                       -> IPV6(INET6)  UDP(DGRAM)
    client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_Socket.connect(address)
    init_Chunk = bytearray(1000)
    counter = 0
    #calc run time and bytes sent- close connection when done
    timer = time.perf_counter()
    while server_Time - timer > 0:
        client_Socket.send(init_Chunk)
        counter += 1
        continue
    #calc rate
    send_Rate = (counter * 8 / 1000) / server_Time

    print("sent={} KB rate={} Mbps".format(counter, send_Rate))
    client_Socket.close()

else:
    print("Error: missing or additional arguments")
    sys.exit()

    


