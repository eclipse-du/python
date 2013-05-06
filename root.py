#!/usr/bin/python
#-*- coding:utf-8 -*-
# author  : eclipse
# email   : adooadoo@163.com
# filename: root.py

def root(x,iterMax = 5):
    """
    """
    s=1.0
    b=1
    for k in range(iterMax):
        s = 0.5 * (s + x/s)
    return s

print root(2.)
print root(2.,1)
