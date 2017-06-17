class JSConsoleScript:
	def __init__(self, jsinjector):
		self.version=0.1
		self.jsinjector = jsinjector
		self.jsinjector.add_help_topic('wn_help()', 'Shows WebNuke Help')
		self.jsinjector.add_help_topic('wn_findStringsWithUrls()', 'Try and locate urls within Javascript strings')
		self.jsfunctions = """		
						
window.wn_findStringsWithUrls = function(){
	console.log('webnuke: Strings Containing URLS from Javascript properties');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
	var obj = this;
	for( var key in obj ) {
		if ( obj.hasOwnProperty(key) ) {
			var keyvalue = obj[key];
			if(typeof keyvalue === "string"){
				if(~keyvalue.indexOf('://')){
					console.log(keyvalue)
					console.log('')
				}
			}
		}
	}
};		
		"""
		self.jsinjector.inject_js(self.jsfunctions)
		
