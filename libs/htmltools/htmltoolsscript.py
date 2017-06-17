class HTMLToolsScript:
	def __init__(self, jsinjector):
		self.version=0.1
		self.jsinjector = jsinjector
		self.jsinjector.add_help_topic('wn_showHiddenFormElements()',   'Show hidden form elements in the browser')
		self.jsinjector.add_help_topic('wn_showPasswordFieldsAsText()', 'Show password fields as text in the browser')		
		self.jsfunctions = """		
window.wn_showHiddenFormElements = function(){
	console.log('webnuke: Show hidden form elements');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=');
	
	
	var inputelements = document.body.getElementsByTagName('input');
	var hidden_elements=[];
	for(x in inputelements) {
		if(inputelements[x].type == 'hidden'){
			hidden_elements.push(inputelements[x])
		}
	}
	for (x in hidden_elements){
		hidden_elements[x].type='text';
	}
    
    if(hidden_elements.length == 0){
		console.log('No hidden form elements found on page');
    }
    else{
		console.log('Hidden forms elements should now be visible within the browser');
	}
};


window.wn_showPasswordFieldsAsText = function(){
	console.log('webnuke: Show passwords fields as text');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=');
	
	
	var inputelements = document.body.getElementsByTagName('input');
	var elements=[];
	for(x in inputelements) {
		if(inputelements[x].type == 'password'){
			elements.push(inputelements[x])
		}
	}
	for (x in elements){
		elements[x].type='text';
	}
    
    if(elements.length == 0){
		console.log('No password fields found on page');
    }
    else{
		console.log('Password fields should now show as text within the browser');
	}
};
	

		"""
		
		self.jsinjector.inject_js(self.jsfunctions)
		
