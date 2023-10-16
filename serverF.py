import socket

HOST = '10.30.201.176' # IP address of the server
PORT = 5000 # Port number to listen on

voterID=[1,2,3,4,5]
candidates = {'BJP':0,'CONGRESS':0,'JDS':0,'NOTA':0}



def check_ID(client_socket):
    while True:
        client_socket.send("Voter ID".encode())
        voterid=client_socket.recv(1024).decode() # Receive ID from the client
        if not voterid: break
        # Parse the request and update the vote counts
        # voterid = ID.decode()#receive voterID and the candidate chosen
        #print(voterid)
        #print(candidate)   
        voterid=int(voterid)
        #print("Ho3")
        if voterid not in voterID:#checking if voterID is valid
            client_socket.send("Invalid ID".encode())
            client_socket.close()
            client_socket, client_address = server_socket.accept()
            check_ID(client_socket)        
            client_socket.close()
        else:
            print("Voter ID is:",voterid)
            client_socket.send("Valid".encode())
            candidate = client_socket.recv(1024).decode()
            count(client_socket,voterid,candidate)
            return
        return
    
def count(client_socket,voterid,candidate):
    #candidate = client_socket.recv(1024).decode()
    if candidate in candidates:
        candidates[candidate] += 1
        voterID.remove(voterid)
        print("Remaining voters:",voterID)
        client_socket.send("Vote casted.Thank you!".encode())
            #quit()
    else:
        client_socket.sendall(b'ERROR')
           # quit()
    return

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1) # Listen for incoming connections
print("Listening on Host:",HOST,"on Port:",PORT)

while True:
    for i in range(5):
        client_socket, client_address = server_socket.accept()
        check_ID(client_socket)        
        client_socket.close()  
        print("connection Closed")
    keymax = max(zip(candidates.values(),candidates.keys()))[1]
    print("The winner is:"+keymax)
    quit()
