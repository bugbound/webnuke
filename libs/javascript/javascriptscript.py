class JavascriptScript:
	def __init__(self, jsinjector):
		self.version=0.1
		self.jsinjector = jsinjector
		self.jsinjector.add_help_topic('wn_findMethodsOfThis()', 'print javascript methods')
		self.jsinjector.add_help_topic('wn_getMethodsPlusCode()', 'print javascript methods and code')
		self.jsinjector.add_help_topic('wn_getFunctions()', 'returns array of javascript functions')
		self.jsinjector.add_help_topic('wn_listFunctions()', 'print javascript function names')
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
