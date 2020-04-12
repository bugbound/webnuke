from pyvirtualdisplay import Display
from selenium import webdriver
import selenium.webdriver.support.ui as ui
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver import Chrome


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
		
		#binary = FirefoxBinary('/usr/bin/firefox-esr')
		#newdriver = webdriver.Firefox(firefox_binary=binary,firefox_profile=profile)
        
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--proxy-server=%s"%("http://"+proxy_host+":"+str(proxy_port)))
		chrome_options.add_argument("--ignore-certificate-errors")
		driver = Chrome(chrome_options=chrome_options)
		return driver
		
		
	def getDriver(self, logger):		
		webnuke_config_proxy_port = 33333
		webnuke_config_web_api_port = 44444
		webnuke_config_web_api_url = 'http://localhost:'+str(webnuke_config_web_api_port)
		
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--ignore-certificate-errors")
		driver = Chrome(chrome_options=chrome_options)
		return driver
		





