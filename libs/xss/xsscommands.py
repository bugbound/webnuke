from selenium.common.exceptions import UnexpectedAlertPresentException

class XSSCommands:
	def __init__(self, webdriver, logger):
		self.version = 0.1
		self.driver = webdriver
		self.logger = logger
		
		
	def find_xss(self):
		print "finding xss..."
		current_url = self.driver.current_url
		suggestor = XSS_Url_Suggestor(current_url)
		urls_to_try = suggestor.get_xss_urls()
		print "url is %s"%current_url
		print ''
		for x in urls_to_try:
			try:
				self.driver.get(x)
				self.driver.get(current_url)
			except UnexpectedAlertPresentException:
				print "XSS - "+x
				pass
			except:
				print "Some error happened finding xss!"
				pass
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")
		


class XSS_Url_Suggestor:
	def __init__(self, url):
		self.version = 0.1
		self.url = url
		
	def get_xss_urls(self):
		rtnData = []
		xss_attacks = ['<script>alert(1)</script>',
						'<img src=x onerror="alert(1)" />'
						"'/><img src=x onerror='alert(1)' />",
						'"/><img src=x onerror="alert(1)" />',
						';alert(1);',
						'";alert(1);',
						"';alert(1);",
						]
						
		urlsplitloc = self.url.find("?")
		if urlsplitloc >= 0:
			paramstring = self.url[urlsplitloc+1:]
			basestring = self.url[:urlsplitloc]
			params = paramstring.split('&')
			
			for singleparam in params:
				posinurl = self.url.find(singleparam)
				(key, value) = singleparam.split('=')
				for xss_payload in xss_attacks:
					newurl = self.url.replace(singleparam, '%s=%s'%(key, xss_payload))
					rtnData.append(newurl)
				
		return rtnData
		
