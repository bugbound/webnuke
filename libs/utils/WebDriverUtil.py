from pyvirtualdisplay import Display
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class WebDriverUtil:
	def __init__(self):
		self.version = 0.1
		self.beta = True
		self.debug = False
		
	def setDebug(self, newValue):
		self.debug = newValue
	
	
	def getWebDriverProfile(self):
		profile = webdriver.FirefoxProfile()
		#profile.set_preference("browser.cache.disk.enable", False)
		#profile.set_preference("browser.cache.memory.enable", False)
		#profile.set_preference("browser.cache.offline.enable", False)
		#profile.set_preference("network.http.use-cache", False)
		return profile
		
	def getDriverWithProxySupport(self, proxy_host, proxy_port):
		if self.debug == False:
			self.display = Display(visible=0, size=(1920, 1080))
			self.display.start()
		profile = self.getWebDriverProfile()
		profile.set_preference("network.proxy.type", 1)
		profile.set_preference("network.proxy.http", proxy_host)
		profile.set_preference("network.proxy.http_port", proxy_port)
		profile.set_preference("network.proxy.https", proxy_host)
		profile.set_preference("network.proxy.https_port", proxy_port)
		profile.set_preference("network.proxy.ssl", proxy_host)
		profile.set_preference("network.proxy.ssl_port", proxy_port)
		profile.update_preferences()
		
		newdriver = webdriver.Firefox(firefox_binary=binary,firefox_profile=profile)
		
		#newdriver = webdriver.Firefox(firefox_profile=profile)
		self.wait = ui.WebDriverWait(newdriver, 10) # timeout after 10 seconds
		return newdriver
		
	def getDriver(self, logger):		
		webnuke_config_proxy_port = 33333
		webnuke_config_web_api_port = 44444
		webnuke_config_web_api_url = 'http://localhost:'+str(webnuke_config_web_api_port)
		#self.web_api_server = WebAPIServer(webnuke_config_web_api_port, logger)
		#self.web_api_server.startServer()
		
		
		#self.proxy_support = ProxySupport('webnuke-proxy', webnuke_config_proxy_port, webnuke_config_web_api_url)
		profile = self.getWebDriverProfile()
		profile.update_preferences()

		binary = FirefoxBinary('/usr/bin/firefox-esr')
		newdriver = webdriver.Firefox(firefox_binary=binary,firefox_profile=profile)
		#newdriver = webdriver.Firefox(firefox_profile=profile)
		#self.driver = self.getDriverWithProxySupport('localhost', webnuke_config_proxy_port)
		return newdriver
		





