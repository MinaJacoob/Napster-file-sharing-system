
class ClientFileObj:
    def __init__(self, host, port, file_path, files = []):  # -
        self.host = host  # address of server hosting lists
        self.port = port  # the port it will be listening to
        self.file_path = file_path # the path of the file to be sent
        self.file = files  # list holds files names
