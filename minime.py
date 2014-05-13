'''
MiniMe
v. 0.0.1
Derek Onay

Simple python program to minify CSS and JS files
'''
import time

file_type = raw_input('Please enter (1) for CSS file or (2) for Javascript file: ')

if file_type == '1':
    filename = raw_input('Enter the name of the file without the extension: ')
elif file_type == '2':
    filename = raw_input('Enter the name of the file without the extension: ')
else:
    file_type = raw_input('Please enter (1) for CSS file or (2) for Javascript file: ')
    
def minify_css(filename):
    css_file = open(filename + '.css', 'r+')
    original_css = css_file.read()
    print 'File Read'
    time.sleep(2)
    converted_css = original_css.replace('\n',' ')
    print 'Replacing new line'
    converted_css = converted_css.replace('    ','')
    print 'Replacing tabs'
    time.sleep(3)
    mini_file = open(filename + '.min.css', 'w')
    mini_file.write(converted_css)
    print 'Minime file created'
    
minify_css(filename)