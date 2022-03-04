html_headers = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "h5": "##### ",
                "h6": "###### "}  # write_without_encloses
html_empty = {"hr": "***\n", "br": "\n"}  # write_empty_tags
text_modifiers = {"i": "*", "b": "__", "s": "~~"}
text_tags = {"p": ""}

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

    def trim_tags(self, content):
        content1 = str(content)
        for i in range(0, len(html_headers)):
            content1 = content1.replace("<" + list(html_headers)[i] + ">", "")
            content1 = content1.replace("</" + list(html_headers)[i] + ">", "")

        return content1

    def pat_links(self, tag_text, tag_href):
        return "[" + str(tag_text) + "]" + "(" + str(tag_href) + ")" + "\n"

    def write_image(self, image_href, alt_text):
        return "![" + str(alt_text) + "]" + "(" + str(image_href) + ")"

    def write_new_line(self):
        return str("\n")

    def write_html_links(self, tag, content):
        out = self.write_links(tag, content)  # OUTPUT TO MODIFY BY MODYFING WRITE_LINKS METHOD
        return out

    def write_table_headers(self, tablehead):
        output = "\n"
        for x in range(0, len(tablehead)):
            if x == 0:
                first_header = tablehead[0].get_text()
                output += "| " + first_header + " | "
            else:
                header = tablehead[x].get_text()
                output += header + " | "

        output += "\n"

        for a in range(0, len(tablehead)):
            if a == 0:
                output += "| " + len(tablehead[a].get_text()) * "-" + " | "
            else:
                output += len(tablehead[a].get_text()) * "-" + " | "
        output += "\n"

        return output

    def write_table_data(self, tabledata):
        output = ""
        for x in range(0, len(tabledata)):
            if x == 0:
                first_data = tabledata[0].get_text()
                output += "| " + first_data + " | "
            else:
                first_data = tabledata[x].get_text()
                output += first_data + " | "

        return output

    def convert(self, tag, **kwargs):
        converted = ""


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

        elif tag.name == "img":
            converted = self.write_image(tag['src'], tag['alt'])  # BAD - SHOULD BE ONLY TAG , NOT TAG_NAME

        elif tag.name == "a":
            converted = self.pat_links(tag.get_text(), tag['href'])

        elif tag.name == "table":
            tag_child_headers = tag.findAll('th')
            tag_child_datarows = tag.findAll('td')

            converted = self.write_table_headers(tag_child_headers)
            converted += self.write_table_data(tag_child_datarows)

        else:
            if len(tag.get_text()) > 0 and tag.name in html_headers:
                parsed_child = self.check_children(str(tag))
                converted = str(html_headers[tag.name]) + self.trim_tags(parsed_child) + "\n"
            elif len(tag.get_text()) == 0 and tag.name in html_empty:
                converted = html_empty[tag.name]

        return converted
