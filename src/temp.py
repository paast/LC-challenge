from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

code = open('../rsc/snippets/pygment_test.py').read()

head = "<head><link rel='stylesheet' href='index.css'></head>"

hl = highlight(code, PythonLexer(), HtmlFormatter(linenos='table', linespans='ln'))

open('../docs/index.html', 'w').write(head + hl)