import re

def normalize(slug, html):
    # Remove all whitespace after html tags
    html = re.sub(r'>\s+(\S)', r'>\1', html)
    # Remove all whitespace before html tags
    html = re.sub(r'(\S)\s+<', r'\1<', html)
    return html
