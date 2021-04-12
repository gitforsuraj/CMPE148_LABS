from socket import *
import base64
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 587)

# Create socket called client_socket and establish a TCP connection with mailserver
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(mailserver)
recv = client_socket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
client_socket.send(heloCommand.encode())
recv1 = client_socket.recv(1024).decode()
print(recv1)

tls_command = "STARTTLS\r\n"
client_socket.send(tls_command.encode())
recv2 = client_socket.recv(1024).decode()
print(recv2)
client_socket = ssl.wrap_socket(client_socket)

username = input('Enter email: ')
password = input('Enter password: ')
base64_str = ("\x00" + username + "\x00" + password).encode()
base64_str = base64.b64encode(base64_str)
auth_msg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
client_socket.send(auth_msg)
recv3 = client_socket.recv(1024).decode()
print(recv3)

# Send MAIL FROM command and print server response.
mail_from_command = 'MAIL FROM:<patel.k.suraj@gmail.com>\r\n'
client_socket.send(mail_from_command.encode())
recv4 = client_socket.recv(1024).decode()
print(recv4)

# Send RCPT TO command and print server response.
mail_from_command = 'RCPT TO:<patel.k.suraj@gmail.com>\r\n'
client_socket.send(mail_from_command.encode())
recv5 = client_socket.recv(1024).decode()
print(recv5)

# Send DATA command and print server response.
client_socket.send('DATA\r\n'.encode())
recv6 = client_socket.recv(1024).decode()
print(recv6)

# Send message data.
client_socket.send(msg.encode())

# Message ends with a single period.
client_socket.send(endmsg.encode())
recv7 = client_socket.recv(1024)
print("Response " + recv7.decode())

# Send QUIT command and get server response.
client_socket.send('QUIT\r\n'.encode())
recv8 = client_socket.recv(1024)
print(recv8.decode())
client_socket.close()
