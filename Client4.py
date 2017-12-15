from Client import *
from Client_server_data_holder import *
from CONST import *
from Run import *
from multiprocessing import Process
from thread import *

peer_state = run_peer()

if peer_state[-1] == "server":  # if peer is server then do nothing except listining
     client1 = Client(int(peer_state[1]))  # create client
     data = client1.reciveConnections()  # block until data is sent
     print data

else:
    client1 = Client(CLIENT1Port)  # create client
    dbClient1 = ClientSeverDataHolder(HOST, PORT)  # create reference
    if peer_state[-1] == "register":  # client wants to register files
        reply = client1.registerfiles(peer_state)  # create new list and fill it with files
        print reply

    elif peer_state[-1] == "download": #client want to download files
        client1.downloadFile()

    elif peer_state[-1] == "search":  # client wants to search for a file
        client1.searchForFile(peer_state[1])
