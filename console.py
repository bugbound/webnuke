#!/usr/bin/env python
# add owa to quickdetect - look for function IsOwaPremiumBrowser

from libs.utils.logger import *
from libs.mainmenu.mainframe import *		

if __name__ == '__main__':
	log_file = FileLogger()
	log_file.log('Webnuke started.')
	
	try:		
		mainframe(log_file).show_main_screen()
	except:
		log_file.log('ERROR RUNNING WEBNUKE.')
		raise
		
	log_file.log('Webnuke finished.')


		
