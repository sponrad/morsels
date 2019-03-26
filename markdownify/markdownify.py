import re

def markdownify(html):
    html = re.sub(r'<a href="(?P<url>[\w:\./]+)">(?P<text>[\w\s]+)</a>',
                  r'[\g<text>](\g<url>)',
                  html)
    return html.replace("\n", " ") \
               .replace("</p><p>", "\n\n").replace("<p>", "").replace("</p>", "") \
               .replace("<br>", "  \n") \
               .replace("<strong>", "**") \
               .replace("</strong>", "**")
