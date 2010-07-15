import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template


def path(name):
    return os.path.join(os.path.dirname(__file__), name)

class HomePage(webapp.RequestHandler):
    def get(self):

        import articles

        for article in articles.list:
            article_template_path = os.path.join(os.path.dirname(__file__), 'content/articles', article['file'])
            article['content'] = template.render(article_template_path, article)

        values = { 'articles': articles.list }
        
        self.response.out.write(template.render(path('templates/home.html'), values))

class AboutPage(webapp.RequestHandler):
    def get(self):
        values = {}
        self.response.out.write(template.render(path('templates/about.html'), values))


application = webapp.WSGIApplication([('/', HomePage),
                                      ('/about/', AboutPage)],
                                     debug=True);        

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
