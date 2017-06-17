class webnuke_api_server:
	def __init__(self, logger):
		self.version = 0.1
		self.logger = logger
		
	
	def start(self):
		self.apiserver = WebAPIServer(8002, logger)
		self.apiserver.startServer()
		self.logger.log("Web server started")
