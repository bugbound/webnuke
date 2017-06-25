from selenium.common.exceptions import WebDriverException
import sys


class JavascriptCommands:
	def __init__(self, webdriver, jsinjector):
		self.version = 0.1
		self.driver = webdriver
		self.jsinjector = jsinjector
		
	def search_for_urls(self):
		self.jsinjector.execute_javascript(self.driver, 'wn_findStringsWithUrls()')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")

	def search_for_document_javascript_methods(self):
		self.jsinjector.execute_javascript(self.driver, 'wn_findMethodsOfThis()')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")
		
	def run_lone_javascript_functions(self):
		print "getting global window object"
		globalitems=[]
		noargfunctions=[]
		properrors=0
		try:
			javascript="jsproberesults=[];for (name in this) {  try{jsproberesults.push( {'name':''+name, 'value': ''+this[name]})}catch(err){var anyerror='ignore'};};return jsproberesults"
			jsresults = self.executeJavascriptAndReturnArray(javascript)
			for logline in jsresults:
				if '[native code]' not in logline['value'] and 'jsproberesults' not in logline['name']:
					globalitems.append(logline)
			
			print str(len(globalitems))+' global items found'
			for record in globalitems:
				if not record['name'].startswith('wn_'):
					if record['value'].startswith('function '+record['name']+'()') or record['value'].startswith('function ()'):
						noargfunctions.append(record['name'])
					#print '\t'+record['name']+': '+record['value']
			
			
			print "Found "+str(len(noargfunctions))+" lone Javascript functions"
			for record in noargfunctions:
				print "\t"+record
			print ""
			
			if len(noargfunctions) > 0:	
				print "Calling "+str(len(noargfunctions))+" lone Javascript functions"
				for record in noargfunctions:
					if not record.startswith("wn_"):
						print "\tCalling %s()"%record
						javascript = record+"()"
						try:
							self.driver.execute_script(javascript)
						except:
							pass
			
				
		except WebDriverException as e:
			print "Selenium Exception: Message: "+str(e)
		except:
			print 'probe_window FAILED'
			print "Unexpected error:", sys.exc_info()[0]
			raise

		print ''
		raw_input("Press ENTER to return to menu.")
			
	def executeJavascriptAndReturnArray(self, javascript):
		try:
			self.clearAlertBox()
			return self.driver.execute_script(javascript)
		except WebDriverException as e:
			print "Selenium Exception: Message: "+str(e)
		except:
			print 'probe_window FAILED'
			print "Unexpected error:", sys.exc_info()[0]
			raise

	def clearAlertBox(self):
		try:
			alert = self.driver.switch_to_alert()
			alert.accept()
		except:
			pass
		
	
