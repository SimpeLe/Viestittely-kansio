# python socketSendFile.py
# terminaalissa: pip3 install tqdm

import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step
 
# the ip address or hostname of the server, the receiver
# tarkasta cmd komennolla ipconfig
# host = "192.168.10.48" #vanha kone
host = "192.168.10.40" #kannettava
#host = "www.python.org" #toimii
# the port, let's use 5001 (tai 5000 tai 5500 tai 65432)
port = 5001
# port = 80 #toimii
# the name of file we want to send, make sure it exists
filename = "Message.txt"
# get the file size
filesize = os.path.getsize(filename)

# create the client socket
s = socket.socket()

# Connecting to the server:
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()





