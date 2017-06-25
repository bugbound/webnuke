window.wn_getAngularAppName = function(){
	if(typeof angular !== 'undefined'){
		return angular.element(document.body).injector().get('$rootElement').attr('ng-app');
	}
	return "No AngularJS app found."
	
};

window.wn_showAngularAppName = function(){
	console.log('webnuke: AngularJS Main App Name');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=');
	console.log(wn_getAngularAppName());
};	

