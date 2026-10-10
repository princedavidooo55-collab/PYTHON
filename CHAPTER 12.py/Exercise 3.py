# Use urllib to replicate the previous exercise of (1) retrieving the
# document from a URL, (2) displaying up to 3000 characters, and (3) counting the
# overall number of characters in the document. Don’t worry about the headers for
# this exercise, simply show the first 3000 characters of the document contents.

import urllib.request

url = input("Enter URL: ")

try:
    fhand = urllib.request.urlopen(url)

    count = 0
    total = 0

    for line in fhand:
        text = line.decode()
        total = total + len(text)

        if count < 3000:
            print(text, end='')

            count = count + len(text)

    print("\nTotal characters:", total)

except:
    print("Error: Invalid or unavailable URL")