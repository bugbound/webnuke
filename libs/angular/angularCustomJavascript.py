class AngularCustomJavascript:
	def __init__(self, jsinjector):
		self.version = 0.1
		self.jsinjector = jsinjector
		self.jsinjector.add_help_topic('wn_showAngularAppName()', 'Show AngularJS Main Application Name')
		self.jsinjector.add_js_file('libs/angular/js/app-name.js')
		
		self.jsinjector.add_help_topic('wn_showAngularDeps()', 'Show AngularJS Main Dependencies')
		self.jsinjector.add_js_file('libs/angular/js/angular-deps.js')
		self.jsinjector.add_help_topic('wn_showAngularMainClasses()', 'Show AngularJS Main Classes')
		self.jsinjector.add_help_topic('wn_showAngularAllClasses()', 'Show AngularJS All Classes')
		self.jsinjector.add_js_file('libs/angular/js/angular-tools.js')
		self.jsinjector.add_help_topic('wn_testNgResourceClasses()', 'Test ngResource Classes')
		self.jsinjector.add_js_file('libs/angular/js/test-ngresource.js')
		self.jsinjector.add_help_topic('wn_showAngularRoutes()', 'Show AngularJS URL Routes')
		self.jsinjector.add_js_file('libs/angular/js/show-routes.js')
		
