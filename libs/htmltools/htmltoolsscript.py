class HTMLToolsScript:
	def __init__(self, jsinjector):
		self.version=0.1
		self.jsinjector = jsinjector
		self.jsinjector.add_help_topic('wn_showHiddenFormElements()',   'Show hidden form elements in the browser')
		self.jsinjector.add_help_topic('wn_showPasswordFieldsAsText()', 'Show password fields as text in the browser')	
		self.jsinjector.add_help_topic('wn_showAllHTMLElements()', 'Set CSS visibility to visible on all HTML elements in the browser')	
		self.jsinjector.add_js_file('libs/htmltools/htmltools.js')
		
