# Headers - done
# Horizontal Rule - done (changed)
# Lists - done
# Emphasis - done
# Links - done

# ![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
# Images - done

# Code and Syntax Highlighting - to do
# Tables - done
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
        readme_output.write(conv.convert(tag))

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
