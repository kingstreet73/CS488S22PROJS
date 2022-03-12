import socket
import sys
import time #https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution

#constants
chunk_Size = 1000
min_Port = 1024
max_Port = 65535

#Create and confirm 3 arguments we want passed in - hostname, port, time

if len(sys.argv) !=4:
    print("Error: missing or additional arguments")
    exit()

server_Hostname = str(sys.argv[1])
server_Port = int(sys.argv[2])
server_Time = int(sys.argv[3])
server_Hostname = socket.gethostbyname(server_Hostname)


#confirm server_Port is in range
if((server_Port < 1024) or (server_Port > 65535)):
    print("Error: port number must be in the range 1024 to 65535")
    exit()

#-------------------------------------3 ARGS CREATED AND CHECKED->>>>>---SEND DATA, CALCUALTE, RETURN DATA+BANDWIDTH-----------------------------------------------------
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
address = (server_Hostname, server_Port)
init_Chunk = bytearray(1000)
counter = 0
#           connection will be     IPV4(INET)         TCP(STREAM)                       -> IPV6(INET6)  UDP(DGRAM)
client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_Socket.connect(address)
#calc run time and bytes sent- close connection when done
init_Time = time.perf_counter()
while init_Time - time.perf_counter() < server_Time:
    client_Socket.send(init_Chunk)
    counter += 1
    continue
#calc rate
send_Rate = (counter * 8 / 1000) / server_Time

print("sent={} KB rate={} Mbps".format(counter, send_Rate))
client_Socket.close()
   


   


