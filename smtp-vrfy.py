#!/usr/bin/env python3

# Description: Run VRFY command against known SMTP server
# Usage: vrfy.py IP USERNAME

import socket
import sys

if len(sys.argv) != 3:
    print("Usage: vrfy.py IP USERNAME")
    sys.exit(1)

SMTP_PORTNO = 25
MSGLEN = 1024

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to mail server
connect = s.connect((sys.argv[1], SMTP_PORTNO))

# Banner request
banner = s.recv(MSGLEN).decode()

print(banner)

# Verify a user with VRFY
s.send(str.encode('VRFY {}\r\n'.format(sys.argv[2])))

# Receive VRFY response
res = s.recv(MSGLEN).decode()

print(res)

# Close connection
s.close()
