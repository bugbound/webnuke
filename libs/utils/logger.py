class FileLogger:
	def __init__(self):
		self.log_path = '/tmp/webnuke.log'
    
	def log(self, text):
		print text
		with open(self.log_path, "ab") as logfile:
			logfile.write("%s\n"%text)
		


