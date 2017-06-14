class AngularCustomJavascript:
	def __init__(self):
		self.version = 0.1
		
	def getJavascriptToInjectAsString(self):
		javascript = """window.console = {log: function(data){this.output.push(data);}, warn: function(data){this.output.push("WARN: "+data);}, error: function(data){this.output.push("ERROR: "+data);}, output: [], flushOutput: function(){var rtndata = this.output; this.output=[]; return rtndata;}};			
						
						window.wn_getAngularAppName = function(){
							if(typeof angular !== 'undefined'){
								return angular.element(document.body).injector().get('$rootElement').attr('ng-app');
							}
							return "No AngularJS app found."
							
						};
						
						window.wn_getAngularDeps = function(namespace){
							var deps = [];
							if(typeof angular !== 'undefined'){
								angular.forEach(angular.module(namespace).requires, function(m){deps.push(m);});
							}
							return deps;
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
						
						window.wn_contains_namespace = function(namespace, alldeps){
							angular.forEach(alldeps, function(m){
								if(m['namespace'] == namespace){
									return true;
								}
							});
							
							return false;
						};
						
						window.wn_showAngularAppName = function(){
							console.log('webnuke: AngularJS Main App Name');
							console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=');
							console.log(wn_getAngularAppName());
						};	
						
						window.wn_showAngularDeps = function (){
							console.log('webnuke: AngularJS Main Dependencies');
							console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=');
							console.log('<namespace>  |   <dependencies>');
							var deps = wn_getAllAngularDeps();
							for (var dep_record in deps){
								console.log(deps[dep_record].namespace+'  |   '+deps[dep_record].deps.join(', '));
							}
						};
						
						
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
						
						window.wn_getNgResourceClasses = function(){
							var resource_classes = [];
							var deps = wn_getAllAngularDeps();
							
							if(typeof angular !== 'undefined'){
								angular.forEach(deps, function(m){
									var contains_ngresource = false;
									angular.forEach(m['deps'], function(mm){
										if(mm == 'ngResource'){
											var namespace = m['namespace']
											
											var angular_classes = wn_getAngularClasses(namespace);
											angular.forEach(angular_classes, function(angular_classname){
												resource_classes.push(angular_classname['name']);
											});
										}
									});
								});
							}
							return resource_classes;
						};
						
						window.wn_testNgResourceClasses = function(){
							console.log('webnuke: AngularJS Testing ngResource Classes');
							console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-');
							var angular_classes = wn_getNgResourceClasses();

							if(typeof angular !== 'undefined'){
								angular.forEach(angular_classes, function(m){
									try {
										var classtotest = m;
										var res = angular.element(document.body).injector().get(classtotest);
										if(typeof res['get'] == 'function'){
											res.get({}, function(data){
												console.log("Received data for "+classtotest);
												//console.log(data);
											}, function(data){
												console.log("error receiving data for "+classtotest);
											});
										}
									}
									catch(err) {
										console.log("Error with '"+m+"' class - "+err.message);
									}
								});
								console.log('');
							}
						};
						
						window.wn_showAngularRoutes = function(){
							console.log('webnuke: AngularJS URL Routes');
							console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-');
							var mminjector = angular.element(document.body).injector()
							if(typeof mminjector !== 'undefined'){
								var mmstate = mminjector.get('$state')
								if(typeof mmstate !== 'undefined'){
									var routes = mmstate.get();
									routes.forEach(function(value){
										console.log('\tRoute: '+value.url+'\tController:'+value.controller);
									});
								}
							}
						};
						
						"""
		return javascript
