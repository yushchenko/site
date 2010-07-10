import markdown


md = markdown.Markdown(extensions = ['meta'])

md.convertFile(input="source/about.md",
               output="content/about.html",
               encoding="utf8")

md.convertFile(input="source/articles/0001_site_from_scratch_0_intro.md",
               output="content/articles/0001_site_from_scratch_0_intro.html",
               encoding="utf8")

# print md.Meta

print "Done."

