html_headers = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "h5": "##### ", "h6": "###### "}  # write_without_encloses
html_empty = {"hr": "***", "br": " "}  # write_empty_tags
html_without_closing_tag = {"img": ""}
html_with_closing_tag = {"p": "", "i": "*", "b": "__", "s": "~~"}
html_lists = {"ul": 0, "ol": 1}
html_links = {"a": ""}  # THIS IS SEPARATED BECAUSE NEEDS DIFFERENT BEHAVIOUR


def write_with_encloses(tag_name, tag_content):  # FOR HTML_WITH_CLOSING_TAG
    return str(tag_name) + str(tag_content) + str(tag_name) + "\n"


class Converter:
    # METHODS FOR PROPER FORMATTING OUTPUT STRINGS

    def write_without_encloses(self, tag_name, tag_content):  # FOR HTML_HEADERS
        return str(tag_name) + str(tag_content) + "\n"

    def write_unordered_list(self, tag_content):
        return "* " + str(tag_content) + "\n"

    def write_ordered_list(self, index, tag_content):
        return str(index) + ". " + str(tag_content) + "\n"

    def write_empty_tags(self, tag):  # FOR HTML_EMPTY
        if tag == "br":
            return "\n"
        else:
            return str(tag) + 2 *"\n"

    def write_links(self, tag_text, tag_href):
        return "[" + str(tag_href) + "]" + "(" + str(tag_text) + ")" + "\n"

    def write_italic_bold(self, tag_content):  # ITALIC UNDERSCORE **_content_**
        italic = "*" * 2
        return str(italic) + "_" + str(tag_content) + "_" + str(italic) + "\n"

    def write_image(self, image_href, alt_text):
        return "![alt text]" + "(" + str(image_href) + " " + "\"" + str(alt_text) + "\"" + ")"

    def write_new_line(self):
        return str("\n")

    def trim_li_tags(self, string_to_trim):  # MAKE THIS UNIVERSAL LIKE (self, tag_to_trim, string_to_trim)
        content1 = str(string_to_trim)
        content1 = content1.replace("<li>", "")  # remove opening bold tag to get pure tag content
        content1 = content1.replace("</li>", "")

        return content1
    # END OF STRING FORMATHING METHODS

    def get_list_with_tag(self, tag, get_list_name):
        list = ""
        if tag in html_headers:
            list = html_headers
        elif tag in html_empty:
            list = html_empty
        elif tag in html_without_closing_tag:
            list = html_without_closing_tag
        elif tag in html_with_closing_tag:
            list = html_with_closing_tag
        elif tag in html_links:
            list = html_links
        elif tag in html_lists:
            list = html_lists
        if get_list_name is True:
            list = str(list)
        return list


    def write_html_with_closing_tag(self, tag, content):  # THIS IS FOR ENCLOSED TAGS LIKE "<b>content</b>"
        if len(content) > 0:
            if "<b>" in str(content):  # for <i><b>content</b></i> so italic content can be also bolded
                content1 = str(content)
                content1 = content1.replace("<b>", "")  # remove opening bold tag to get pure tag content
                content1 = content1.replace("</b>", "")  # remove closing bold tag to get pure tag content
                out = self.write_italic_bold(content1)  # separated function for bolded italic - README OUTPUT TO MODIFY BY MODYFING WRITE_ITALIC_BOLD METHOD
            else:  # if not child but got contents - type enclosed tag in file
                out = write_with_encloses(tag, content)  # README OUTPUT TO MODIFY BY MODYFING WRITE_WITH_ENCLOSES METHOD
        return out

    def write_html_empty(self, tag, content):
        if len(content) > 0:
            out = self.write_without_encloses(html_empty[tag.name], content) # README OUTPUT TO MODIFY BY MODYFING WRITE_WITHOUT_ENCLOSES METHOD
        else:  # for empty content - so without text between > and <
            if tag == "img":  # check for images
                out = self.write_image(tag['src'], tag['alt'])
            out = self.write_without_encloses(html_empty[tag], "")  # if tag is not image then write normal tag  - README OUTPUT TO MODIFY BY MODYFING WRITE_WITHOUT_ENCLOSES METHOD
        return out

    def write_html_links(self, tag, content):
        out = self.write_links(tag, content)  # OUTPUT TO MODIFY BY MODYFING WRITE_LINKS METHOD
        return out

    def convert(self, key_list, tag_name, **kwargs):
        converted = ""
        tag_content = kwargs.get('tag_content')  # REMEMBER THAT TAG_CONTENT IS tag.contents NOT tag.contents[0]
        # print(key_list)
        tag_href = kwargs.get('tag_href')
        tag_img = kwargs.get('tag_img')
        tag_index = kwargs.get('tag_index')
        li_children = kwargs.get('list_children')

        if key_list == html_empty:  # FOR HR AND BR
            converted = self.write_empty_tags(html_empty[tag_name])

        if tag_img:
            converted = self.write_image(tag_img['src'], tag_img['alt'])  # BAD - SHOULD BE ONLY TAG , NOT TAG_NAME

        if key_list == html_headers:
            converted = self.write_without_encloses(html_headers[tag_name], tag_content[0])

        if key_list == html_with_closing_tag:
            converted = self.write_html_with_closing_tag(html_with_closing_tag[tag_name], tag_content[0])

        if key_list == html_links:
            # write_links(readme_output, str(tag.get('href')), tag.contents[0])
            converted = self.write_links(tag_href, tag_content[0])

        if key_list == html_lists:
            if tag_index:
                li_index = 0
                while (tag_index <= len(li_children)):
                    converted += str(self.write_ordered_list(tag_index, self.trim_li_tags(li_children[li_index])))
                    tag_index += 1
                    li_index += 1
            else:
                li_index = 0
                while (li_index < len(li_children)):
                    converted += str(self.write_unordered_list((self.trim_li_tags(li_children[li_index]))))
                    li_index += 1
        return converted
