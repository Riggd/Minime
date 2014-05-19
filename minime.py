'''
MiniMe
v. 0.0.1
Derek Onay

Simple python program to minify CSS and JS files
'''
import time
import re

'''
Workflow for deleting spaces, further compression

for keyword in list
    readline find match
    if not in exception list
        from match to match2
            delete spaces
    else
        dont touch
'''
def css_keywords(list):
    list = "align-content align-items align-self animation animation-delay animation-direction animation-duration animation-fill-mode animation-iteration-count animation-name animation-play-state animation-timing-function backface-visibility background background-attachment background-clip background-color background-image background-origin background-position background-repeat background-size	border border-bottom border-bottom-color border-bottom-left-radius border-bottom-right-radius	border-bottom-style border-bottom-width border-collapse border-color border-image	border-image-outset	border-image-repeat	border-image-slice	border-image-source	border-image-width	border-left border-left-color border-left-style border-left-width border-radius	border-right border-right-color border-right-style border-right-width border-spacing	border-style border-top border-top-color border-top-left-radius	border-top-right-radius border-top-style border-top-width border-width bottom box-shadow	box-sizing	caption-side clear clip color column-count column-fill column-gap column-rule column-rule-color column-rule-style column-rule-width column-span column-width columns content counter-increment counter-reset cursor direction display empty-cells flex flex-basis flex-direction flex-flow flex-grow flex-shrink flex-wrap float font @font-face	font-family font-size font-size-adjust	font-stretch	font-style font-variant font-weight hanging-punctuation height icon justify-content @keyframes left letter-spacing line-height list-style list-style-image list-style-position list-style-type margin margin-bottom margin-left margin-right margin-top max-height max-width min-height min-width nav-down	nav-index	nav-left	nav-right	nav-up	opacity	order	outline outline-color outline-offset	outline-style outline-width overflow overflow-x	overflow-y	padding padding-bottom padding-left padding-right padding-top page-break-after page-break-before page-break-inside perspective perspective-origin position quotes resize	right tab-size table-layout text-align text-align-last text-decoration text-decoration-color text-decoration-line text-indent text-justify text-overflow	text-shadow	text-transform top transform transform-origin transform-style transition transition-delay transition-duration transition-property transition-timing-function unicode-bidi	vertical-align visibility white-space width word-break	word-spacing word-wrap	z-index"
    

def minime_css(filename):
    print 'Reading File'
    css_file = open(filename + '.css', 'r+')
    original_css = css_file.read()    
    time.sleep(1)
    
    print 'Removing Comments'
    converted_css = original_css    
    converted_css = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,converted_css) # remove all multi-line comments (/* COMMENT */)
    time.sleep(1)
    
    print 'Removing Linebreaks'
    converted_css = converted_css.replace('\n','')    
    time.sleep(1)
    
    print 'Removing Tabs'
    converted_css = converted_css.replace('\t','')
    converted_css = converted_css.replace('  ','')  
    converted_css = converted_css.replace('   ','')  
    converted_css = converted_css.replace('    ','') 
    time.sleep(1)
    
    print 'Removing Spaces'
    converted_css = re.sub(re.compile(":\s", re.DOTALL) , ":" ,converted_css) # remove all space after (:)
    converted_css = re.sub(re.compile(";\s", re.DOTALL) , ";" ,converted_css) # remove all space after (;)
    converted_css = re.sub(re.compile(",\s", re.DOTALL) , "," ,converted_css) # remove all space after (,)
    converted_css = re.sub(re.compile("{\s", re.DOTALL) , "{" ,converted_css) # remove all space after ({)
    converted_css = re.sub(re.compile("\s{", re.DOTALL) , "{" ,converted_css) # remove all space before ({)
    converted_css = re.sub(re.compile("}\s", re.DOTALL) , "}" ,converted_css) # remove all space after (})
    converted_css = re.sub(re.compile(";}", re.DOTALL) , "}" ,converted_css) # remove all last semicolons (;})
    time.sleep(1)    
    '''
    print 'Finding key words and removing correct spaces'
    keywords = []
    converted_css.find('transition', 'margin', 'padding'
    
    '''
    mini_file = open(filename + '.min.css', 'w')
    mini_file.write(converted_css)
    print 'MiniMe file created'
 
