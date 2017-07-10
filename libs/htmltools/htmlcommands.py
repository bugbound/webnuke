from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
import time

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
		
	def click_everything(self):
		start_url = self.driver.current_url
		all_elements = self.driver.find_elements_by_xpath('//*')
		baseline_elements_count= len(all_elements)
		print "Found %d elements on page %s"%(baseline_elements_count, start_url)
		current_element_index=0
		
		doPageReload=False
		
		for currect_element_index in range(baseline_elements_count):
			if doPageReload:
				print "PAGE RELOAD"
				self.driver.get(start_url)
			
			try:
				doPageReload=False
				all_elements = self.driver.find_elements_by_xpath('//*')
				print "%d/%d"%(currect_element_index+1, len(all_elements)+1)
				current_element = all_elements[currect_element_index]
				current_element.click()
				#print 'Linktext: %s'%link_text
				#print ''
				time.sleep(3)
				
				
				if self.driver.current_url != start_url:
					print self.driver.current_url
					doPageReload = True
					
				# for speed, if we have same amount of elements on page then continue...
				after_click_elements =  self.driver.find_elements_by_xpath('//*')
				if doPageReload == False and len(all_elements) != len(after_click_elements):
					doPageReload=True
				
				
				
			except ElementNotInteractableException:
				# ignore these errors, just means we cant click this object!
				#print "ElementNotInteractableException"
				doPageReload = False
				pass
			except IndexError:
				# we had too little page elements compared to the first time on page
				give_or_take = 10
				if baseline_elements_count - len(all_elements) - give_or_take > 0:
					doPageReload=True
					pass
				else:
					break
			except StaleElementReferenceException:
				# something got out of hand so we force a page reload
				# hopefully we should not get too many of these errors!
				doPageReload = True
				print "!!!STALE!!!"
				pass
			except:
				print "Something unexpected happened"
				raise
		print ''
		raw_input("Press ENTER to return to menu.")
		
