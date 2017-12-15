from CONST import *
from socket import *
import pickle
import threading


class IndexServer:
    no_of_connections = 0  # static variable to count connected peers

    def __init__(self, port=PORT, HOST='localhost'):
        self.host = HOST  # server host
        self.port = port  # the port server will listen to
        self.sock = socket()  # socket for incoming calls
        self.sock.bind((self.host, self.port))  # bind socket to an address
        self.sock.listen(5)  # max num of connections
        self.listOfFiles = {}  # init: no lists to manage
        print "[*] Starts Listening on", self.host, ":", self.port

    def run(self):
        #self.s = threading._RLock()
        #self.rw = threading._Semaphore(value=1)
        #self.mutex = threading._Semaphore(value=1)
        while True:
            print "no of connected peers = ", self.no_of_connections
            (conn, addr) = self.sock.accept()  # accept incoming call
            print "[*] Got a connection from ", addr[0], ":", addr[1]
            #self.s.acquire(self.mutex)
            self.no_of_connections = self.no_of_connections + 1
            #if self.no_of_connections == 1:
            #    self.s.acquire(self.rw)
            #self.s.release(self.mutex)
            print "no of connected peers = ", self.no_of_connections
            data = conn.recv(1024)  # fetch data from client
            request = pickle.loads(data)  # unwrap the request

            ########################################################################
            if request[0] == REGISTER_FILE:  # create a list to files
                #self.s.acquire(self.rw)   #wait()
                listID = len(self.listOfFiles) + 1  # allocate file_list_id
                self.listOfFiles[listID] = []  # initialize to empty
                conn.send(pickle.dumps([listID, "files has been uploaded successfully, Good Bye."]))  # return ID
                data = request[1]
                self.listOfFiles[listID] = data
                print self.listOfFiles
                #self.s.release(self.rw)  #signal()

            ########################################################################

            elif request[0] == SEARCH:
                file_name = request[1]
                str1 = "Searching for file (" + file_name + ")..."
                str2 = self.search_files(file_name)
                list_result = [str1, str2]
                conn.send(pickle.dumps(list_result))
                print file_name, " path forwarded to client successfully."
                #self.s.acquire(self.mutex)
                self.no_of_connections = self.no_of_connections - 1
                #if self.no_of_connections == 0:
                #    self.s.release(self.rw)
                #self.s.release(self.mutex)

            ########################################################################
    def search_files(self, file_name):
        print "Searcing for", file_name, "..."
        for key, val in self.listOfFiles.iteritems():
            for v in val:
                if file_name == v:
                    file_path = "file found on:\n peer port = " + str(val[0]) + ", file path = " + val[1] + "/" + v
                    return file_path
