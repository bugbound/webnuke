window.wn_hasNormalRouting = function(){
	var mminjector = angular.element(document.body).injector()
	try{
		if(typeof mminjector !== 'undefined'){
			var mmstate = mminjector.get('$state')
			if(typeof mmstate !== 'undefined')
				return true;
		}
	}
	catch(err){}
	return false;
};

window.wn_hasNgComponentRouterRouting = function(){
	var mminjector = angular.element(document.body).injector()
	try{
		if(typeof mminjector !== 'undefined'){
			var mmstate = mminjector.get('$rootRouter')
			if(typeof mmstate !== 'undefined')
				return true;
		}
	}
	catch(err){}
	return false;
};



window.wn_showAngularRoutes = function(){
	if(window.wn_hasNormalRouting())
		window.wn_showNormalAngularRoutes();
	if(window.wn_hasNgComponentRouterRouting())
		window.wn_show_routes_from_ngComponentRouter();
	
};


window.wn_showNormalAngularRoutes = function(){
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


window.wn_show_routes_from_ngComponentRouter = function(){
	console.log('webnuke: AngularJS URL Routes - ngComponentRouter');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-');
	var mminjector = angular.element(document.body).injector()
	if(typeof mminjector !== 'undefined'){
		var mmstate = mminjector.get('$rootRouter')
		if(typeof mmstate !== 'undefined'){
			var routes = mmstate._childRouter.registry._rules;
			routes.forEach(function(value, key, map){
				console.log(`${key}`);
				value.rules.forEach(function(rule){
					console.log('\tRoute: '+rule.path)
					});
				});	
		}
	}	
};

