import os
import re

import markdown

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# ~~~~~~~~~~~~~~~~~

# html = markdown.markdown(open('../rsc/pages/test.md').read(), extensions=['tables'])

# Need to replace ${filename} tags with the actual code blocks generated
# by pygments. Also need to wrap it all in a legit html document + css.

# open('../docs/index.html', 'w').write(html)

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
		item = "<li><a href='{}'>{}</li>".format(name, name.upper())
		menu_items.append(item)

	# generate pages
	for file_name in page_files:
		cre = r'\${.+}'
		file = open('../rsc/pages/' + file_name).read()
		content = re.sub(cre, pyg, file)
		page = HTML.format(menu_items=''.join(menu_items), content=content)

		new_file = file_name.split('.')[0] + '.html'
		open('../docs/' + new_file, 'w').write(page)




if __name__ == "__main__": main()
