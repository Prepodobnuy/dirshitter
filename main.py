def main():
	
	with open('settings.conf') as file:
		
		config = file.read().split('\n')
		conf = []
		for half in config:
			conf.append(half.split('=')[1])
    
	def confedit():

		run = True

		def write(towrite):
			with open('settings.conf','w+') as file:
				file.write(f'''path={towrite[0]}
extention={towrite[1]}
filecount={towrite[2]}
stringlen={towrite[3]}
stringsinfile={towrite[4]}''')

		def path(path):
			conf[0] = path
			write(conf)
		
		def exte(exte):
			conf[1] = exte
			write(conf)

		def filecount(num):
			conf[2] = num
			write(conf)

		def strlen(num):
			conf[3] = num
			write(conf)

		def strinfile(num):
			conf[4] = num
			write(conf)

		while run:
			task = input('>>')
			if task == 'help': 
				print('''Config commands:
set path [path] - - - - - sets spam folder
set extension [ext] - - - sets spam files extension
set filecount [num] - - - sets spam files number
set stringlen [num] - - - sets length of 1 string in file
set stringsinfile [num] - sets num of strings in file

back - return to previous mode
''')		
			elif 'set' in task:
				if 'path' in task:
					path(task.split(' ')[2])
				elif 'extension' in task:
					exte(task.split(' ')[2])
				elif 'filecount' in task:
					filecount(int(task.split(' ')[2]))
				elif 'stringlen' in task:
					strlen(int(task.split(' ')[2]))
				elif 'stringsinfile' in task:
					strinfile(int(task.split(' ')[2]))
			
			elif 'back' in task:
				run = False
	
	def start():
		for i in range(int(conf[2])):
			with open(f'{conf[0]}{i}{conf[1]}', 'w+') as file:
				for j in range(int(conf[3])):
					file.write((f'{j}'*int(conf[4])) + '\n')

	while True:
		task = input('>>')
		if task == 'help':
			print('''Spam commands:
conf - enter config edit mode
start - start spam
exit - exit from program
''')
		elif task == 'conf':
			confedit()
		elif task == 'start':
			start()
		elif task == 'exit':
			exit()

if __name__ == '__main__':
	main()