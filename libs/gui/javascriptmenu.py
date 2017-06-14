import curses
from selenium.common.exceptions import WebDriverException


class JavascriptScript:
	def __init__(self, jsinjector):
		self.version=0.1
		self.jsinjector = jsinjector
		self.jsfunctions = """		
window.wn_findMethodsOfThis = function(){
	console.log('webnuke: Javascript Methods');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-');
	//var methods = window.wn_getMethods(this);
	var methods = window.wn_getMethodsPlusCode(this);
	console.log(methods.join(', '));
};
	
window.wn_getMethods = function getMethods(obj) {
  var result = [];
  for (var id in obj) {
	try {
	  if (typeof(obj[id]) == "function") {
		result.push(id+":");
	  }
	} catch (err) {
	  result.push(id);
	}
  }
  return result;
};

window.wn_getMethodsPlusCode = function getMethods(obj) {
  var result = [];
  for (var id in obj) {
	try {
	  if (typeof(obj[id]) == "function") {
		result.push(id+":"+obj[id].toString());
	  }
	} catch (err) {
	  result.push(id);
	}
  }
  return result;
};


window.wn_getFunctions = function () {
	var jsproberesults=[];for (name in this) {  try{jsproberesults.push( {'name':''+name, 'value': ''+this[name]})}catch(err){var anyerror='ignore'};}
	return jsproberesults;
};

window.wn_listFunctions = function () {
	var jsproberesults=wn_getFunctions();
	jsproberesults.forEach(function(item, index){console.log(item['name']);});
};

		"""
		
		self.jsinjector.inject_js(self.jsfunctions)
		self.jsinjector.add_help_topic('wn_findMethodsOfThis()', 'print javascript methods')
		self.jsinjector.add_help_topic('wn_getMethodsPlusCode()', 'print javascript methods and code')
		self.jsinjector.add_help_topic('wn_getFunctions()', 'returns array of javascript functions')
		self.jsinjector.add_help_topic('wn_listFunctions()', 'print javascript function names')

class JavascriptScreen:
	def __init__(self, screen, webdriver, curses_util, jsinjector):
		self.version=0.1
		self.screen = screen
		self.driver = webdriver
		
		self.curses_util = curses_util
		self.jsinjector = jsinjector
		
		self.commands = JavascriptCommands(self.driver, self.jsinjector)
		
		
	def show(self):
		showscreen = True
		
		while showscreen:
			self.screen = self.curses_util.get_screen()
			# pic from http://ascii.co.uk/art/rockets
			self.screen.addstr(6, 32, "                           *    ", curses.color_pair(2))
			self.screen.addstr(7, 32, "               +               ", curses.color_pair(2))
			self.screen.addstr(8, 32, "                  *          +   '--'  *", curses.color_pair(2))
			self.screen.addstr(9, 32, "                      +   /\\", curses.color_pair(2))
			self.screen.addstr(10,32, "         +              .'  '.   *", curses.color_pair(2))
			self.screen.addstr(11,32, "                *      /======\\      +", curses.color_pair(2))
			self.screen.addstr(12,32, "                      ;:.      ;", curses.color_pair(2))
			self.screen.addstr(13,32, "                      |:.      |", curses.color_pair(2))
			self.screen.addstr(14,32, "                      |:.      |", curses.color_pair(2))
			self.screen.addstr(15,32, "            +         |:.      |          *", curses.color_pair(2))
			self.screen.addstr(16,32, "                      ;:.      ;", curses.color_pair(2))
			self.screen.addstr(17,32, "                    .' \\:.    / `.", curses.color_pair(2))
			self.screen.addstr(18,32, "                   / .-'':._.'`-. \\", curses.color_pair(2))
			self.screen.addstr(19,32, "                   |/    /||\\    \\|", curses.color_pair(2))
			self.screen.addstr(2, 2, "Javascript Tools")
			self.screen.addstr(4, 5, "4) Find URLS within Javascript Global Properties")
			self.screen.addstr(5, 5, "5) Show Javascript functions of Document")
			self.screen.addstr(6, 5, "6) Run all js functions without args")


			
			self.screen.addstr(22, 28, "PRESS M FOR MAIN MENU")
			self.screen.refresh()
			
			c = self.screen.getch()
			if c == ord('M') or c == ord('m'):
				showscreen=False
				
			if c == ord('4'):
				self.curses_util.close_screen()
				self.commands.search_for_urls()
				
			if c == ord('5'):
				self.curses_util.close_screen()
				self.commands.search_for_document_javascript_methods()
				
		return
		
class JavascriptCommands:
	def __init__(self, webdriver, jsinjector):
		self.version = 0.1
		self.driver = webdriver
		self.jsinjector = jsinjector
		self.install_custom_javascript_functions()
		
	def search_for_urls(self):
		self.execute_javascript('wn_findStringsWithUrls()')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")

	def search_for_document_javascript_methods(self):
		self.execute_javascript('wn_findMethodsOfThis()')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")
		
	def execute_javascript(self, javascript):
		try:
			amended_javascript="""window.webnuke = function(){"""+javascript+""";}; webnuke(); return window.console.flushOutput() """
			result = self.driver.execute_script(amended_javascript)
			if result is not None:
				for result_line in result:
					print result_line
		except WebDriverException:
			print "ERROR with webdriver"
			print javascript
			print ''
			raise
		except:
			raise
			
		print ''
		
	def install_custom_javascript_functions(self):
		javascript = """window.console = {log: function(data){this.output.push(data);}, warn: function(data){this.output.push("WARN: "+data);}, error: function(data){this.output.push("ERROR: "+data);}, output: [], flushOutput: function(){var rtndata = this.output; this.output=[]; return rtndata;}};			
						
						"""+self.jsinjector.get_js_block()
		try:
			self.driver.execute_script(javascript)
		except:
			raise
	
		
	
