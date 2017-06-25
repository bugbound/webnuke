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
