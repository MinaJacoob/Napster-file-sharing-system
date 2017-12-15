import pickle
from socket import *
import os
import CONST
import threading
import string
from random import *
from Client_server_data_holder import *
import threading


class Client:
    no_of_connections = 0
    def __init__(self, port, HOST='localhost'):
        self.host = HOST  # this machine
        self.port = port  # port that this client will listen to
        self.sock = socket()  # socket for incoming calls
        self.sock.bind((self.host, self.port))  # bind socket to an address
        self.sock.listen(5)  # max num connections
        self.clientData = ClientSeverDataHolder(HOST, CONST.PORT)

    def sendTo(self, host, port, data):  # file requestor
        sock = socket()
        sock.connect((host, port))  # connect to server (blocking call)
        sock.send(data)  # send some data
        sock.close()

    def reciveConnections(self):  # file download request reciever
        print "start listening on port: ", self.port
        print "Number of connected peers = 0"
        while True:
            conn, addr = self.sock.accept()
            self.no_of_connections = self.no_of_connections + 1
            print "Number of connected peers = ", self.no_of_connections
            print "GOT Connection from a client from : ",addr[0]," on port : ",addr[1]
            file_path = conn.recv(1024)
            file_list = file_path.split('/')
            file = file_list[-1]
            out_file = os.getcwd()
            final_path = out_file + "/"+ self.generate_file_name() +".txt"
            with open(file, "rb") as in_file:
                with open(final_path, "wb") as out_file:
                    out_file.write(in_file.read())
            information_message = "Download complete at " + out_file.name
            print information_message
            conn.close()

    #listen_thread = threading.Thread(target=reciveConnections)
    #connect_to_server = threading.Thread(target=__init__())

    def registerfiles(self, list_of_files):
        final_list = list_of_files[3]
        final_list.insert(0, list_of_files[2])
        final_list.insert(0, list_of_files[1])
        reply = self.clientData.create(final_list)  # create new list and fill it with files
        return reply

    def downloadFile(self):
        peer_port = int(raw_input("Enter peer port : "))
        file_path = raw_input("Enter file path : ")
        self.sendTo(HOST, peer_port, file_path)

    def searchForFile(self, file_name):
        print file_name
        result = self.clientData.search(file_name)
        if result == "0":
            print "file not found!"
        else:
            print result[0]
            print result[1]

    def generate_file_name(self):
        name = random = ''.join([choice(string.ascii_letters + string.digits) for n in xrange(10)])
        return name