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


window.wn_findStringsWithUrls = function(){
	console.log('webnuke: Strings Containing URLS from Javascript properties');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
	var obj = this;
	for( var key in obj ) {
		if ( obj.hasOwnProperty(key) ) {
			var keyvalue = obj[key];
			
			if(key.startsWith('wn_') == false){			
				if(typeof keyvalue === "function"){
					var functionCodeToExamine = obj[key].toString(); 
					if(~functionCodeToExamine.indexOf('://')){
						console.log(functionCodeToExamine);
						console.log('');
					}
				}
				if(typeof keyvalue === "string"){
					if(~keyvalue.indexOf('://')){
						console.log(key+": "+keyvalue);
					}
				}
			}
		}
	}
};	
