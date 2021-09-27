#Headers - done
#Horizontal Rule - done (changed)
#Lists - done
#Emphasis - done
#Links - done

#![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
#Images - done

#Code and Syntax Highlighting - to do
#Tables - to do
#Blockquotes - to do
#Inline HTML - to do
#Line Breaks - to do
#YouTube Videos - to do

#TODO PYTHON SIDE:
      # exceptions handling
      # refactoring for cleaner code

from bs4 import BeautifulSoup
import time

html_without_enclosing = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ","h5": "##### ", "h6": "###### ", 
                     "hr": "***", "p": "", "img": ""
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

def write_image(filename, image_href, alt_text):
  filename.write("![alt text]" + "(" + image_href + " \"" + alt_text + "\")")



def main():
  html_file = open("index.html", "r")     #input file
  readme_output = open("readme_output.md", "w")     #output - readme_output.md

  bsoup = BeautifulSoup(html_file, 'html.parser')     #parse input

  #could be prettier - bsoup.prettify()
  #print(list(bsoup.children))

  for tag in list(bsoup.children):      #THIS NEED TO BE REFACTORED
    if tag.name in html_without_enclosing:
      if tag.contents:
        write_without_encloses(readme_output, html_without_enclosing[tag.name], tag.contents[0])
      else: #for empty content - so without text between > and <
        if tag.name == "img": #check for images
          write_image(readme_output, tag['src'], tag['alt'])
        write_without_encloses(readme_output, html_without_enclosing[tag.name], "")     #if tag is not image then write normal tag

    #BELOW IS FOR ENCLOSED TAGS LIKE "<b>content</b>"
    if tag.name in html_with_enclosing:
      if tag.contents:
        for ch in tag.contents:     #ch for child
          if "<b>" in str(ch):      #for <i><b>content</b></i> so italic content can be also bolded
            content = str(tag.contents[0])
            content = content.replace("<b>", "")      #remove opening bold tag to get pure tag content
            content = content.replace("</b>", "")     #remove closing bold tag to get pure tag content
            write_italic_bold(readme_output, html_with_enclosing[tag.name], content)      #separated function for bolded italic
          else:     #if not child but got contents - type enclosed tag in file
            write_with_encloses(readme_output, str(html_with_enclosing[tag.name]), str(tag.contents[0]))

    #THIS ONE SEARCH FOR LISTS
    if tag.name in html_lists:
      if tag.name == "ul":      #unordered
        for li in tag.findAll('li'):
          if li.contents:
            write_unordered_list(readme_output, li.contents[0])

      if tag.name == "ol":      #ordered
        index = 1
        for li in tag.findAll('li'):
          if li.contents:
            write_ordered_list(readme_output, index, li.contents[0])
            index += 1

    #THIS ONE FOR HYPERLINKS
    if tag.name in html_hrefs:
      write_links(readme_output, str(tag.get('href')), tag.contents[0])
    
  html_file.close()   #close input file after use
  readme_output.close()     #close output file after use

if __name__ == "__main__":
  main()
  print("\n\nDone")