class JavascriptInjector:
	def __init__(self):
		self.version = 0.1
		self.jsfunctions=[]
		self.javascript_block=""	
		self.help_block=[]
		
	def inject_js(self, javascript):
		self.javascript_block+=javascript
		
	def add_help_topic(self, jsfunction, description):
		self.jsfunctions.append(jsfunction)
		self.help_block.append({'function': jsfunction, 'description': description})
		
	def get_js_block(self):
		wnhelp_block = """window.wn_help = function(){
	console.log('webnuke: HELP!!');
	console.log('-=-=-=-=-=-=-=-');"""
		for x in self.help_block:
			wnhelp_block+="console.log('"+x['function']+" - "+x['description']+"');"
		wnhelp_block+='};'
	
	
		return self.javascript_block+wnhelp_block
