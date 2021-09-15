#Headers - done
#Horizontal Rule - done

#Emphasis - to do
#Lists - to do
#Links - to do
#Images - to do
#Code and Syntax Highlighting - to do
#Tables - to do
#Blockquotes - to do
#Inline HTML - to do
#Line Breaks - to do
#YouTube Videos - to do

from bs4 import BeautifulSoup

#Files programs use
html_file = open("index.html", "r")
readme_output = open("readme_output.md", "w")

bs = BeautifulSoup(html_file, 'html.parser')

def write_with_encloses(filename, tag_name, tag_contents):
  filename.write(tag_name + tag_contents + tag_name + "\n")

def write_without_encloses(filename, tag_name, tag_contents):
  filename.write(tag_name + tag_contents + "\n")

#enabled (0/1) - unordered/ordered
def write_lists(filename, index, enabled, tag_contents):
  if enabled == 0:
    filename.write("* " + tag_contents + "\n")
  if enabled == 1:
    filename.write(str(index) + ". " + tag_contents + "\n")
    #start_index += 1
  

html_without_enclosing = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ","h5": "##### ", "h6": "###### ", 
                     "hr": "---",
                    }
html_with_enclosing = {"i": "*", }
html_lists = {"ul": 0, "ol": 1}


'''
        if tag.name == "ul":
          ordered_list_enabled = 1
          if ordered_list_enabled == 1 and tag.contents:
            readme_output.write(ordered_list_number + ". " + tag.contents[0] + "\n")

''' 
for tag in bs.find_all():
    ordered_list_enabled = 0
    ordered_list_number = 1
  
    #below conditional compare dicts and if html_without_enclosing is true than it knows to no to add enclosing signs like *something*
    if tag.name in html_without_enclosing:
      #this writes to file corresponding markdown value for HTML tag
      if tag.contents:
        write_without_encloses(readme_output, html_without_enclosing[tag.name], tag.contents[0])        
      else:
        write_without_encloses(readme_output, html_without_enclosing[tag.name], "")
    elif tag.name in html_with_enclosing:
      if tag.contents:
        write_with_encloses(readme_output, html_with_enclosing[tag.name], tag.contents[0])
    elif tag.name in html_lists:
      if tag.name == "ul":
        print("UL FOUND")
        #INDEX SET ONLY FOR NOT BREAKING THE CODE
        index = 0
        for li in bs.findAll('li'):
          ordered_list_enabled = html_lists['ul']
          if tag.contents:
            #INDEX SET ONLY FOR NOT BREAKING THE CODE
            index = 0
            write_lists(readme_output, index, ordered_list_enabled, li.contents[0])
          else:
            pass
      elif tag.name == "ol":
        print("OL FOUND")
        index = 1
        for li in bs.findAll('li'):
          ordered_list_enabled = html_lists['ol']
          if tag.contents:
            write_lists(readme_output, index, ordered_list_enabled, li.contents[0])
            index += 1
          else:
            pass
        

print("Done")

html_file.close()
readme_output.close()