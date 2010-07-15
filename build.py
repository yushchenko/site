import os
import markdown


md = markdown.Markdown(extensions = ['meta'])

md.convertFile(input="source/about.md",
               output="content/about.html",
               encoding="utf8")


src_dir = 'source/articles'
out_dir = 'content/articles'
lst = []

def get_article(meta, out_file_name):
    return {'id': meta[u'id'][0],'title': meta['title'][0], 'date': meta['date'][0],
            'file': out_file_name }

for name in os.listdir(src_dir):
    out_file_name = name.replace('.md', '.html')
    md.convertFile(input = os.path.join(src_dir, name),
                   output = os.path.join(out_dir, out_file_name),
                   encoding = 'utf8')
    
    lst.append(get_article(md.Meta, out_file_name))

f = open('articles.py', 'w')
f.write('list = ' + str(lst))                       # serialization, love Python :)
f.close()

print "Done."
