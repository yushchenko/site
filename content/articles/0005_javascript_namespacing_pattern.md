id:     javascript-namespacing-pattern
title:  A JavaScript Namespacing Pattern
date:   December 09, 2010
tags:   javascript,namespacing
status: draft

### Introduction

The simplest way to create namespace in JavaScript is variable declaration in global scope:

    var app = { ns: {}};
    app.ns.aFunction = function aFunction() (/*...*/};
    
Looks a bit clumsy even in a small example.
For a application with a couple of hundreds files it will make the code messy extremely fast
especially if several files should contribute in the same namespace.

For a real world app it would better to have a solution that fits the following basic requirements:

*   Concise and readable syntax, namespace should be declared before its content;
*   Ability to add members to the same namespace in several files;
*   Scope for private data and functions;
*   Simple and library independent implementation;

### A Just Another Solution

In fact, there are several well known patterns that simplify namespacing in JavaScript.
Right combination of them will provide a good way to solve the problem.

First, namespace creation should be done automatically on demand:

    ns('app.test.namespace');

This function parses namespace name and create appropriate chain of objects in global scope.
If the namespace already exists the function just returns it without damaging.

Next, created namespace should be filled with members in a convenient manner.
The [pattern][edwards] provided by James Edwards looks elegant and concise:

    (function () {

        var aPrivateMember = 'value';
     
        this.aNamespaceMember = function() {/*...*/};
    
    }).apply(ns('app.test.namespace'));

Anonymous function gives scope for private members and `this` is used as reference to the namespace.

Now lets give a final touch adding chaining.
It helps us to move namespace declaration at the beginning
and make the code a bit more readable hiding implementation details:

    ns('ns.test').extend(function () {

        var ctor = this.MyClass = function() {
            },
            secret = 'secret';  // private data

        ctor.prototype.getSecret = function getSecret() { // public method
            return secret;
        };
    });
    
### Micro Library

For the sake of convenience I have created a micro library which implements the discussed solution.

It's called ns.js and available [here on Github][source].

Feel free to contact with [me][about] if you have any suggestions.

### Links

1. [ns.js Micro Library on Github][source]
2. [Namespacing in JavaScript][croll] by Angus Croll
3. [My Favorite JavaScript Design Pattern][edwards] by James Edwards
4. [JavaScript Namespacing][michaux] by Peter Michaux


[source]: http://github.com/yushchenko/ns.js
[croll]: http://javascriptweblog.wordpress.com/2010/12/07/namespacing-in-javascript/
[edwards]: http://blogs.sitepoint.com/2010/11/30/my-favorite-javascript-design-pattern/
[michaux]: http://michaux.ca/articles/javascript-namespacing
[about]: /about/
