from selenium.common.exceptions import WebDriverException
import sys


class JSWalker:
	def __init__(self, webdriver, jsinjector):
		self.version = 0.1
		self.driver = webdriver
		self.jsinjector = jsinjector
	
	def start_walk_tree(self):
		#javascript="jsproberesults=[];for (name in this) {  try{jsproberesults.push( {'name':''+name, 'value': ''+this[name]})}catch(err){var anyerror='ignore'};};return jsproberesults"
		javascript = """
window.wn_walk_functions = function(rootnode, pathstring){
	var blacklist = ["InstallTrigger", "window", "__webDriverComplete", "__webDriverArguments", "close","stop","focus","blur","open","alert","confirm","prompt","print","postMessage","captureEvents","releaseEvents","getSelection","getComputedStyle","matchMedia","moveTo","moveBy","resizeTo","resizeBy","scroll","scrollTo","scrollBy","requestAnimationFrame","cancelAnimationFrame","getDefaultComputedStyle","scrollByLines","scrollByPages","sizeToContent","updateCommands","find","dump","setResizable","requestIdleCallback","cancelIdleCallback","btoa","atob","setTimeout","clearTimeout","setInterval","clearInterval","createImageBitmap","fetch","self","name","history","locationbar","menubar","personalbar","scrollbars","statusbar","toolbar","status","closed","frames","length","opener","parent","frameElement","navigator","external","applicationCache","screen","innerWidth","innerHeight","scrollX","pageXOffset","scrollY","pageYOffset","screenX","screenY","outerWidth","outerHeight","performance","mozInnerScreenX","mozInnerScreenY","devicePixelRatio","scrollMaxX","scrollMaxY","fullScreen","mozPaintCount","ondevicemotion","ondeviceorientation","onabsolutedeviceorientation","ondeviceproximity","onuserproximity","ondevicelight","sidebar","crypto","onabort","onblur","onfocus","onauxclick","oncanplay","oncanplaythrough","onchange","onclick","onclose","oncontextmenu","ondblclick","ondrag","ondragend","ondragenter","ondragexit","ondragleave","ondragover","ondragstart","ondrop","ondurationchange","onemptied","onended","oninput","oninvalid","onkeydown","onkeypress","onkeyup","onload","onloadeddata","onloadedmetadata","onloadend","onloadstart","onmousedown","onmouseenter","onmouseleave","onmousemove","onmouseout","onmouseover","onmouseup","onwheel","onpause","onplay","onplaying","onprogress","onratechange","onreset","onresize","onscroll","onseeked","onseeking","onselect","onshow","onstalled","onsubmit","onsuspend","ontimeupdate","onvolumechange","onwaiting","onselectstart","ontoggle","onpointercancel","onpointerdown","onpointerup","onpointermove","onpointerout","onpointerover","onpointerenter","onpointerleave","ongotpointercapture","onlostpointercapture","onmozfullscreenchange","onmozfullscreenerror","onanimationcancel","onanimationend","onanimationiteration","onanimationstart","ontransitioncancel","ontransitionend","ontransitionrun","ontransitionstart","onwebkitanimationend","onwebkitanimationiteration","onwebkitanimationstart","onwebkittransitionend","onerror","speechSynthesis","onafterprint","onbeforeprint","onbeforeunload","onhashchange","onlanguagechange","onmessage","onmessageerror","onoffline","ononline","onpagehide","onpageshow","onpopstate","onstorage","onunload","localStorage","origin","isSecureContext","indexedDB","caches","sessionStorage","document","location","top","addEventListener","removeEventListener","dispatchEvent"];
	var rtndata = [];
	for (name in rootnode) {  
		typefound = typeof rootnode[name];
		var fullname = ""+pathstring+"."+name;
		if(typefound == "object"){
			blacklistlookup = fullname.substring(5);
			if (blacklist.includes(blacklistlookup) == false ) {
				console.log("OBJECT: "+fullname);
				rtndata.push({'type': 'object', 'fullpath': fullname});
				//wn_walk_functions(rootnode[name], fullname);
			}
			
		}
		else if(typefound == "function"){
			blacklistlookup = fullname.substring(5);
			if (blacklist.includes(blacklistlookup) == false && name.startsWith("wn_") == false) {
				rtndata.push({'type': 'function', 'fullpath': fullname});
				console.log("FUNCTION: "+fullname+"()");
			}
		}
		else {
			rtndata.push({'type': 'ignored', 'fullpath': fullname});
			//console.log("Name: "+name+" ["+typefound+"]"); 
			//console.log(fullname)  
		}
	
	}
	
	return rtndata;
}
"""
		# inject walk function
		self.driver.execute_script(javascript)
		self.walk_tree('this','this')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")


	def walk_tree(self, rootnode, fullpath):
		javascript="return wn_walk_functions(%s, '%s');"%(rootnode, fullpath)		
		jsresults = self.executeJavascriptAndReturnArray(javascript)
		#print jsresults
		for record in jsresults:
			recordtype = record['type']
			fullpath = record['fullpath']
			if recordtype == 'function':
				confirmed = self.confirm("Do you want to run javascript function '"+fullpath+"'?")
				if confirmed:
					print "running function "+fullpath+"();"
					self.jsinjector.execute_javascript(self.driver, fullpath+"();")
			if recordtype == 'object':
				confirmed = self.confirm("Do you want to walk '"+fullpath+"'?")
				if confirmed:
					print "walking object "+fullpath+""
					self.walk_tree(fullpath, fullpath)
			#print "%s [%s]"%(record['fullpath'], record['type'])
		
		
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
			return self.driver.execute_script(javascript)
		except WebDriverException as e:
			print "Selenium Exception: Message: "+str(e)
		except:
			print 'probe_window FAILED'
			print "Unexpected error:", sys.exc_info()[0]
			raise
	
	def confirm(self, message):
		bah = raw_input(message+" (Y/n):")
		if bah == 'Y' or bah == 'y' or bah == '':
			return True
		if bah == 'N' or bah == 'n':	
			return False
		return self.confirm(message)
