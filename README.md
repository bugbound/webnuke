Webnuke is a console based python application useful when pentesting web based applications.

To run:

python console.py

![webnuke main gui](http://bugbound.co.uk/sites/default/files/webnuke%20mainscreen.png?19)

Detect technologies in use not by parsing files or applying regex to file names but from Javascript variables and html elements on the page.
![quickdetect - Wordpress and jQuery](http://bugbound.co.uk/sites/default/files/webnuke-quickdetect.png)

![quickdetect - Drupal CMS](http://bugbound.co.uk/sites/default/files/webnuke-drupal.png)



## JSCONSOLE

The jsconsole option allows you to execute javascript or run internal webnuke javascript.

Enter the Javascript to run and start a new line with @@@ to execute in the browser

### Demo:
```javascript
var msg="hello world";
alert(msg);
@@@
```

### To escape back to menu
```javascript
quit()
@@@
```


### Internal Webnuke Javascript Functions
```
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
```

## HTML tools menu

The HTML tools can be used to expose hidden form elements and can also control the browser by clicking every HTML elements on the page. 

The click every element option can take abit of time to complete but can be helpful flushing out urls for the site.

The type 'test' option is useful when dealing with Ajax calls.
                                        
### HTML Options                                                                        
1. Show hidden form elements                                    
2. Turn password fields into text                                         
3. Turn css visibility on for all HTML elements                           
4. Click every element on the page                                        
5. Type 'test' into every text box


## javascript

### Javascript Options
                                                                              
1. Find URLS within Javascript Global Properties                          
2. Show Javascript functions of Document                                  
3. Run all js functions without args  
