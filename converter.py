html_headers = { "h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ","h5": "##### ", "h6": "###### " }
html_without_enclosing = { "hr": "***", "p": "", "img": "", "br": "" }

class Converter():
    def check_if_tag_exists_in_list(self, tag_name):
        if tag_name in html_headers or tag_name in html_without_enclosing:
            return 1
        else:
            return -1

    def get_list_with_tag(self, tag_name):
        if tag_name in html_headers:
             list = html_headers
        elif tag_name in html_without_enclosing:
             list = html_without_enclosing
        return list

    def convert(self, key_list, tag_name, tag_content):
        converted = ""
        if len(tag_content) > 0:
            converted = str(key_list[tag_name] + tag_content + "\n")
        else:
            converted = str(key_list[tag_name] + "\n")
        return converted

