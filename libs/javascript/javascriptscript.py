class JavascriptScript:
	def __init__(self, jsinjector):
		self.version=0.1
		self.jsinjector = jsinjector
		self.jsinjector.add_help_topic('wn_findMethodsOfThis()', 'print javascript methods')
		self.jsinjector.add_help_topic('wn_getMethodsPlusCode()', 'print javascript methods and code')
		self.jsinjector.add_help_topic('wn_getFunctions()', 'returns array of javascript functions')
		self.jsinjector.add_help_topic('wn_listFunctions()', 'print javascript function names')
		self.jsinjector.add_help_topic('wn_findStringsWithUrls()', 'Try and locate urls within Javascript strings')
		self.jsinjector.add_help_topic('wn_showCookie()', 'Show Cookies')
		self.jsinjector.add_js_file('libs/javascript/javascript-tools.js')
		
