window.wn_showAngularDeps = function (){
	console.log('webnuke: AngularJS Main Dependencies');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=');
	console.log('<namespace>  |   <dependencies>');
	var deps = wn_getAllAngularDeps();
	for (var dep_record in deps){
		console.log(deps[dep_record].namespace+'  |   '+deps[dep_record].deps.join(', '));
	}
};

window.wn_getAllAngularDeps = function(namespace){
	var main_app_name = wn_getAngularAppName();
	var deps_list=[];
	var main_deps = wn_getAngularDeps(main_app_name);
	deps_list.push({'namespace': main_app_name, 'deps': main_deps});
	
	if(typeof angular !== 'undefined'){
		angular.forEach(main_deps, function(m){
			var deps = wn_getAngularDeps(m);
			deps_list.push({'namespace': m, 'deps': deps});
		});
		
		//now get remaining namespaces....
		additional_namespaces=[]
		angular.forEach(deps_list, function(m){
			var deps = m['deps'];
			angular.forEach(deps, function(depname){
				if(wn_contains_namespace(depname, deps_list)==false){
					additional_namespaces.push(depname);
				}
			});
		});
		
		angular.forEach(additional_namespaces, function(m){
			var deps = wn_getAngularDeps(m);
			deps_list.push({'namespace': m, 'deps': deps});
		});
	}
	return deps_list;
};


window.wn_getAngularDeps = function(namespace){
	var deps = [];
	if(typeof angular !== 'undefined'){
		angular.forEach(angular.module(namespace).requires, function(m){deps.push(m);});
	}
	return deps;
};


window.wn_contains_namespace = function(namespace, alldeps){
	angular.forEach(alldeps, function(m){
		if(m['namespace'] == namespace){
			return true;
		}
	});
	
	return false;
};

