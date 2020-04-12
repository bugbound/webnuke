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
		hidden_elements[x].style.color="green";
		hidden_elements[x].style.backgroundColor = "black";
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
	
window.wn_showAllHTMLElements = function(){
	console.log('webnuke: Show All HTML Elements');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-');

	var all = document.getElementsByTagName('*');

	for (var i=0, max=all.length; i < max; i++) {
		 var element = all[i];
		 element.style.visibility = 'visible';
	}
};


window.wn_remove_hidden_from_classnames = function(){
	console.log('webnuke: Removing hidden from classnames');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=');

	var all = document.getElementsByTagName('*');

	for (var i=0, max=all.length; i < max; i++) {
		 var element = all[i];
		 element.classList.remove("hidden");
	}
};
