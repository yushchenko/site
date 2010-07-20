id:     site-from-scratch-1-the-first-page
title:  Site from Scratch 1: The First Page
date:   July 31, 2010
tags:   site,development
status: draft


### Introduction

This article contains brief description of the first step on the long way of building my own site.
As usual, it's hard to start from blank page so let's make the first step short and create
the site that contains only one page with only one paragraph of text.
On the other hand, the first step should be done in the right direction
so our page will contain well formed HTML code generated by Django template
and styled with separate CSS style sheet.

### URLs

As according the old russian proverb a theater starts from the wardrobe, as a site starts from its URL.

First of all, the address should be as short as it possible, so own domain name is required.
Having spent a couple of hours for investigations, I decided to use [name.com](http://www.name.com).
I liked their relatively simple and fast site and also 'bike-to-work incentive program'
described in [the wikipedia article][name-com-wiki].
Our decisions are sometimes driven by strange motives, arn't they?

Next, the resource part of the URL should be short and verbose.
For example, link to this article should look something like this:

    site.name/blog/site-from-scratch-1-the-first-page

Short, helps to understand where we are now and even not so hard to type.

Requesting an url the user should get something, for example, a page or an image.
An url can point to a static file on server's hard drive.


In nutshell, the idea is very simple: get request, parse its URL to determine what the user wants to get
and prepare response executing server side code.
Inspite of the simplicity, this approach is extremely flexible, in fact, the response can contain
everything (static content, nicely formated data from a database, something from a web service etc).

Frankly speaking, using [Google App Engine][app-engine] it's hard to do otherwise, so I just have to configure it properly.

At the begining I created site directory and put there only two files: `app.yaml` and `main.py`.
`app.yaml` is the main configuration file and tells to App Engine what to do with incoming requests:

    - url: /.*                # take any request to the site
      script: main.py         # and run code from main.py to generate response

`main.py` file contains the simple Python code:

    print 'Content-Type: text/plain'   # let the browser know that it's getting simple text
    print ''
    print 'Hello, world!'              # return response content - the text itself



### Markup Generation

### Adding Styles

### Couple of Links



[app-engine]: http://appengine.google.com/ "Google App Engine"
[name-com-wiki]:http://en.wikipedia.org/wiki/Name.com "Wiki article about name.com"