import os
from google.appengine.ext.webapp import template

home_file = os.path.join(os.path.dirname(__file__), 'home.html')

print 'Content-Type: text/html'           # let the browser know that it's getting html
print ''
print template.render(home_file, {})      # return response content - the text itself


