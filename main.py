class main():
	def __init__(self):
		self.iter = 0

		self.cap = 10

		list = []

		file = open('settings.conf')
		while True:
			line = file.readline()

			if not line:
				break

			list.append(line)
		file.close()

		self.path = list[0][6::][::-1][1::][::-1] + '/'
		
		self.extension = list[1][11::]

		self.messageHandler()

	def merge(self) -> str:
		return self.path + str(self.iter) + self.extension

	def rewriteSettings(self):
		towrite = f"path= {self.path}\nextention= {self.extension}"

		file = open('settings.conf', 'w+')
		file.write(towrite)
		file.close()

	def messageHandler(self):
		print('help for command list')

		run = True

		while run:

			message = input('>>')

			if message.strip() == 'exit':
				run = False
	
			elif 'change' in message:
				if len(message.strip()) == 6:
					print(self.path + self.extension)
	
				else:
					try:
						list = message.split()

						if len(list) == 3:
							if list[1].strip() == 'dir':
								if list[2].strip()[len(list[2].strip())-1] == '/':
									self.path = list[2].strip()

									self.rewriteSettings()

								else:
									self.path = list[2].strip() + '/'

									self.rewriteSettings()

							elif list[1].strip() == 'ext':
								if list[2].strip()[0] == '.':
									self.extension = list[2].strip()

									self.rewriteSettings()

								else:
									self.extension = '.' + list[2].strip() 

									self.rewriteSettings()

					except BaseException:
						print('Error in change!')

			elif 'set' in message:
				try:
					list = message.split()
					if len(list) > 1:
						if list[1] == 'inf':
							self.cap = list[1]
						else:
							self.cap = int(list[1])
					else: 
						print(self.cap)
				except BaseException:
					print('Error in set!')

			elif message.strip() == 'start':
				while True:
					if self.cap == self.iter:
						break

					file = open(self.merge(), 'w+')
					for i in range(10000):
						file.write(str(i)*1000)

					file.close()
					self.iter += 1
				self.iter = 0
				print('>>>>Spam finished')

			elif message.strip() == 'help':
				print("""
				Command list:
----------------------------------------------------------------------------
|change dir|ext [dir|extension] -> changes directory|file extension to spam|
|#change dir /home/neformal/Документы/test                                 |
|#change ext .txt                                                          |
----------------------------------------------------------------------------
|set [number of files] -> sets number of spam files                        |
|#set inf //infinit files                                                  |
|#set 5 //5 files                                                          |
----------------------------------------------------------------------------
|start -> starts spam                                                      |
----------------------------------------------------------------------------
|exit -> shutdown programm                                                 |
----------------------------------------------------------------------------
|help -> print this message                                                |
----------------------------------------------------------------------------
|about -> print message about this programm                                |
----------------------------------------------------------------------------
					""")
			elif message.strip() == 'about':
				print ("""
Welcome to dirshitter!
This program filling directory with text files.
My github: https://github.com/Prepodobnuy
					""")
if __name__ == '__main__':
	app = main()