import csv
import sys

from defs import hier

def summarize(fn, nfn):
    f = csv.reader(file(fn, "rb"))
    fo = open(nfn, "wb")
    header = f.next()
    cams = Node("Root")
    for l in f:
        for x in zip(header, l):
            if x in hier:
                #print hier[x][0]
                cams.inc_child(*hier[x][0])
    cams.p()            

class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.val = 1
    def inc_child(self, *x):
        if not x: return # empty recursion...
        if x[0] in self.children:
            self.children[x[0]].val += 1
        else:
            self.add_child(x[0]).inc_child(*x[1:])
    def add_child(self, name):
        if name in self.children:
            return self.children[name]
        x = Node(name)
        self.children[name] = x
        return x
    def count(self):
        # Yes I know this is recursive.
        return sum([v.count() for k,v in self.children.items()]) + self.val
    def p(self, level=0):
        print "%s %s %d" % (" "*level, self.name, self.count())
        print "%s %r" % (" "*level, self.children)
        for k,v in self.children.items():
            v.p(level+2)

if __name__ == "__main__":
    summarize(*sys.argv[1:])