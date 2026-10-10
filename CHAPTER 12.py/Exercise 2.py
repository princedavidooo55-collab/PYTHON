# Change your socket program so that it counts the number of characters it has received
# and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of
# characters and display the count of the number of characters at the end of the document.

import socket

url = input("Enter URL: ")

try:
    parts = url.split('/')
    host = parts[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    mysock.send(cmd.encode())

    count = 0
    total = 0

    while True:
        data = mysock.recv(512)

        if len(data) < 1:
            break

        total = total + len(data)

        if count < 3000:
            print(data.decode(), end='')

            count = count + len(data)

            if count > 3000:
                print(data.decode()[:3000 - (count - len(data))], end='')

    print("\nTotal characters:", total)

    mysock.close()

except:
    print("Error: Invalid or unavailable URL")