#!/usr/bin/python
#-*- coding:utf-8 -*-
# author  : eclipse
# email   : adooadoo@163.com
# filename: root.py

def root(x,debug = False,iterMax = 100):
    """
    """
    s=1.0
    tol = 1.e-14
    for k in range(iterMax):
        s1 = s
        s = 0.5 * (s + x/s)
        if debug:
            print "Before iteration %s,s=%20.15f" %(k,s)
        if abs((s-s1)/x) < tol:
            return s
    return s

print root(2.,True)
