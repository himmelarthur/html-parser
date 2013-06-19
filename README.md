html-parser
===========

A small but useful HTML Parser in Python that allows you to pick a special tag with its class !

Purpose
-------
html-parser is a tiny python module that can parse any HTML webpage (thanks to Python's urllib2) in order to find a particular tag with its name, or its name and its class.

The parser uses a Stack to benefit from the HTML structure : opening tags and their string position are pushed into the stacked, and popped out when their closing counterpart in encountered, the opening and closing position allows to select the tag's content and to store it into a list of hashtables.
Single-block tags (such as img, input, etc.) are stored with their attributes as their content.

It is made of a single function, getInsideHTMLTag, that takes one to three arguments :

* An **html string** : the content of an html file, gotten from a string, a distant website or a local file
* A **tag name** (such as a, div, span, iframe, etc.)
* A **class name** *(optional)* : allows you to *filter* the tags by a specific class
