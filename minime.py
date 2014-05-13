'''
MiniMe
v. 0.0.1
Derek Onay

Simple python program to minify CSS and JS files
'''
import time
import re

def minime_css(filename):
    print 'Reading File'
    css_file = open(filename + '.css', 'r+')
    original_css = css_file.read()    
    time.sleep(1)
    
    print 'Removing Linebreaks'
    converted_css = original_css.replace('\n','')    
    time.sleep(1)
    
    print 'Removing Tabs'
    converted_css = converted_css.replace('\t','')
    converted_css = converted_css.replace('    ','')    
    time.sleep(1)

    print 'Removing Comments'
    converted_css = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,converted_css) # remove all occurance streamed comments (/*COMMENT */) from string
    time.sleep(1)
    
    mini_file = open(filename + '.min.css', 'w')
    mini_file.write(converted_css)
    print 'MiniMe file created'

'''
def minime_js(filename):
    print 'Reading File'
    js_file = open(filename + '.js', 'r+')
    original_js = js_file.read()    
    time.sleep(1)
    
    print 'Removing Linebreaks'
    converted_js = original_js.replace('\n','')    
    time.sleep(1)
    
    print 'Removing Tabs'
    converted_js = converted_js.replace('\t','')
    converted_js = converted_js.replace('    ','')    
    time.sleep(1)

    print 'Removing Comments'
    converted_js = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,converted_js) # remove all multi-line comments (/*COMMENT */)
    converted_js = re.sub(re.compile("//.*?\n" ) ,"" ,converted_js) # remove all single-line comments (//COMMENT)
    time.sleep(1)
    
    mini_file = open(filename + '.min.js', 'w')
    mini_file.write(converted_js)
    print 'MiniMe file created'
'''
    
file_type = raw_input('Please enter (1) for CSS file or (2) for Javascript file: ')

while True:
    if file_type == '1':
        filename = raw_input('Enter the name of the file without the extension: ')
        minime_css(filename)
        break
    elif file_type == '2':
        filename = raw_input('Enter the name of the file without the extension: ')
        #minime_js(filename)
        break
    else:
        file_type = raw_input('Please enter (1) for CSS file or (2) for Javascript file: ')