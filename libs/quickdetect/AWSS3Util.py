from selenium import webdriver
import time 
class AWSS3Util:
	def __init__(self, webdriver, start_url, logger):
		self.version = 0.1
		self.beta = True
		self.webdriver = webdriver
		self.start_url = start_url
		self.end_url = self.webdriver.current_url
		self.known_s3_hosts=['.amazonaws.com']
		self.logger =logger
	

	
		
	def hasS3Buckets(self):
		result = False
		try:
			
			metatags = self.webdriver.find_elements_by_xpath("//meta")
			for tag in metatags:
				contenturl = tag.get_attribute('content')
				if contenturl:
					for s3host in self.known_s3_hosts:
						if s3host in contenturl:
							result = True
				
			
			imgtags = self.webdriver.find_elements_by_xpath("//img")
			for tag in imgtags:
				contenturl = tag.get_attribute('src')
				if contenturl:
					for s3host in self.known_s3_hosts:
						if s3host in contenturl:
							result = True

			linktags = self.webdriver.find_elements_by_xpath("//link")
			for tag in linktags:
				contenturl = tag.get_attribute('href')
				if contenturl:
					for s3host in self.known_s3_hosts:
						if s3host in contenturl:
							result = True
							
			scripttags = self.webdriver.find_elements_by_xpath("//script")
			for tag in scripttags:
				contenturl = tag.get_attribute('src')
				if contenturl:
					for s3host in self.known_s3_hosts:
						if s3host in contenturl:
							result = True
														
			atags = self.webdriver.find_elements_by_xpath("//a")
			for tag in atags:
				contenturl = tag.get_attribute('href')
				if contenturl:
					for s3host in self.known_s3_hosts:
						if s3host in contenturl:
							result = True														



		except:
			print "ERRORORORORORO"
			raise
		return result
		
	def getUrlString(self):
		return "S3 BUCKET"
		
