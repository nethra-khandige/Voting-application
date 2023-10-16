import socket 
from tkinter import *
from tkinter import font
from tkinter import ttk

  
HOST = '10.30.203.237' # IP address of the server
PORT = 5000 


class GUI:
    def __init__(self):
        self.first()
    def first(self):
        self.Window = Tk()
        self.Window.withdraw()
        
        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300,background="#2e1630")
        
        self.pls=Label(self.login,text="Please enter your voter ID",justify=CENTER,font="Helvetica 13 bold")
        self.pls.place(relheight=0.15,relx=0.2,rely=0.07)

        self.labelVoterID = Label(self.login,text="Voter ID: ",font="Helvetica 13 bold")
        self.labelVoterID.place(relheight=0.2,relx=0.1,rely=0.2)
        
        self.voterID=Entry(self.login,font="Helvetica 13 bold")# for entering voterID
        self.voterID.place(relwidth=0.4,relheight=0.12,relx=0.35,rely=0.2)
        
        #set focus of cursor
        self.voterID.focus()
        
        self.go=Button(self.login,text="Continue",font="Helvetica 13 bold",command=lambda:self.goAhead(self.voterID.get()))#continue button
        self.go.place(relx=0.4,rely=0.55)
        self.Window.mainloop()
    
    #to verify ID and then go ahead if present in the list
    def goAhead(self,ID):
        self.receive()
    
    #main layout 
    def layout(self,ID):
        self.login.destroy()
        self.ID=ID

        self.Window.deiconify()#for the window to appear
        self.Window.title("Voter App")
        self.Window.resizable(width=True,height=True)
        self.Window.geometry("300x300")
        self.Window.configure(background="#f5c4ee")
        self.labelHead = Label(self.Window,text=self.ID,bg="#f5c4ee",justify=CENTER,font="Helvetica 13 bold",pady=5)
        self.labelHead.place(relwidth=1)
        
        self.BJP=Button(self.Window,text="BJP",font = "bold" ,bg="#43a8c4",bd = "2",command=lambda:self.BJPVote())
        self.BJP.pack(pady=10)
        self.CONGRESS=Button(self.Window,text="CONGRESS",font = "bold",bg="#43a8c4",bd = "2",command=lambda:self.CONGRESSVote())
        self.CONGRESS.pack(pady=10)
        self.JDS=Button(self.Window,text="JDS",font = "bold",bg="#43a8c4",bd = "2",command=lambda:self.JDSVote())
        self.JDS.pack(pady=10)
        self.NOTA=Button(self.Window,text="NOTA",font = "bold",bg="#43a8c4",bd = "2",command=lambda:self.notaVote())
        self.NOTA.pack(pady=10)
        
    
    def BJPVote(self):
        client_socket.send("BJP".encode())
        response=client_socket.recv(1024)
        print(response) 
        self.Window.destroy()
        return
    def CONGRESSVote(self):
        client_socket.sendall("CONGRESS".encode())
        response=client_socket.recv(1024)
        print(response) 
        self.Window.destroy()
        return
    def JDSVote(self):
        client_socket.sendall("JDS".encode())
        response=client_socket.recv(1024)
        print(response)
        self.Window.destroy()
        return 
    def notaVote(self):
        client_socket.sendall("NOTA".encode())
        response=client_socket.recv(1024)
        print(response)
        self.Window.destroy()
        return 
    
    #receiving info from server
    def receive(self):
        while True:
            try:
                message=client_socket.recv(1024).decode()
                print(message)
                if message=="Voter ID":
                    client_socket.send(self.voterID.get().encode())
                elif message=="Valid":
                    self.layout(self.voterID.get())
                    break
                elif message=="Invalid ID":
                    print("Invalid Client")
                    self.login.destroy()
                    # self.invalid()
                    self.Window.destroy()
                    client_socket.shutdown(client_socket.SHUT_RDWR)
                    client_socket.close()
                    quit()
                    # self.first()
                    break
                
                else:
                    print("Done!")
                    break
            except:
                print("Please re-enter")
                client_socket.close()
                break
        return


for i in range(7):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    g=GUI()
    client_socket.close()