def minime_css_dict(filename):
    print 'Reading File'
    css_file = open(filename + '.css', 'r+')
    original_css = css_file.read()    
    time.sleep(1)
    
    print 'Removing Comments'
    converted_css = original_css    
    converted_css = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,converted_css) # remove all multi-line comments (/* COMMENT */)
    time.sleep(1)
    
    print 'Removing Linebreaks'
    converted_css = converted_css.replace('\n','')    
    time.sleep(1)
    
    print 'Removing Tabs'
    converted_css = converted_css.replace('\t','')
    converted_css = converted_css.replace('  ','')  
    converted_css = converted_css.replace('   ','')  
    converted_css = converted_css.replace('    ','') 
    time.sleep(1)
    
    print 'Removing Spaces'
    css_syntax = {'{','}',',',':',';'}
    #for syntax in css_syntax:
        #converted_css = re.sub(re.compile("%s\s", re.DOTALL) % syntax , syntax , converted_css)
        
    for syntax in css_syntax:
        converted_css = re.sub(re.compile("\s".join(syntax), re.DOTALL), syntax , converted_css)
    
    converted_css = re.sub(re.compile(";}", re.DOTALL) , "}" ,converted_css) # remove all last semicolons (;})
    time.sleep(1)
    
    '''
    print 'Finding key words and removing correct spaces'
    keywords = []
    converted_css.find('transition', 'margin', 'padding'
    
    '''
    mini_file = open(filename + '.min.css', 'w')
    mini_file.write(converted_css)
    print 'MiniMe file created' 
    
'''
Create a dictionary of all mathematical operators

" +  -  !=  ==  ===  =  ?  etc. "
'''
def minime_js(filename):
    print 'Reading File'
    js_file = open(filename + '.js', 'r+')
    original_js = js_file.read()    
    time.sleep(1)

    print 'Removing Comments'
    converted_js = original_js
    converted_js = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,converted_js) # remove all multi-line comments (/* COMMENT */)
    converted_js = re.sub(re.compile("(?<!\")\/\/.+?\n"),"" ,converted_js) # remove all single-line comments (//COMMENT) expect in quotes   
    time.sleep(1)
    
    print 'Removing Linebreaks'
    converted_js = converted_js.replace('\n','')    
    time.sleep(1)
    
    print 'Removing Tabs'
    converted_js = converted_js.replace('\t','')
    converted_js = converted_js.replace('    ','') 
    converted_js = converted_js.replace('  ','')
    time.sleep(1)
    
    print 'Removing Spaces'
    converted_js = re.sub(re.compile("\s=\s"),"=" ,converted_js) # remove all spaces before and after (=)
    converted_js = re.sub(re.compile("\s==\s"),"==" ,converted_js) # remove all spaces before and after (==)
    converted_js = re.sub(re.compile("\s===\s"),"==" ,converted_js) # remove all spaces before and after (===) and replace with (==)
    converted_js = re.sub(re.compile("\s\+\s"),"+" ,converted_js) # remove all spaces before and after (+)
    converted_js = re.sub(re.compile("\)\s"),")" ,converted_js) # remove all spaces after ())
    converted_js = re.sub(re.compile("\s\)"),")" ,converted_js) # remove all spaces before ())
    converted_js = re.sub(re.compile("(\(\s)"),"(" ,converted_js) # remove all spaces after ())
    converted_js = re.sub(re.compile("\s\("),"(" ,converted_js) # remove all spaces before ())
    converted_js = re.sub(re.compile("\s{\s"),"{" ,converted_js) # remove all spaces after ({)
    converted_js = re.sub(re.compile("\?\s"),"?" ,converted_js) # remove all spaces after (?)
    converted_js = re.sub(re.compile("\s\?"),"?" ,converted_js) # remove all spaces before (?)
    converted_js = re.sub(re.compile(",\s", re.DOTALL) ,"," ,converted_js) # remove all space after (,) 
    converted_js = re.sub(re.compile(":\s", re.DOTALL) ,":" ,converted_js) # remove all space after (:) |
    converted_js = re.sub(re.compile("\s&&\s", re.DOTALL) ,"&&" ,converted_js) # remove all space after (&&)
    converted_js = re.sub(re.compile("\s!=\s", re.DOTALL) ,"!=" ,converted_js) # remove all space after (!=)
    converted_js = re.sub(re.compile("\s\|\|\s", re.DOTALL) ,"||" ,converted_js) # remove all space after (||)
    time.sleep(1)
    
    mini_file = open(filename + '.min.js', 'w')
    mini_file.write(converted_js)
    print 'MiniMe file created'
    
file_type = raw_input('Please enter (1) for CSS file or (2) for Javascript file: ')

while True:
    if file_type == '1':
        filename = raw_input('Enter the name of the file without the extension: ')
        #minime_css(filename)
        minime_css_dict(filename)
        break
    elif file_type == '2':
        filename = raw_input('Enter the name of the file without the extension: ')
        minime_js(filename)
        break
    else:
        file_type = raw_input('Please enter (1) for CSS file or (2) for Javascript file: ')