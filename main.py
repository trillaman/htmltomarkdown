# Headers - done
# Horizontal Rule - done (changed)
# Lists - done
# Emphasis - done
# Links - done

# ![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
# Images - done

# Code and Syntax Highlighting - to do
# Tables - to do
# Blockquotes - to do
# Inline HTML - to do
# Line Breaks - to do
# YouTube Videos - to do

# TODO PYTHON SIDE:
# parameters as in/out file
# checking if files exists
# exceptions handling
# refactoring for cleaner code
# unit tests

from bs4 import BeautifulSoup
from converter import *


def main():
    try:
        html_file = open("index.html", "r")  # input file
    except Exception as ex:
        print("Error while opening source html for read" + str(ex))

    try:
        readme_output = open("readme_output.md", "w")  # output - readme_output.md
    except Exception as ex:
        print("Error while opening readme_output.md to write" +str(ex))

    if html_file:
        bsoup = BeautifulSoup(html_file, 'html.parser')  # parse input

    conv = Converter()

    # could be prettier - bsoup.prettify()
    # print(list(bsoup.children))

    for tag in list(bsoup.children):
        check_if_exists = conv.check_if_tag_exists_in_list(tag.name)
        if check_if_exists != -1:  # -1 means it doesn't exists in any list
            list_with_tag = conv.get_list_with_tag(tag.name, 0)  # returns list containing tag
            list_name_with_tag = conv.get_list_with_tag(tag.name, True)
            print("Exists in %s\n" % list_name_with_tag)
            print("List: %s\n" % list_with_tag)
            if tag.name == "img":
                converted_value = str(conv.convert(list_with_tag, tag.name, tag_content=tag.contents, tag_img=tag))
            elif tag.name == "a":
                converted_value = str(conv.convert(list_with_tag, tag.name, tag_content=tag.contents, tag_href=tag.get('href')))
            else:
                converted_value = str(conv.convert(list_with_tag, tag.name, tag_content=tag.contents))
            readme_output.write(converted_value)
        else:
            print("Not exists in any list\n")
            converted_value = ""
            pass

    html_file.close()  # close input file after use
    readme_output.close()  # close output file after use


if __name__ == "__main__":
    main()
    print("\n\nDone")
