#!/usr/bin/env python
"""
Get information on what cameras people use for WWP.
"""

import sys
import re
import thatch.dumbcache as dc

dc._maxage = 24 * 60 * 60 * 365 #seconds in one year


# For real events
base = "http://geoimages.berkeley.edu/wwp%s/" % sys.argv[1]
# For prerelease
#base = "http://128.32.102.88:8090/gen/live_preview/wwp%s/" % sys.argv[1]

c = dc.Cacher()
r_person = re.compile(r"""<dt>\s+<a href="(html/.+?\.html)">""")
r_equip = re.compile(r"""<p><small><b>Equipment:</b><br>(.+?)</small></p></td>""", re.DOTALL)

def main(csv=False):
    o = c.fetch(base + "NameIndex.html")
    for p in r_person.finditer(o.data):
        print p.group(1)[5:-5]
        if not csv:
            po = c.fetch(base + p.group(1))
            e = r_equip.search(po.data)
            #print p.group(1)
            if not e:
                #print p.group(1)
                print "    FAILED"
            else:
                print indent(e.group(1), 4)
                print

def indent(s, n):
    lines = s.split("\n")
    return "\n".join([" "*n + l for l in lines])

if __name__ == "__main__":
    main(False)
   
