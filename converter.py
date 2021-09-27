html_headers = { "h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ","h5": "##### ", "h6": "###### ", "hr": "***"}
html_without_enclosing = { "hr": "***", "p": "", "img": "", "br": "" }

class Converter():
    def check_if_tag_exists_in_list(self, tag_name):
        if tag_name in html_headers:
            return 1
        else:
            return -1


    def convert(self, key_list, tag_name, tag_content):
        converted = ""
        if len(tag_content) > 0:
            converted = str(html_headers[tag_name] + tag_content + "\n")
        else:
            converted = str(html_headers[tag_name] + "\n")
        return converted

