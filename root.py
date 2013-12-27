#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author  : eclipse


def root(x,debug = False,iterMax = 100):
    """
    root for none-negative number
    """
    if x==0:
        return 0
    elif x<0:
        print "***Erro,x must be nonnegative"
        return None
    assert x>0. and type(x) is float or int ,"Unrecognized input"
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

def test():
    from numpy import sqrt
    xvalues = [0.,2.,100.,10000.,1.e-4]
    for x in xvalues:
        print "Testing with x = %20.15e" % x
        s = root(x)
        s_numpy = sqrt(x)
        print " s = %20.15e, numpy.sqrt = %20.15e" \
              % (s,s_numpy)
        assert abs(s - s_numpy)<1e-14,\
               "Disagree for x = %20.15e" % x
if __name__ == "__main__":
    print "Running test."
    test()
