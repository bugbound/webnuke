window.wn_getAngularAppName = function(){
	if(typeof angular !== 'undefined'){
		var appname = '';
		rootelement = angular.element(document.body).injector().get('$rootElement');
		if(rootelement && rootelement.attr('ng-app')) {
			appname = rootelement.attr('ng-app');
		}
		if(rootelement && rootelement.attr('data-ng-app')) {
			appname = rootelement.attr('data-ng-app');
		}
		return appname;
	}
	return "No AngularJS app found."
	
};

window.wn_showAngularAppName = function(){
	console.log('webnuke: AngularJS Main App Name');
	console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=');
	console.log(wn_getAngularAppName());
};	

