import os
import re

import markdown

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# ~~~~~~~~~~~~~~~~~

def pyg(file):
	file = str(file).split('{')[1].split('}')[0]
	code = open('../rsc/snippets/' + file).read()
	return highlight(code, PythonLexer(), HtmlFormatter(linenos='table'))

def main():

	# collect all pages that need to be accounted for
	pages_dir = list(os.walk('../rsc/pages'))[0][2]
	page_files = list(filter(lambda x: x.split('.')[-1] == 'md', pages_dir))

	# load/generate various html bits
	HTML = open('./templates/html.html').read()
	menu_items = []
	for name in map(lambda x: x.split('.')[0], page_files):
		item = "<a href='{}'>{}</a>".format(name + '.html', name.upper())
		menu_items.append(item)

	# generate and save pages
	for file_name in page_files:
		cre = r'<p>\${.+}<\/p>'
		file = open('../rsc/pages/' + file_name).read()
		file = re.sub('\t', "•", file)
		html = markdown.markdown(file, extensions=['tables'])
		content = re.sub(cre, pyg, html)
		content = re.sub('•', "<span class='tab'></span>", content)
		page = HTML.format(menu_items=''.join(menu_items), content=content)

		new_file = file_name.split('.')[0] + '.html'
		open('../docs/' + new_file, 'w').write(page)


# ~~~~~~~~~~~~~~~~~

if __name__ == "__main__": main()


# <div class='tab'></div>