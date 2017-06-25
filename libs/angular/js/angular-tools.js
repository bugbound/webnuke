window.wn_getAngularAllClasses = function(){
	var deps = wn_getAllAngularDeps();
	var rtnData = [];
	angular.forEach(deps, function(m){
		var namespace_classes = wn_getAngularClasses(m['namespace']);
		rtnData.push({'namespace': m['namespace'], 'classes': namespace_classes});
	
	});
	return rtnData;
};


window.wn_getAngularClasses = function(namespace){
	//namespace = 'angularFlaskServices';
	//namespace = 'reporterApp';
	var rtnData = [];
	angular.module(namespace)['_invokeQueue'].forEach(function(value){ 
		var items = value[2][1];
		isarray = items instanceof Array;
		var item_name = value[2][0];
		if(isarray){
			var components = items.slice(0, -1);
			var source = items[items.length-1];
			var record = {'type': value[1], 'name': value[2][0], 'sourcecode': source, 'components': components}
			rtnData.push(record);
		}
		else{
			var source = "na";
			var components = value[2][1]
			var record = {'type': value[1], 'name': value[2][0], 'sourcecode': source, 'components': components};
			rtnData.push(record);
		}								
	});
	return rtnData;
};

window.wn_getAngularMainClassesOLDWORKING = function(){
	namespace = wn_getAngularAppName();
	var rtnData = [];
	angular.module(namespace)['_invokeQueue'].forEach(function(value){ 
		var sourcecode="not available!";
		if(value[2].length == 2){
			sourcecode = value[2][1].toString();
			console.log(value[2][1])
		}
		rtnData.push({'type': value[1], 'name': value[2][0], 'sourcecode': sourcecode});
	});
	return rtnData;
};

window.wn_showAngularMainClasses = function(){
	console.log('webnuke: AngularJS Main Classes');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-');
	var angular_classes = wn_getAngularClasses(wn_getAngularAppName());
	for (var class_record in angular_classes){
		console.log(angular_classes[class_record]['name']+' - '+angular_classes[class_record]['type']);
		var components = angular_classes[class_record]['components'];
		console.log('\t'+Array.prototype.join.call(components, ', '));
		console.log('');
	}
};	

window.wn_showAngularAllClasses = function(){
	console.log('webnuke: AngularJS All Classes');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=');
	var angular_classes = wn_getAngularAllClasses();
	for (var class_record in angular_classes){
		console.log("--[ "+angular_classes[class_record]['namespace']+" ]--");
		var components = angular_classes[class_record]['classes'];
		var component_names = [];
		angular.forEach(components, function(m){
			component_names.push(m.name);
		});								
		console.log('\t'+component_names.join(', '));
		console.log('');
	}
};	





