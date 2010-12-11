#! /usr/bin/python
import os
import markdown
import PyRSS2Gen

from datetime import datetime

os.chdir('site') # fix directory in Linux
URL_ROOT = 'http://www.yushchenko.name/'

# generating articles from Markdown
md = markdown.Markdown(extensions = ['meta'])

md.convertFile(input="content/about.md",
               output="markup/content/about.html",
               encoding="utf8")

src_dir = 'content/articles'
out_dir = 'markup/content/articles'
lst = []

def get_article(meta, out_file_name):
    dt = datetime.strptime(meta['date'][0], '%B %d, %Y') # July 10, 2010
    identifier = meta[u'id'][0]
    return {'id': identifier, 'title': meta['title'][0], 'status': meta['status'][0],
            'date': dt.strftime('%Y-%m-%d'), 'month': dt.strftime('%b'), 'day': dt.day, 'year': dt.year,
            'file': out_file_name, 'url': URL_ROOT + '/blog/' + identifier }

for name in os.listdir(src_dir):
    out_file_name = name.replace('.md', '.html')
    md.convertFile(input = os.path.join(src_dir, name),
                   output = os.path.join(out_dir, out_file_name),
                   encoding = 'utf8')
    
    article = get_article(md.Meta, out_file_name)

    if article['status'] == 'published' or article['status'] == 'draft':
        lst.append(get_article(md.Meta, out_file_name))

lst.sort(key = lambda a: a['date'], reverse = True)

# saving articles list to file
f = open('articles.py', 'w')
f.write('list = ' + str(lst))                       # serialization, love Python :)
f.close()

# Generation of RSS feed (rss.xml)
rss_items = []

for article in lst:
    rss_items.append(PyRSS2Gen.RSSItem(
         title = article['title'],
         link = article['url'],
         guid = PyRSS2Gen.Guid(article['url']),
         pubDate = datetime.strptime(article['date'], '%Y-%m-%d'))
    )

rss = PyRSS2Gen.RSS2(
    title = "Valery Yushchenko",
    link = URL_ROOT,
    description = "Articles by Valery Yushchenko",
    lastBuildDate = datetime.now(),
    items = rss_items
)

rss.write_xml(open("rss.xml", "w"))

print "Done."
