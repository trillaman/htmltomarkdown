html_headers = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "h5": "##### ",
                "h6": "###### "}  # write_without_encloses
html_empty = {"hr": "***\n", "br": "\n"}  # write_empty_tags
text_modifiers = {"i": "*", "b": "__", "s": "~~"}

class Converter:
    #THOSE NEEDED
    def pat_unordered_li(self, tag_content):
        return "* " + str(tag_content) + "\n"

    def pat_ordered_li(self, index, tag_content):
        return str(index) + ". " + str(tag_content)

    def pat_text(self, tag_content):
        content = tag_content.replace("<p>", "")
        content = content.replace("</p>", "")
        return str(content)

    def trim_li_tags(self, string_to_trim):  # MAKE THIS UNIVERSAL LIKE (self, tag_to_trim, string_to_trim)
        content1 = str(string_to_trim)
        content1 = content1.replace("<li>", "")  # remove opening bold tag to get pure tag content
        content1 = content1.replace("</li>", "")

        return content1

    def check_children(self, content):
        content1 = str(content)
        if "<b>" in str(content1):  # for <i><b>content</b></i> so italic content can be also bolded
            content1 = content1.replace("<b>", "__")  # remove opening bold tag to get pure tag content
            content1 = content1.replace("</b>", "__")  # remove closing bold tag to get pure tag content
        if "<i>" in str(content):
            content1 = content1.replace("<i>", "*")  # remove opening bold tag to get pure tag content
            content1 = content1.replace("</i>", "*")  # remove closing bold tag to get pure tag content
        if "<s>" in str(content):
            content1 = content1.replace("<s>", "~~")  # remove opening bold tag to get pure tag content
            content1 = content1.replace("</s>", "~~")
        return content1






    def write_links(self, tag_text, tag_href):
        return "[" + str(tag_href) + "]" + "(" + str(tag_text) + ")" + "\n"

    def write_image(self, image_href, alt_text):
        return "![alt text]" + "(" + str(image_href) + " " + "\"" + str(alt_text) + "\"" + ")"

    def write_new_line(self):
        return str("\n")



    def write_html_empty(self, tag, content):
        if len(content) > 0:
            out = self.write_without_encloses(html_empty[tag.name],
                                              content)  # README OUTPUT TO MODIFY BY MODYFING WRITE_WITHOUT_ENCLOSES METHOD
        else:  # for empty content - so without text between > and <
            if tag == "img":  # check for images
                out = self.write_image(tag['src'], tag['alt'])
            out = self.write_without_encloses(html_empty[tag],
                                              "")  # if tag is not image then write normal tag  - README OUTPUT TO MODIFY BY MODYFING WRITE_WITHOUT_ENCLOSES METHOD
        return out

    def write_html_links(self, tag, content):
        out = self.write_links(tag, content)  # OUTPUT TO MODIFY BY MODYFING WRITE_LINKS METHOD
        return out

    def convert(self, tag, **kwargs):
        converted = ""

        if tag.name in html_empty:  # FOR HR AND BR
            converted = html_empty[tag.name]

        if tag.name == "ol":  # if ordered
            tag_child_list = tag.findAll('li')  # we need to find all li's inside
            i = 1
            for x in tag_child_list:  # for every li
                parsed_child = self.check_children(self.trim_li_tags(str(x)))  # we have to trim "li" tags and replace all inside tags with proper markdown tags
                converted += self.pat_ordered_li(i, parsed_child) + "\n"  # we are writing number of list element with parsed value
                i += 1
        elif tag.name == "ul":
            tag_child_list = tag.findAll('li')  # for every li
            for x in tag_child_list:
                parsed_child = self.check_children(self.trim_li_tags(str(x))) # we have to trim "li" tags and replace all inside tags with proper markdown tags
                converted += self.pat_unordered_li(parsed_child)  # and here we are writing parsed value
        else:
            if len(tag.get_text()) > 0:
                parsed_child = self.check_children(str(tag))
                converted += self.pat_text(parsed_child)
            #else:
                #parsed_output = self.convert(tag)
            #    converted = parsed_output
        '''
        if tag_img:
            converted = self.write_image(tag_img['src'], tag_img['alt'])  # BAD - SHOULD BE ONLY TAG , NOT TAG_NAME

        if key_list == html_headers:
            converted = self.write_without_encloses(html_headers[tag_name], tag_content[0])

        if key_list == html_with_closing_tag:
            converted = self.write_html_with_closing_tag(html_with_closing_tag[tag_name], tag_content[0])

        if tag.:
            # write_links(readme_output, str(tag.get('href')), tag.contents[0])
            converted = self.write_links(tag_href, tag_content[0])
        '''
        return converted
