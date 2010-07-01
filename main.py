import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class HomePage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'markup/home.html')
        values = {}
        self.response.out.write(template.render(path, values))

class AboutPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'markup/about.html')
        values = {}
        self.response.out.write(template.render(path, values))


application = webapp.WSGIApplication([('/', HomePage),
                                      ('/about/', AboutPage)],
                                     debug=True);        

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
