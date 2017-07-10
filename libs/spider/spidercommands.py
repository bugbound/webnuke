import time
import requests

class SpiderCommands:
	def __init__(self, proxy_host, proxy_port):
		self.version = 0.1
		self.proxy_host = proxy_host
		self.proxy_port = proxy_port
		
	def run_kitchensinks_in_foreground(self, url):
		print "Running Kitchensinks on %s, please wait..."%url
		print ''
		print ''
		kitchensinks_path = 'libs/spider/data/fuzzdb/discovery/predictable-filepaths/KitchensinkDirectories.txt'
		
		
		
		with open(kitchensinks_path) as f:
			content = f.read().splitlines()
		for line in content:
			url_to_try = self.build_full_url(url, line)
			r = self.get_result(url_to_try)
			if r is not None:
				self.log_result(r, url_to_try)
			
		print ''
		print ''
		raw_input("Finished, Press ENTER to return to menu.")
		
	def build_full_url(self, url, line):
		url_to_return = url
		if line[0] == '/' and url[-1] == '/': 
			url_to_return += line[1:]
		else:
			url_to_return = url+"/"+line
			
		return url_to_return
	
	def get_result(self, url_to_try):
		proxies = {
					'http': 'http://%s:%s'%(self.proxy_host, self.proxy_port),
					'https': 'http://%s:%s'%(self.proxy_host, self.proxy_port),
		}
		
		try:
			if self.proxy_port > 0:
				return requests.get(url_to_try, proxies=proxies, verify=False)
		
			return requests.get(url_to_try, verify=False)
		except:
			print "!!!ERROR - "+url_to_try
			time.sleep(10)
			#sleep a bit to ease up on network sockets
			pass
			
		return None
		
	def log_result(self, r, url_to_try):
		if r.status_code != 404:
			print '%s - %s'%(r.status_code, url_to_try)
		
