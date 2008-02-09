import sys

from pyx import *

class grad(color.gradient):
    color_cycle = [
        color.rgb(1.0,   0.501, 0.0),
        color.rgb(1.0,   1.0,   0.2),
        color.rgb(0.2,   1.0,   0.0),
        color.rgb(0.102, 0.702, 1.0),
        color.rgb(0.4,   0.302, 1.0),
        color.rgb(0.902, 0.102, 0.2),
        
        color.rgb(1.0,   0.749, 0.501),
        color.rgb(1.0,   1.0,   0.6),
        color.rgb(0.702, 1.0,   0.549),
        color.rgb(0.651, 0.929, 1.0),
        color.rgb(0.8,   0.749, 1.0),
        color.rgb(1.0,   0.6,   0.749),
    ]
        
    def select(self, i, n):
        return self.color_cycle[i]

f = graph.data.file("graph/nikon_cams.txt", xname=1)

print dir(f)
sys.exit()

g = graph.graphxy(width=8,
                  x=graph.axis.linear(min=0, max=2),
                  y=graph.axis.linear(min=0, max=2),
                  key=graph.key.key(pos="br", dist=0.1))
g.plot(f,
       [graph.style.line([grad()])])
g.writeEPSfile("change")
g.writePDFfile("change")
