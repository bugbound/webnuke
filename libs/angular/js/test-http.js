

window.wn_testHTTPClasses = function(){
	console.log('webnuke: AngularJS Testing Classes using $http');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=');
	
	var angular_classes = wn_getAngularAllClasses();
	var drf = [];
	
	var component_names = [];
	for (var class_record in angular_classes){
		//console.log("--[ "+angular_classes[class_record]['namespace']+" ]--");
		var components = angular_classes[class_record]['classes'];
		
		angular.forEach(components, function(m){
			//creane new instance
			try{
				if(component_names.indexOf(m.name) >= 0)
				{
					// do nothing
				}
				else
				{
					component_names.push(m.name);
					var api = angular.element(document.body).injector().get(m.name)
					var service_name = m.name
					if(service_name.startsWith('$') == false)
					{			
						console.log("Testing "+service_name);	
						try{
							api.query();
							drf.push(service_name+".query()");
							}
						catch(err){}
							
						try{
							api.get();
							drf.push(service_name+".get()");
							}
						catch(err){}						
						
						try{
							api.getData();
							drf.push(service_name+".getData()");
							}
						catch(err){}						
					}
				}
			}
			catch(err){//console.log("err");
				}
			
		});								
	}
	
	console.log("Found the following items...");
	for (var x in drf){
		console.log(drf[x]);	
	}

};	


window.wn_isPromise = function(x){
	try{
		if (typeof x.then === "function"){return true;}
	}
	catch(err){
		console.log("EEEEE");
		console.log(err);
		return false;
		}
};
