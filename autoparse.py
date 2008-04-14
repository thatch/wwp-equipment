import re
import sys

#FIXME: http://www.photopla.net/wwp0506/index.php camera, lens, tripod!!!

from defs import rules


def parseit(fn):
    name_re = re.compile(r"^(.+?)\r?\n((?:    .*\r?\n)+|    FAILED)\r?\n", re.M)
    data = file(fn, "r").read()

    # Setup parsing rule.
    rep = []
    for type in rules:
        t = []
        for r in type:
            t.append((re.compile(r[0], re.I | re.M), r[1:]))
        rep.append(t)

    # Now use 'em
    k = ['user', 'camera', 'lens', 'panohead', 'tripod', 'software']
    print ",".join(k)
    linestr = ",".join(['%%(%s)s' % i for i in k])
    for name in name_re.finditer(data):
        #print name.group(1)
        equip = name.group(2)
        if equip.strip().startswith("FAILED"):
            print name.group(1)
            continue
        me = {}
        for i in k: me[i] = "?"
        me['user'] = name.group(1)
        for t in rep:
            for r, i in t:
                x = r.search(equip)
                if x:
                    for a, b in i:
                        me[a] = b
                    #print "    ", i, x.group(0)
                    break
        print linestr % me
        #"%(user)s,%(camera)s,%(lens)s,%(panohead)s,%(tripod)s,%(software)s"


if __name__ == "__main__":
    parseit(sys.argv[1])
