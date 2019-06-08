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
	  if(id.startsWith('wn_') == false){	
		try {
		  if (typeof(obj[id]) == "function") {
			result.push(id+":"+obj[id].toString());
		  }
		} catch (err) {
		  result.push(id);
		}
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


window.wn_showCookie = function(){
	console.log('webnuke: Show Cookies');
	console.log('-=-=-=-=-=-=-=-=-=-=-')
	console.log(document.cookie);
	
}



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
