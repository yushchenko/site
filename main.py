# print 'Content Type: text/plain'
# print ''
# print """Hi,
# Welcome to Valery Yushchenko's web site.
# Unfortunatelly, it's still under contruction... sorry for temporary inconvenience..."""

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'markup/index.html')
        values = {}
        self.response.out.write(template.render(path, values))


application = webapp.WSGIApplication([('/', MainPage)], debug=True);        


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
