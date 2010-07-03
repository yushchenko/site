import markdown


md = markdown.Markdown()
md.convertFile(input="markdown/0001_site_from_scratch_0_intro.md",
               output="markup/blog/0001_site_from_scratch_0_intro.html",
               encoding="utf8")

print "Done."

