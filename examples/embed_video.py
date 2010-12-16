import pystache
from pystaches import EmbedVideo

class EmbedVideo(pystache.View, EmbedVideo):

  self.linenos = True
  template_path = 'examples'

print EmbedVideo().render()

