import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template


def path(name):
    return os.path.join(os.path.dirname(__file__), name)

def article_path(article):
    return os.path.join(os.path.dirname(__file__), 'markup/content/articles', article['file'])

class HomePage(webapp.RequestHandler):

    def get(self):

        import articles

        publishedArticles = [];

        for a in articles.list:
            if a['status'] == 'published':
                a['path'] = article_path(a)
                a['link'] = '/blog/' + a['id']
                a['content'] = template.render('markup/article.html', { 'article': a })
                publishedArticles.append(a);

        values = { 'articles': publishedArticles }
        
        self.response.out.write(template.render(path('markup/pages/home.html'), values))


class ArticlePage(webapp.RequestHandler):

    def get_article_by_id(self, id):

        import articles

        for a in articles.list:
            if  a['id'] == id:
                a['path'] = article_path(a)
                a['link'] = '/blog/' + a['id']
                return a

    def get(self, id):
        article =  self.get_article_by_id(id)
        self.response.out.write(template.render( path('markup/pages/article.html'),
                                                 {'article': article} ))


class AboutPage(webapp.RequestHandler):
    def get(self):
        values = {}
        self.response.out.write(template.render(path('markup/pages/about.html'), values))

class CssLayout(webapp.RequestHandler):
    def get(self):
        values = {}
        self.response.out.write(template.render(path('markup/sandbox/css_layout.html'), values))

application = webapp.WSGIApplication([
    ('/',             HomePage),
    ('/about/',       AboutPage),
    (r'/blog/(.*)',   ArticlePage),
    ('/sandbox/css-layout', CssLayout)
], debug=True);        


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
