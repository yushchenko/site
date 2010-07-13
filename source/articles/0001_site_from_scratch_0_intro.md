id:     site-from-scratch-0-introduction
title:  Site from Scratch 0: Introduction
date:   July 10, 2010
tags:   site,development

### The Idea

I have been thinking about having own place in the Internet for many years.
Time was coming but the dream remained just a dream probably because it had never been the real necessity for me.
On the other hand, building of a site it's a big pile of problems for an unprepared person. 
One needs, for example, to register a domain, find a hosting, develop or adopt a site engine and so on.
This long list is limited only by creator's ambitions and imagination.


Why not to use existing solutions?
There are many fashionable Web 2.0 services which let anybody create and publish content.
Hundreds and thousands blog spots, wikis, social networks allow to share your writing, pictures, links, contacts...
Seems very simple but everything comes with its own price.

The first and the most important concern is *lack of control*.
Let imagine, I've established a blog on [blogger.com](http://www.blogger.com).
The first my question would be how to remove this ugly blue header from my pages.
I clearly understand that it's a part of the app but I simply don't want to have it up on my writings...
It could sound weird but as a developer I want fully control what reader's browser gets from the site.
Probably, it's due to hate to bloated software in general and bloated web sites in particular.

Next, every service has its own limitations. 
For instance, using blog it's extremely easy to publish articles and share photos.
But what should be done if I want to create a small JavaScript application to enrich my developer's portfolio? 
Use another service and link it? But I want put it *inside* my last article...

It could sound a bit strange but it's looks like that I'm willing to spend my time to get *exactly* what I want.
Not more but not less.

There are two ways to do so.
The first one is usage of an existing solution such as a CMS, blog engine etc.
Spend more or less time for studying it, set up required configuration, customize than fix several weird bugs...
It's a usual way how we do things at work, isn't it?
And this approach works really well while the solution is used how it was thought by its creator.
But a step aside costs much more than ten or even hundred steps forward.
So it's crucial to choose the right solution that fits one's needs as close as it's possible.
But right now I don't know precisely what I want to create.
Due to this reason I'm going to chose the second way - start from the blank sheet.

The last but not the least thing here is that simple fact
that creation of something from scratch can be extremely interesting.
Unfortunately or not, but it rarely happens when a programmer gets opportunity to do something on his own mind at work.
So I'm going to have a great fun developing at least own website.

### The Requirements

The major requirement is *simplicity*.
The simplest implementation is the best.
For example, the most widespread way of data representation is text format.
Why? Because it's simple.
So I'm going to keep all stuff editable in Emacs (replace it with your favorite editor)
unless it's really impractical (images is a good example).
By the way, text is not only simple but allows to see diffs (using a VCS is a good habit),
have several versions of the same article and easily or even automatically merge them
(yes, it's like dealing with source code, why not?) and use grep and other Unix utils. 
In addition, it helps keep my mind healthy because minimizes usage of M$ Word or other similar products
created for such called 'stupid users'.
Binary formats and databases are great only when they are used on proper place.

So keep everything simple including this 'requirements' letting  space for creativity.

### The Technologies

On client side life's simple.
I need only HTML, CSS and JavaScript. No Flash. No SilverLight.
Keep it simple, even primitive and it will work everywhere.
There is also a space for usage of existing JavaScript libraries, for example jQuery, to not reinvent the wheel.

On server-side there are much more options. Let's narrow them.
First of all, I love dynamic languages.
And it's a pain to switch between dynamic (JavaScript) and static (e.g. C# or Java) languages all the time.
For small application written by one person client and server sides should fit well.
Next, the language should be stable and have plenty of libraries.
Writing the one hundred first implementation of RSS is not so fascinating.
At the end, I'm too lazy to study a new language especially for project.
So there is only one candidate in the rest, it's [Python](http://www.python.org) programming language.

There is also hosting problem. 
I'm definitely not a system administrator, love rather create than thinker something.
So I would like to have set up and trouble-free hosting.
I thought that it's just an illusion until I found [Google App Engine](https://appengine.google.com/).
It's a great example of solving problem adding extra level of abstraction,
in this case, it's abstraction between a developer and a hosting.
And it supports Python as first class citizen so no way to escape, I'm catch.

### What next?

The answer is easy, as long way starts form the first step as a site begins form
[the first page](/blog/site-from-scratch-1-the-first-page).




