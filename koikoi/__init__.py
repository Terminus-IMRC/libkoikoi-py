import socket

class koikoi():

	byteorder = 'little'

	CMD_INVALID = (0).to_bytes(1, byteorder = byteorder)
	CMD_HELLO = (1).to_bytes(1, byteorder = byteorder)

	def __init__(self):
		pass

	def connect(self, sockname):
		s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
		s.connect(sockname)
		self.sock = s

	def disconnect(self):
		s = self.sock
		s.shutdown(socket.SHUT_RDWR)
		s.close()
		del(self.sock)

	def send(self, data):
		s = self.sock
		return s.send(data)

	def recv(self, maxlen):
		s = self.sock
		return s.recv(maxlen)

	def i2c(self, i, l = 1):
		return i.to_bytes(l, byteorder = self.byteorder)

	def c2i(self, code, l = 1):
		return code.from_bytes(l, byteorder = self.byteorder)
