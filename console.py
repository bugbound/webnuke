#!/usr/bin/env python

# add owa to quickdetect - look for function IsOwaPremiumBrowser

from libs.utils.logger import *
from libs.mainmenu.mainframe import *		

logger = FileLogger()
logger.log('Webnuke started')

try:		
	mainwin = mainframe(logger)
	mainwin.run_main()
except:
	logger.log('ERROR RUNNING WEBNUKE')
	raise
	

logger.log('Webnuke finished')


		
