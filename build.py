import os
import markdown


md = markdown.Markdown(extensions = ['meta'])

md.convertFile(input="source/about.md",
               output="content/about.html",
               encoding="utf8")

# md.convertFile(input="source/articles/0001_site_from_scratch_0_intro.md",
#                output="content/articles/0001_site_from_scratch_0_intro.html",
#                encoding="utf8")

def get_article(meta):
    return { 'id': meta[u'id'][0],
             'title': meta['title'][0],
             'date': meta['date'][0]}

src_dir = 'source/articles'
out_dir = 'content/articles'

f = open('articles.py', 'w')
f.write('articles = [ ')

for name in os.listdir(src_dir):
    md.convertFile(input = os.path.join(src_dir, name),
                   output = os.path.join(out_dir, name.replace('.md', '.html')),
                   encoding = 'utf8')
    print md.Meta
    print get_article(md.Meta)
    f.write(str(get_article(md.Meta)))

f.write(' ]')
f.close()

print "Done."

