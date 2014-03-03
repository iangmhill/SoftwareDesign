# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:17:42 2014

@author: ihill
"""

from re import findall

f = open('mary_had_a_little_lamb.txt','r')
book = f.read()
#book = [(book.index(" ***")+ 4):(book.index("*** END OF THIS PROJECT GUTENBERG EBOOK")-1)]
print findall("[a-zA-Z']+",book)
f.close()
