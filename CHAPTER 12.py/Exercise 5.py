# (Advanced) Change the socket program so that it only shows data
# after the headers and a blank line have been received. Remember that recv receives
# characters (newlines and all), not lines.

import socket

url = input("Enter URL: ")

try:
    parts = url.split('/')
    host = parts[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    mysock.send(cmd.encode())

    header = True

    while True:
        data = mysock.recv(512)

        if len(data) < 1:
            break

        if header:
            pos = data.find(b'\r\n\r\n')

            if pos != -1:
                header = False
                data = data[pos + 4:]
            else:
                continue

        print(data.decode(), end='')

    mysock.close()

except:
    print("Error: Invalid or unavailable URL")