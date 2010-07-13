import os
import markdown


md = markdown.Markdown(extensions = ['meta'])

md.convertFile(input="source/about.md",
               output="content/about.html",
               encoding="utf8")


def get_article(meta):
    return { 'id': meta[u'id'][0],
             'title': meta['title'][0],
             'date': meta['date'][0]}

src_dir = 'source/articles'
out_dir = 'content/articles'
lst = []

f = open('articles.py', 'w')

for name in os.listdir(src_dir):
    md.convertFile(input = os.path.join(src_dir, name),
                   output = os.path.join(out_dir, name.replace('.md', '.html')),
                   encoding = 'utf8')
    print get_article(md.Meta)
    lst.append(get_article(md.Meta))

f.write(str(lst))                       # serialization, love Python :)

f.close()

print "Done."
