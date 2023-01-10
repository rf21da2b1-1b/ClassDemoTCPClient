#
# TCP client efter bogen (side 191)
#

from socket import *

# konstant
serverPort = 12001
serverName = 'localhost'    # server kører på den lokale maskine

# opretter socket objekt til klienten
clientSocket = socket(AF_INET, SOCK_STREAM)         # lave TCP socket
clientSocket.connect((serverName,serverPort))       # opretter forbindelse til serverName med port serverPort

#Indlæser sætning fra skærmen(tasteturet)
sentence = input('Input lowercase sentence ')
clientSocket.send(sentence.encode())            # sender tekst line til server

# modtager svaret
answerSentence = clientSocket.recv(2048).decode()   # modtager svar
print (f'From Server: {answerSentence}')
clientSocket.close()                            # lukker forbindelsen