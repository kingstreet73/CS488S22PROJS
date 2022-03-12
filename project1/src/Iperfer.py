import socket
import sys
import time #https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
#VERSION 321091029301230129 COMPLETE, SIMPLIFIED REDO WITH NO SERVER, NO MODULES/FUNCTIONS, ONLY FOR AUTOGRADER
#Create and confirm 3 arguments we want passed in - hostname, port, time

if (len(sys.argv) !=4):
    print("Error: missing or additional arguments")
    exit()

server_Hostname = str(sys.argv[1])
server_Port = int(sys.argv[2])
server_Time = int(sys.argv[3])
#confirm server_Port is in range
if((server_Port < 1024) or (server_Port > 65535)):
    print("Error: port number must be in the range 1024 to 65535")
    exit()

#-------------------------------------3 ARGS CREATED AND CHECKED->>>>>---SEND DATA, CALCUALTE, RETURN DATA+BANDWIDTH-----------------------------------------------------
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
address = (server_Hostname, server_Port)
#           connection will be     IPV4(INET)         TCP(STREAM)                       -> IPV6(INET6)  UDP(DGRAM)
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
   


   


