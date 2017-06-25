from selenium.common.exceptions import WebDriverException

class HTMLCommands:
	def __init__(self, webdriver, jsinjector):
		self.version = 0.1
		self.driver = webdriver
		self.jsinjector = jsinjector
		
	def show_hidden_form_elements(self):
		self.jsinjector.execute_javascript(self.driver, 'wn_showHiddenFormElements()')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")

	def show_password_fields_as_text(self):
		self.jsinjector.execute_javascript(self.driver, 'wn_showPasswordFieldsAsText()')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")		

	def see_all_html_elements(self):
		self.jsinjector.execute_javascript(self.driver, 'wn_showAllHTMLElements()')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")		
		
