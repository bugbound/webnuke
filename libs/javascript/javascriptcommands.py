from selenium.common.exceptions import WebDriverException
import sys


class JavascriptCommands:
	def __init__(self, webdriver, jsinjector):
		self.version = 0.1
		self.driver = webdriver
		self.jsinjector = jsinjector
		
	def search_for_urls(self):
		self.jsinjector.execute_javascript(self.driver, 'wn_findStringsWithUrls();')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")


	def walk_functions(self):
		self.jsinjector.execute_javascript(self.driver, 'wn_walk_functions(this, "this")')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")


	def search_for_document_javascript_methods(self):
		script_to_include = """
var blacklist = ["__webDriverComplete", "__webDriverArguments", "close","stop","focus","blur","open","alert","confirm","prompt","print","postMessage","captureEvents","releaseEvents","getSelection","getComputedStyle","matchMedia","moveTo","moveBy","resizeTo","resizeBy","scroll","scrollTo","scrollBy","requestAnimationFrame","cancelAnimationFrame","getDefaultComputedStyle","scrollByLines","scrollByPages","sizeToContent","updateCommands","find","dump","setResizable","requestIdleCallback","cancelIdleCallback","btoa","atob","setTimeout","clearTimeout","setInterval","clearInterval","createImageBitmap","fetch","self","name","history","locationbar","menubar","personalbar","scrollbars","statusbar","toolbar","status","closed","frames","length","opener","parent","frameElement","navigator","external","applicationCache","screen","innerWidth","innerHeight","scrollX","pageXOffset","scrollY","pageYOffset","screenX","screenY","outerWidth","outerHeight","performance","mozInnerScreenX","mozInnerScreenY","devicePixelRatio","scrollMaxX","scrollMaxY","fullScreen","mozPaintCount","ondevicemotion","ondeviceorientation","onabsolutedeviceorientation","ondeviceproximity","onuserproximity","ondevicelight","sidebar","crypto","onabort","onblur","onfocus","onauxclick","oncanplay","oncanplaythrough","onchange","onclick","onclose","oncontextmenu","ondblclick","ondrag","ondragend","ondragenter","ondragexit","ondragleave","ondragover","ondragstart","ondrop","ondurationchange","onemptied","onended","oninput","oninvalid","onkeydown","onkeypress","onkeyup","onload","onloadeddata","onloadedmetadata","onloadend","onloadstart","onmousedown","onmouseenter","onmouseleave","onmousemove","onmouseout","onmouseover","onmouseup","onwheel","onpause","onplay","onplaying","onprogress","onratechange","onreset","onresize","onscroll","onseeked","onseeking","onselect","onshow","onstalled","onsubmit","onsuspend","ontimeupdate","onvolumechange","onwaiting","onselectstart","ontoggle","onpointercancel","onpointerdown","onpointerup","onpointermove","onpointerout","onpointerover","onpointerenter","onpointerleave","ongotpointercapture","onlostpointercapture","onmozfullscreenchange","onmozfullscreenerror","onanimationcancel","onanimationend","onanimationiteration","onanimationstart","ontransitioncancel","ontransitionend","ontransitionrun","ontransitionstart","onwebkitanimationend","onwebkitanimationiteration","onwebkitanimationstart","onwebkittransitionend","onerror","speechSynthesis","onafterprint","onbeforeprint","onbeforeunload","onhashchange","onlanguagechange","onmessage","onmessageerror","onoffline","ononline","onpagehide","onpageshow","onpopstate","onstorage","onunload","localStorage","origin","isSecureContext","indexedDB","caches","sessionStorage","document","location","top","addEventListener","removeEventListener","dispatchEvent"];

jsproberesults=[];for (name in this) {  
if ((blacklist.includes(name) == false) && (name.startsWith('wn_') == false)){jsproberesults.push('"'+name+'"')};}
var full = jsproberesults.join(','); console.log(full);		
		
		"""
		self.jsinjector.execute_javascript(self.driver, script_to_include)
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

	def show_cookies(self):
		self.jsinjector.execute_javascript(self.driver, 'wn_showCookie()')
		print ''
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
		
	
