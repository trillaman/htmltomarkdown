html_headers = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "h5": "##### ", "h6": "###### "} # write_without_encloses
html_empty = {"hr": "***", "br": ""} # write_empty_tags
html_without_closing_tag = {"img": "" }
html_with_closing_tag = {"p": "", "i": "*", "b": "__", "s": "~~"}
html_lists = {"ul": 0, "ol": 1}
html_links = {"a": ""}  # THIS IS SEPARATED BECAUSE NEEDS DIFFERENT BEHAVIOUR


class Converter():
    # METHODS FOR PROPER FORMATTING OUTPUT STRINGS

    def write_with_encloses(self, tag_name, tag_content): # FOR HTML_WITH_CLOSING_TAG
        return str(tag_name) + str(tag_content) + str(tag_name) + "\n"

    def write_without_encloses(self, tag_name, tag_content): # FOR HTML_HEADERS
        return str(tag_name) + str(tag_content) + "\n"

    def write_unordered_list(self, tag_content):
        return "* " + str(tag_content) + "\n"

    def write_ordered_list(self, index, tag_content):
        return str(index) + ". " + str(tag_content) + "\n"

    def write_empty_tags(self, tag): # FOR HTML_EMPTY
        return str(tag) + "\n"

    def write_links(self, tag_text, tag_href):
        return "[" + str(tag_text) + "]" + "(" + str(tag_href) + ")" + "\n"

    def write_italic_bold(self, tag_content):  # ITALIC UNDERSCORE **_content_**
        italic = "*" * 2
        return str(italic) + "_" + str(tag_content) + "_" + str(italic) + "\n"

    def write_image(self, image_href, alt_text):
        return "![alt text]" + "(" + str(image_href) + " \"" + alt_text + "\")"

    def write_new_line(self):
        return str("\n")

    # END OF STRING FORMATHING METHODS

    def check_if_tag_exists_in_list(self, tag_name):
        if tag_name in html_headers or tag_name in html_empty or tag_name in html_without_closing_tag or tag_name in html_with_closing_tag:
            return 1
        else:
            return -1

    def get_list_with_tag(self, tag, get_list_name):
        if tag in html_headers:
            list = html_headers
        elif tag in html_empty:
            list = html_empty
        elif tag in html_without_closing_tag:
            list = html_without_closing_tag
        elif tag in html_with_closing_tag:
            list = html_with_closing_tag
        if get_list_name == True:
            list = str(list)
        return list

    def write_html_with_closing_tag(self, tag, content): #THIS IS FOR ENCLOSED TAGS LIKE "<b>content</b>"
        if len(content) > 0:
            if "<b>" in str(content):  # for <i><b>content</b></i> so italic content can be also bolded
                content1 = str(content)
                content1 = content1.replace("<b>", "")  # remove opening bold tag to get pure tag content
                content1 = content1.replace("</b>", "")  # remove closing bold tag to get pure tag content
                out = self.write_italic_bold(content1)  # separated function for bolded italic - README OUTPUT TO MODIFY BY MODYFING WRITE_ITALIC_BOLD METHOD
            else:  # if not child but got contents - type enclosed tag in file
                out = self.write_with_encloses(tag, content) #README OUTPUT TO MODIFY BY MODYFING WRITE_WITH_ENCLOSES METHOD
        return out

    def write_html_empty(self, tag, content):
        if len(content) > 0:
            out = self.write_without_encloses(html_empty[tag.name], content) #README OUTPUT TO MODIFY BY MODYFING WRITE_WITHOUT_ENCLOSES METHOD
        else:  # for empty content - so without text between > and <
            if tag == "img":  # check for images
                out = self.write_image(tag['src'], tag['alt'])
            out = self.write_without_encloses(html_empty[tag], "")  # if tag is not image then write normal tag  - README OUTPUT TO MODIFY BY MODYFING WRITE_WITHOUT_ENCLOSES METHOD
        return out

    '''
    def write_html_lists(self, tag):
        if tag.name in html_lists:
            if tag.name == "ul":  # unordered
                for li in tag.findAll('li'):
                    if li.contents:
                        self.write_unordered_list(readme_output, li.contents[0]) #README OUTPUT TO MODIFY BY MODYFING WRITE_UNORDERED_LIST METHOD

        if tag.name == "ol":  # ordered
            index = 1
            for li in tag.findAll('li'):
                if li.contents:
                    self.write_ordered_list(readme_output, index, li.contents[0]) #README OUTPUT TO MODIFY BY MODYFING WRITE_ORDERED_LIST METHOD
                    index += 1

    def write_html_links(self, tag, content):
        return str( self.write_links(readme_output, tag.contents[0], str(tag.get('href'))) ) #README OUTPUT TO MODIFY BY MODYFING WRITE_LINKS METHOD

    '''

    def convert(self, key_list, tag_name, **kwargs):
        converted = ""
        tag_content = kwargs.get('tag_content') # REMEMBER THAT TAG_CONTENT IS tag.contents NOT tag.contents[0]
        # print(key_list)
        tag_img = kwargs.get('tag_img')
        if key_list == html_empty:  # FOR HR AND BR
            converted = self.write_empty_tags(html_empty[tag_name])

        if key_list == html_without_closing_tag:  # FOR IMG
            if tag_img:
                converted = self.write_image(tag_img['src'], tag_img['alt']) # BAD - SHOULD BE ONLY TAG , NOT TAG_NAME

        if key_list == html_headers:
            converted = self.write_without_encloses(html_headers[tag_name], tag_content[0])
        #    converted = str(key_list[tag_name] + "\n")

        if key_list == html_with_closing_tag:
            # converted = self.write_with_encloses(html_with_closing_tag[tag_name], tag_content[0])
            converted = self.write_html_with_closing_tag(html_with_closing_tag[tag_name], tag_content[0])
        return converted
