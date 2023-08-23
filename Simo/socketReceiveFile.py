# python socketReceiveFile.py
# terminaalissa: pip3 install tqdm
# https://www.thepythoncode.com/article/send-receive-files-using-sockets-python?utm_content=cmp-true


import socket
import tqdm
import os
import time
from PyQt5 import QtWidgets as qtw


def RecvFileViaIP(port = 5001, sekuntia = 10, kohdeKansio = "C:/Tekstit"):
    # device's IP address
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = port
    # receive 4096 bytes each time
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"
    
    # create the server TCP socket
    s = socket.socket()

    # bind the socket to our local address
    s.bind((SERVER_HOST, SERVER_PORT))

    # laita kotihakemisto talteen ja siirry kohdekansioon
    kotiKansio = os.getcwd()
    # print ("socketReceiveFile kotiKansio:", kotiKansio)
    # print ("socketReceiveFile kohdeKansio:", kohdeKansio)
    os.chdir(kohdeKansio)
    # tyoKansio = os.getcwd()
    # print ("socketReceiveFile tyokansio:", tyoKansio)

    
    # enabling our server to accept connections
    # 5 here is the number of unaccepted connections that
    # the system will allow before refusing new connections
    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    s.settimeout(sekuntia)
    client_socket = ""
    try:
        # accept connection if there is any
        # print ("try")
        client_socket, address = s.accept() 
    except socket.timeout:
        # print("except timeout")
        pass        
    else:    
        # print("else")
        # if below code is executed, that means the sender is connected
        print(f"[+] {address} is connected.")
        # receive the file infos
        # receive using client socket, not server socket
        received = client_socket.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
        # remove absolute path if there is
        filename = os.path.basename(filename)
        # convert to integer
        filesize = int(filesize)

        # start receiving the file from the socket
        # and writing to the file stream
        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
            while True:
                # read 1024 bytes from the socket (receive)
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:    
                    # nothing is received
                    # file transmitting is done
                    break
                # write to the file the bytes we just received
                f.write(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))
        # close the client socket
        client_socket.close()
    if client_socket == "":
        qtw.QMessageBox.information(None, 'IP-osoitteesi odottaa viestiä', \
            f"Viestiä ei saapunut {sekuntia} sekunnissa")

    os.chdir(kotiKansio)
    # print("seuraavaksi klosaa server socket")
    # close the server socket
    s.close()

if __name__=='__main__':
    app = qtw.QApplication([])
    kotisivu = RecvFileViaIP()
    app.exec_()


