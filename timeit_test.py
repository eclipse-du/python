#!/usr/bin/env python
# -*- coding: utf-8 -*-



#import timeit
from timeit import Timer
import random

t1 = Timer("root(2.)","from root import root")
print t1.timeit(10000)

for i in xrange(1,10):
	pass

print random.random()
print "hello"
print (1+(2*(3+4)))

