Webnuke is a console based python application useful when pentesting web based applications.

To run:

python console.py

![webnuke main gui](http://bugbound.co.uk/sites/default/files/webnuke%20mainscreen.png?19)

Detect technologies in use not by parsing files or applying regex to file names but from Javascript variables and html elements on the page.
![quickdetect - Wordpress and jQuery](http://bugbound.co.uk/sites/default/files/webnuke-quickdetect.png)

![quickdetect - Drupal CMS](http://bugbound.co.uk/sites/default/files/webnuke-drupal.png)



## JSCONSOLE

The jsconsole option allows you to execute javascript or run internal webnuke javascript.

### Demo:
```javascript
var msg="hello world";
alert(msg);
@@@
'''

### Internal commands
wn_help() - Shows WebNuke Help
wn_findMethodsOfThis() - print javascript methods
wn_getMethodsPlusCode() - print javascript methods and code
wn_getFunctions() - returns array of javascript functions
wn_listFunctions() - print javascript function names
wn_findStringsWithUrls() - Try and locate urls within Javascript strings
wn_showHiddenFormElements() - Show hidden form elements in the browser
wn_showPasswordFieldsAsText() - Show password fields as text in the browser
wn_showAllHTMLElements() - Set CSS visibility to visible on all HTML elements in the browser
wn_showAngularAppName() - Show AngularJS Main Application Name
wn_showAngularDeps() - Show AngularJS Main Dependencies
wn_showAngularMainClasses() - Show AngularJS Main Classes
wn_showAngularAllClasses() - Show AngularJS All Classes
wn_testNgResourceClasses() - Test ngResource Classes
wn_showAngularRoutes() - Show AngularJS URL Routes


