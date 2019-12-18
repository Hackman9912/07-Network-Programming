import socket

host = 'l10.240.234.166'
mysock=socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.SOCK_STREAM)
addr=(host,9898)
mysock.connect(addr)

try:
	msg=b"hi, this is a test\n"
	mysock.sendall(msg)
except:
	print("Socket error ", e)
finally:
	mysock.close()