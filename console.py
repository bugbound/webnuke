#!/usr/bin/env python

# add owa to quickdetect - look for function IsOwaPremiumBrowser

from libs.utils.logger import *
from libs.mainmenu.mainframe import *		

logger = FileLogger()
logger.log('Webnuke started')

try:
	#webserver = webnuke_api_server(logger)
	#webserver.start()
	currently_not_used_local_proxy_port = 8008
	#webnukeproxy = ProxySupport("bah1", proxy_port, logger)
		
	mainwin = mainframe(logger, currently_not_used_local_proxy_port)
	mainwin.run_main()
except:
	logger.log('ERROR RUNNING WEBNUKE')
	raise
#finally:
	#webnukeproxy.stop()
	

logger.log('Webnuke finished')


		
