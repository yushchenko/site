import os
import markdown
from datetime import datetime

md = markdown.Markdown(extensions = ['meta'])

md.convertFile(input="content/about.md",
               output="markup/content/about.html",
               encoding="utf8")


src_dir = 'content/articles'
out_dir = 'markup/content/articles'
lst = []

def get_article(meta, out_file_name):
    dt = datetime.strptime(meta['date'][0], '%B %d, %Y') # July 10, 2010
    return {'id': meta[u'id'][0],'title': meta['title'][0], 'status': meta['status'][0],
            'date': dt.strftime('%Y-%m-%d'), 'month': dt.strftime('%b'), 'day': dt.day, 'year': dt.year,
            'file': out_file_name }

for name in os.listdir(src_dir):
    out_file_name = name.replace('.md', '.html')
    md.convertFile(input = os.path.join(src_dir, name),
                   output = os.path.join(out_dir, out_file_name),
                   encoding = 'utf8')
    
    article = get_article(md.Meta, out_file_name)

    if article['status'] == 'published' or article['status'] == 'draft':
        lst.append(get_article(md.Meta, out_file_name))

lst.sort(key = lambda a: a['date'], reverse = True)

f = open('articles.py', 'w')
f.write('list = ' + str(lst))                       # serialization, love Python :)
f.close()

print "Done."
