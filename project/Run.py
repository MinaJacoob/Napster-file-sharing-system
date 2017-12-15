'''
author: Mina Mofreh Tawfik
ID: 20510667
Department: Computer Science
sec: wed 8:10 AM
'''


return_list = []


'''
function to convert given string of multiple files to a list of files 
as it splits the string on comma
'''
def Conver_fileString_to_list(files):
    list_of_files = files.split(',')
    Trimer = lambda x: x.strip()   #defining lambda function to trim string
    list_trimed = list(map(Trimer,list_of_files))  #applying function
    return list_trimed

def get_client_config(state):
   if state == '1': #register files
       peer_port = raw_input("Enter your port : ")
       file_directory = raw_input("Please enter file directory : ")
       files_names = raw_input("Enter file names, Please separate with comma for multiple files\n=>")
       files_list = Conver_fileString_to_list(files_names)
       return_list.append(peer_port)
       return_list.append(file_directory)
       return_list.append(files_list)
       return_list.append("register")
   elif state == '2': # search files
       search_file_name = raw_input("Enter file name : ")
       return_list.append(search_file_name)
       return_list.append("search")
   elif state == '3':  # download files
         return_list.append("download")


def run_peer():

    print "----------------------------------------"
    print "|Welcome to Napster File Sharing System.|"
    print "----------------------------------------\n"

    ip = raw_input("Enter (l) for localhost or press any key to enter your own IP : ")
    if (ip == 'l' or ip == 'L'):
        ip = 'localhost'
        print "your IP is ", ip, " (127.0.0.1)"
    else:
        ip = raw_input("Enter your IP : ")
    return_list.append(ip)
    print "--------------------------------"
    state = raw_input("Choose\n(1)Register Files.\n(2)Search Files\n(3)Download Files\n(4)Act as a Server\n=>")
    if state == '1' or state == '2' or state == '3': # i.e act as a peer
         get_client_config(state)
    elif state == '4':  # i.e act as a server
        port = raw_input("Enter the port which you will listen on : ")
        return_list.append(port)
        return_list.append("server")

    return return_list


