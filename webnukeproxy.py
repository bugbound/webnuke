#
#pip install https://pypi.python.org/packages/source/m/mitmproxy/mitmproxy-0.15.tar.gz

 
from libmproxy import controller, proxy, utils
from gzip import GzipFile
from StringIO import StringIO
import os
import threading
import json
import requests 

class ProxySupport:
	def __init__(self, name, port, logger):
		self.logger = logger
		self.logger.log("Starting proxy server...")
		#config = proxy.ProxyConfig(
		#	cacert = os.path.expanduser("~/.mitmproxy/mitmproxy-ca.pem")
		#)
		#config = proxy.ProxyConfig(upstream_server=("http", "192.168.1.7", "8080"), port=port)
		config = proxy.ProxyConfig(port=port)
		server = proxy.ProxyServer(config)
		self.master = ProxyMaster(server)
		self.master.setname(name)
		self.master.setLogger(self.logger)
		
		self.thread = threading.Thread(target=self.master.run)
		self.thread.daemon = True
		self.thread.start()
		self.logger.log("Proxy server up and running")
	
	def stop(self):
		self.logger.log("Stopping proxy server...")
		self.master.shutdown()
		self.logger.log("Proxy server stoped.")


class ProxyMaster(controller.Master):
    def setname(self, name):
		self.name = name
		
    def setLogger(self, logger):
		self.logger = logger
		
    def handle_request(self, msg):	
		self.logger.log("got request - %s"%msg.request.pretty_url)
		#self.remote_log(msg)
		msg.reply()

    def handle_response(self, msg):	
		self.remote_log(msg)
		
		hid = (msg.request.host, msg.request.port)
		msg.reply()

    def remote_log(self, msg):   
        headerdump=''
        for item in msg.request.headers:
			headerdump+=str("%s: %s\n"%(item, msg.request.headers.get(item)))
			
        response_headerdump=''
        if msg.response:
			for itema in msg.response.headers:
				response_headerdump+=str("%s: %s\n"%(itema, msg.response.headers.get(itema)))
        
        status_code = -1
        if msg.response:
			 status_code = msg.response.status_code
        
        reason = ''
        if msg.response:
			reason  = msg.response.reason.decode('utf-8', "ignore")
			
        response_http_version = -1
        if msg.response:
			response_http_version = msg.response.http_version
		
		
			
        response_content = '<HTTP REQUEST ONLY>'
        if msg.response:
			#self.logger.log("is gzip???")
			#self.logger.log(msg.response.headers.get('Content-Encoding'))
			if msg.response.headers.get('Content-Encoding') == 'gzip':
				response_content = GzipFile('', 'rb', 9, StringIO(msg.response.content)).read()
			else:
				response_content = msg.response.content
			
			
        recordToAdd = {'Request_Path': msg.request.path.decode('utf-8', "ignore"), 
				'Request_FullUrl': msg.request.pretty_url.decode('utf-8', "ignore"), 
				'Request_Method': msg.request.method.decode('utf-8', "ignore"),
				'Request_HttpVersion': "%s" % (msg.request.http_version),
				'Request_Headers': headerdump.decode('utf-8', "ignore"),
				'Request_Content': msg.request.content.decode('utf-8', "ignore"),
				'Response_Code': status_code,
				'Response_CodeMsg': reason.decode('utf-8', "ignore"),
				'Response_Headers': response_headerdump,
				'Response_Content': response_content.decode('utf-8', "ignore"),
				'Response_HttpVersion': "%s" % (response_http_version),
				'Proxy_Name': self.name
				}
        #print recordToAdd
        headers = {'Content-type': 'application/json'}
        try:
			url = "http://localhost:8010/api/v1/http_response"
			#self.logger.log(json.dumps(recordToAdd))
			r = requests.post(url, data=json.dumps(recordToAdd), headers=headers)
			self.logger.log("POSTED web transaction - %s - %s" %(r.status_code, r.reason))
        except:
			self.logger.log("ERROR Posting to API" )
			raise

        

