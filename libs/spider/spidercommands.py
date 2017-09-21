import time
import requests

class SpiderCommands:
	def __init__(self, webdriver):
		self.version = 0.1
		self.webdriver = webdriver
		self.default_page_element_count = 0 
		
	def run_kitchensinks_in_foreground(self, url):
		print "Running Kitchensinks on %s, please wait..."%url
		print ''
		print ''
		# try fuzzdb, kitchensinks
		kitchensinks_path = 'libs/spider/KitchensinkDirectories.txt'
		
		
		
		with open(kitchensinks_path) as f:
			content = f.read().splitlines()
		for line in content:
			url_to_try = self.build_full_url(url, line)
			r = self.try_url(url_to_try)
		
			
		print ''
		print ''
		raw_input("Finished, Press ENTER to return to menu.")
		
	def build_full_url(self, url, line):
		url_to_return = url
		
		if '#' in url:
			url_without_hash = url.split('#')[0]
			url_to_return = url_without_hash+'#'+line
		elif line[0] == '/' and url[-1] == '/': 
			url_to_return += line[1:]
		else:
			url_to_return = url+"/"+line
			
		return url_to_return
	
	def try_url(self, url_to_try):		
		try:
			if self.default_page_element_count == 0:
				all_elements = self.webdriver.find_elements_by_xpath('//*')
				self.default_page_element_count = len(all_elements)
			self.webdriver.get(url_to_try)
			#time.sleep(0.5)
			newurl = self.webdriver.current_url
			new_elements = self.webdriver.find_elements_by_xpath('//*')
			new_elements_count= len(new_elements)
			if new_elements_count != self.default_page_element_count:
				print "XXX "+url_to_try
			
		
		except:
			print "!!!ERROR - "+url_to_try
			time.sleep(10)
			#sleep a bit to ease up on network sockets
			pass
			
		return None
		
	def log_result(self, r, url_to_try):
		if r.status_code != 404:
			print '%s - %s'%(r.status_code, url_to_try)
		
