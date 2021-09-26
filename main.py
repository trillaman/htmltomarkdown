#Headers - done
#Horizontal Rule - done
#Lists - done

#Emphasis - to do

#Links - to do
#Images - to do
#Code and Syntax Highlighting - to do
#Tables - to do
#Blockquotes - to do
#Inline HTML - to do
#Line Breaks - to do
#YouTube Videos - to do

from bs4 import BeautifulSoup
import time
html_file = open("index.html", "r")
readme_output = open("readme_output.md", "w")

bsoup = BeautifulSoup(html_file, 'html.parser')

#TEST
output = bsoup.get_text()

html_without_enclosing = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ","h5": "##### ", "h6": "###### ", 
                     "hr": "---", "p": ""
                    }

html_with_enclosing = {"i": "*", "b": "__", "s": "~~"}

html_lists = {"ul": 0, "ol": 1}

html_hrefs = {"a": ""}


def write_with_encloses(filename, tag_name, tag_contents):
  filename.write(tag_name + tag_contents + tag_name + "\n")

def write_without_encloses(filename, tag_name, tag_contents):
  filename.write(tag_name + tag_contents + "\n")

def write_unordered_list(filename, tag_contents):
  filename.write("* " + tag_contents + "\n")

def write_ordered_list(filename, index, tag_contents):
  filename.write(str(index) + ". " + tag_contents + "\n")

def write_empty_tags(filename, tag):
  filename.write(tag)

def write_links(filename, tag1_contents, tag2_contents):
  filename.write("[" + tag1_contents + "]" + "("+ tag2_contents +")" + "\n")

#ITALIC UNDERSCORE **_content_**
def write_italic_bold(filename, tag_name, tag_contents):
  first_tag = "*" * 2
  filename.write(str(first_tag) + "_" + str(tag_contents) + "_" + str(first_tag) + "\n")

#TEST
#for row in output.splitlines():
#print(bsoup.prettify())

#print(list(bsoup.children))

bsoup.prettify()

#print(list(bsoup.children))

for tag in list(bsoup.children):
  #THIS VAR IS USED IN  CASE OF I AND B USED IN SAME TIME TO AVOID DUPLICATING
  bold_itallic_written = 0

  #below conditional compare dicts and if html_without_enclosing is true than it knows to no to add enclosing signs like *something*
  #THIS IS FOR NOTENCLOSED TAGS LIKE h1
  if tag.name in html_without_enclosing:
    #this writes to file corresponding markdown value for HTML tag
    if tag.contents:
      write_without_encloses(readme_output, html_without_enclosing[tag.name], tag.contents[0])        
    else:
      write_without_encloses(readme_output, html_without_enclosing[tag.name], "")

  #BELOW IS FOR ENCLOSED TAGS 
  if tag.name in html_with_enclosing:
    #THIS ONE SEARCH FOR CURSIVE AND BOLD EMPHASIS
    #print(list(tag.children))
    if tag.contents and len(list(tag.children)) == 0:
      write_with_encloses(readme_output, str(html_with_enclosing[tag.name]), str(tag.contents[0]))

    '''
    if tag.name == "i" and len(list(tag.children)) > 0:
      for ch in list(tag.children):
        write_italic_bold(readme_output, html_with_enclosing[tag.name], tag.children[0].contents[0])
    '''    
    #if tag.name == "i" and len(tag.contents) != 0 and "b" in list(tag.children)[0]:
    '''if tag.children[0].contents:
        write_italic_bold(readme_output, html_with_enclosing[bold.name], tag.children[0].contents[0])
        bold_itallic_written = 1  #assigning var to 1 to compare it and avoid duplicate <b> converting
    '''
    ''' elif tag.name == "i" and tag.contents == None:
        for bold in tag.findAll('b'):
          if bold.contents:
            write_italic_bold(readme_output, html_with_enclosing[bold.name], bold.contents[0])
    '''
    #here is this comparing and break is for going out from this loop and going to next line in index
    #if bold_itallic_written == 1:
    #  break
    #else:
    #  write_with_encloses(readme_output, html_with_enclosing[tag.name], tag.contents[0])

  #THIS ONE SEARCH FOR LISTS
  if tag.name in html_lists:
    if tag.name == "ul":
      for li in tag.findAll('li'):
        if li.contents:
          write_unordered_list(readme_output, li.contents[0])

    if tag.name == "ol":
      index = 1
      for li in tag.findAll('li'):
        if li.contents:
          write_ordered_list(readme_output, index, li.contents[0])
          index += 1

  if tag.name in html_hrefs:
    write_links(readme_output, str(tag.get('href')), tag.contents[0])
    
print("\n\nDone")

html_file.close()
readme_output.close()