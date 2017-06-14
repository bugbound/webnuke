# webnuke
# load website and search for any vars with the name url in to detech any api calls from javascript/angularjs
"""Usage: 
	webnuke.py [--debug] <url> 
	webnuke.py -h | --help
	webnuke.py --version

Arguments:
	<url>          Website url to nuke...
	
Options:
	-h --help      show this
	--debug        shows debugging goodness such as browser window
	--version      shows the current version
	
Examples:
	webnuke.py http://www.your.website/
	webnuke.py http://www.your.website/wp-admin/
	
"""

from docopt import docopt
from libs.mainclasses import *

if __name__ == '__main__':
    arguments = docopt(__doc__, version='webnuke 0.1')
    #print(arguments)
    url = arguments['<url>']
    debug = arguments['--debug']
    ops = OpCenter()
    ops.setDebug(debug)
    ops.addUrl(url)
    ops.activate()
