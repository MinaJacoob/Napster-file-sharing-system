import pickle
from socket import *
from CONST import *


class ClientSeverDataHolder:
    def __init__(self, host, port,listID=None):
        self.host = host  # address of server hosting lists
        self.port = port  # the port it will be listening to
        self.listID = listID  # the list for which this stub is meant

    def sendrecv(self, message):
        sock = socket()  # create a socket
        sock.connect((self.host, self.port))  # connect to server
        sock.send(pickle.dumps(message))  # send some data
        result = pickle.loads(sock.recv(3024))  # receive the response
        sock.close()  # close the connection
        return result

    def create(self,data):
        assert self.listID == None  # -
        reply_server = self.sendrecv([REGISTER_FILE,data])
        self.listID = reply_server[0]
        reply = reply_server[1]
        return reply

    def search(self,name):
        search_result = self.sendrecv([SEARCH,name])
        if search_result[1] == None:
           return "0"
        else:
            return search_result