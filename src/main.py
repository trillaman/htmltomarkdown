# Headers - to rewrite
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
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", help="input file path (html)", type=str)
parser.add_argument("output", help="output file path (for markdown)", type=str)

def main():
    args = parser.parse_args()
    try:
        html_file = open(args.input, "r")  # input file
        bsoup = BeautifulSoup(html_file, 'html.parser')  # parse input
    except Exception as ex:
        print("Error while opening source html for read" + str(ex))

    try:
        readme_output = open(args.output, "w")  # output - readme_output.md
    except Exception as ex:
        print("Error while opening %s to write" + str(ex) % str(args.output))

    conv = Converter()  # this class is responsible for all operations between html and markdown

    for tag in list(bsoup.children):

        if tag.name == "ol":  # if ordered
            tag_child_list = tag.findAll('li')  # we need to find all li's inside
            i = 1
            for x in tag_child_list:  # for every li
                parsed_child = conv.check_children(conv.trim_li_tags(str(x)))  # we have to trim "li" tags and replace all inside tags with proper markdown tags
                readme_output.write(conv.pat_ordered_li(i, parsed_child) + "\n")  # we are writing number of list element with parsed value
                i += 1
        elif tag.name == "ul":
            tag_child_list = tag.findAll('li')  # for every li
            for x in tag_child_list:
                parsed_child = conv.check_children(conv.trim_li_tags(str(x))) # we have to trim "li" tags and replace all inside tags with proper markdown tags
                readme_output.write(conv.pat_unordered_li(parsed_child))  # and here we are writing parsed value
        else:
            if len(tag.get_text()) > 0:
                parsed_child = conv.check_children(str(tag))
                readme_output.write(conv.pat_text(parsed_child))
            else:
                parsed_output = conv.convert(tag)
                readme_output.write(parsed_output)

    try:
        html_file.close()  # close input file after use
    except Exception as ex:
        print("Can't close the file with input" + str(ex))

    try:
        readme_output.close()  # close output file after use
    except Exception as ex:
        print("Can't close output file" + str(ex))


if __name__ == "__main__":
    main()
    print("\n\nDone")
