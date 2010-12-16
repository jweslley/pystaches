import pystache
from pystaches import SyntaxHighlighter

class Python(pystache.View, SyntaxHighlighter):

  template_path = 'examples'

print Python().render()

