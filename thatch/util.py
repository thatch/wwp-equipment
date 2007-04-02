"""
Some basic utilities I find myself rewriting a lot
"""

__author__ = "Tim Hatch <tim@timhatch.com>"
__revision__ = "$Rev: 433 $"[6:-2]
__date__  = "$Date: 2006-03-17 21:29:34 -0600 (Fri, 17 Mar 2006) $"[7:-2]
__copyright__ = "Copyright (c) 2006 Tim Hatch"
__license__ = "BSD"
__all__ = ["alloc2d", "swapdict", "swaplist", "sublist", "rmkdir"]


import os

def alloc2d(x,y,iv=0):
    """
    Allocate a 2-dimensional array, with the specified
    initial value.  May do weird things with objects, I'm not sure.

    >>> alloc2d(2,5)
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    >>> alloc2d(2,2,"x")
    [['x', 'x'], ['x', 'x']]

    """
    return [[iv for j in range(int(x))] for i in range(int(y))]
    
def swapdict(d):
    """
    Swap around the keys and values of a dictionary (i.e. flip on the diagonal)
    
    >>> d = {"a": 1, "b": 2, "c": "blah"}
    >>> swapdict(d)
    {1: 'a', 2: 'b', 'blah': 'c'}
    >>> swapdict(swapdict(d)) == d #invertable
    True
    >>> swapdict({})
    {}
    """
    x = {}
    for k, v in d.iteritems():
        x[v] = k
    return x

def swaplist(l, base=0):
    """
    Swap the values and indices of a list.  Values default to None if something
    is doubled up and not specified.  Values should be numbers, because they
    will become indices!
    
    >>> el = [0,4,1,3,2] #basic list
    >>> swaplist(el)
    [0, 2, 4, 3, 1]
    >>> swaplist(swaplist(el)) == el # invertable
    True
    >>> swaplist([0, 1, 2]) #already match
    [0, 1, 2]
    >>> swaplist([1, 2, 3], 1) #already match, just one based
    [1, 2, 3]
    >>> swaplist([3, 2, 1], 1)
    [3, 2, 1]
    >>> swaplist([1, 1, 1]) #kinda undefined, but at least works.  Last one wins -- effectively el[2] = 1 by the last item
    [None, 2, None]
    >>> swaplist(["a"])
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for -: 'str' and 'int'
    >>> swaplist([])
    []
    """
    r = [None] * len(l)
    for i, v in enumerate(l):
        r[v - base] = i + base
    return r
    
def sublist(a, b):
    """
    Subtract the list b from a, return a copy
    
    >>> sublist([1, 2, 3, 4, 5], [2, 3])
    [1, 4, 5]
    """
    r = a[:]
    for i in b:
        r.remove(i)
    return r

def rmkdir(path):
    """
    Recursively mkdir() when necessary to ensure a path exists

    Kinda like mkdir -p

    Note: I just noticed that os.makedirs() exists but throws the same error
    if a directory exists or if a file is blocking creation of that dir (at
    least on Windows).  Not terribly useful.
    """
    t = []
    sep = os.path.sep
    if sep != "/":
        parts = path.replace(os.path.sep, "/").split("/")
    else:
        parts = path.split(sep)
    
    if path[0] == "/":
        t = ["/" + parts[0]]
        parts = parts[1:]
        
    for p in parts:
        t.append(p)
        # I chose isdir so we'll get a helpful error if it exists but is a file
        if os.path.isdir(sep.join(t)): continue
        os.mkdir(sep.join(t))
    
def _test():
    from doctest import testmod
    testmod()

if __name__ == "__main__":
    _test()