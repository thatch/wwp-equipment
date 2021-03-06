"""
This will produce some basic stats for output to a graphing program. The
main purpose is to aggregate the new/*.csv files
"""

import re
import sys
import os

import natsort

class Aggregator(object):
    #N.B. no flags passed to compile
    def __init__(self, interesting):
        self.interesting = map(re.compile, interesting)
        self.stats = []
        self.headings = []
    def feed(self, data, title):
        """
        data is a list of entries, f.e. from a column in a csv file
        """
        self.stats.append([0.] * len(self.interesting))
        self.headings.append(prettyfile(title))
        size = len(data)
        for x in data:
            for (i, r) in enumerate(self.interesting):
                if r.match(x):
                    self.stats[-1][i] += 1. / size
    def results(self):
        """
        returns a string for simple data, which can be run through PyX or gnuplot.

        The first line is the headings, subsequent lines are data.  All space-separated.
        """
        buf = []
        #buf.append(' '.join(self.headings))
        
        buf.append('x ' + ' '.join(describe_regex(r.pattern) for r in self.interesting))
        i = 0
        #for (title, series) in zip([describe_regex(r.pattern) for r in self.interesting], zip(*self.stats)):
        for (title, series) in zip(self.headings, self.stats):

            #buf.append('%s %s' % (title, ' '.join(map(str, series))))
            buf.append('%d %s' % (i, ' '.join(map(str, series))))
            i += 1
        return '\n'.join(buf)
    def results_to_file(self, fn):
        fo = open('graph/' + fn, 'wb')
        fo.write(self.results())
        fo.write('\n')
        fo.close()
        fo = open("graph/mk" + fn.replace('.txt', '.sh'), "wb")
        fo.write("""#!/bin/bash

gnuplot <<EOF;
set term png
set key below
set output '%s'\n""" % fn.replace('.txt', '.png'))

        fo.write("plot ")
        heads = [describe_regex(r.pattern) for r in self.interesting]
        fo.write("\"%s\" using 1:2 with lines title \"%s\"" % (fn, heads[0]))

        n = 3
        for h in heads[1:]:
            fo.write(",\"\" using 1:%d with lines title \"%s\"" % (n, h))
            n += 1
        fo.write("\nEOF\n")
        fo.close()

r_date = re.compile(r'(\d+)(\d{2})\.')

def cmpdates(a, b):
    x = r_date.search(a)
    y = r_date.search(b)
    xt = (int(x.group(2)), int(x.group(1)))
    yt = (int(y.group(2)), int(y.group(1)))
    return cmp(xt, yt)

def main(args):
    interesting = [
        ["Nikon vs Canon", "cam_war.txt", [r'^Canon-', r'^Nikon-', r'^Olympus-']],
        ["Historical Nikon", "cam_histnikon.txt", ['Nikon-CP9..', 'Nikon-CP5...', 'Nikon-D100', 'Nikon-D200']],
        ["Recent Prosumer Nikon", "cam_nikon.txt", ['']]]

    cams = Aggregator([r'^Canon-', r'^Nikon-', r'^Olympus-', r'^Fuji-'])
    mid_nikon_cams = Aggregator(['Nikon-CP9..', 'Nikon-CP5...', 'Nikon-D40', 'Nikon-D50', 'Nikon-D80'])
    pro_nikon_cams = Aggregator(['Nikon-D70', 'Nikon-D100', 'Nikon-D200', 'Nikon-D300', 'Nikon-D1x?$', 'Nikon-D2x?$', 'Nikon-D3x?$'])
    mid_canon_cams = Aggregator(['Canon-300D', 'Canon-350D', 'Canon-400D', 'Canon-450D'])
    pro_canon_cams = Aggregator(['Canon-6D', 'Canon-10D', 'Canon-5D', 'Canon-20D', 'Canon-30D', 'Canon-40D'])

    # r'^Sigma-', r'^Peleng-', r'^Nikkor-', r
    lenses = Aggregator([r'Nikkor-10\.5', 'Nikon-FCE[89]', 'Sigma-8mm', 'Peleng-8mm', '^Tamron-11', '^Canon-15', '^Nikkor-8mm', 'Nikon-WCE24'])
    panoheads = Aggregator([r'LensRing-BoPhoto', r'360precision', r'Manfrotto', 'NodalNinja', 'Agnos-', 'none'])
    nn = Aggregator(['NodalNinja-', 'NodalNinja-2', 'NodalNinja-3', 'NodalNinja-4', 'NodalNinja-5'])
    
    for fn in sorted(args, cmp=cmpdates):
        print "Processing", fn
        fo = open(fn, 'rb')
        tuples = [line.split(',') for line in fo if ',' in line]
        #0:user, 1:camera, 2:lens, 3:panohead, 4:tripod, 5:software
        cams.feed([t[1] for t in tuples], fn)
        mid_nikon_cams.feed([t[1] for t in tuples], fn)
        pro_nikon_cams.feed([t[1] for t in tuples], fn)
        mid_canon_cams.feed([t[1] for t in tuples], fn)
        pro_canon_cams.feed([t[1] for t in tuples], fn)
        lenses.feed([t[2] for t in tuples], fn)
        panoheads.feed([t[3] for t in tuples], fn)
        nn.feed([t[3] for t in tuples], fn)
        fo.close()

    cams.results_to_file("cams.txt")
    mid_nikon_cams.results_to_file("nikon_cams_mid.txt")
    pro_nikon_cams.results_to_file("nikon_cams_pro.txt")
    mid_canon_cams.results_to_file("canon_cams_mid.txt")
    pro_canon_cams.results_to_file("canon_cams_pro.txt")
    lenses.results_to_file("lenses.txt")
    panoheads.results_to_file("panoheads.txt")
    nn.results_to_file("nn.txt")


 
dummy = """
interesting_cams = \
    ['^Canon', 'Canon-5D', 'Canon-300D', 'Canon-350D', 'Canon-20D', 'Canon-30D', 'Canon-40D',
     '^Nikon', 'Nikon-D70s', 'Nikon-D70$', 'Nikon-D40', 'Nikon-D50', 'Nikon-D80',
     '^Olympus', 'Olympus-E3',
     'Fuji-S3Pro', 'Nikon-CP990', 'Nikon-CP950', 'Nikon-CP5000']

interesting_lenses = \
    ['Nikkor-10.5mm', 'Nikkor-8mm', 'Sigma-8mm', 'Peleng-8mm', 'Nikon-FCE8', 'Nikon-FCE9']

stats_cams = []
stats_lenses = []

def main(fo):
    stats_cams.append([0] * len(interesting_cams))
    stats_lenses.append([0] * len(interesting_lenses))

    #TODO: use csv module, read header line to obj
    for line in fo:
        line = line.strip()
        if not line or ',' not in line: continue

        (user, camera, lens, panohead, tripod, software) = line.split(",")
        for (i, t) in enumerate(interesting_cams):
            if re.match(t, camera):
                stats_cams[-1][i] += 1
        for (i, t) in enumerate(interesting_lenses):
            if re.match(t, lens):
                stats_lenses[-1][i] += 1


if __name__ == '__main__':
    for fn in sys.argv[1:]:
        fo = open(fn, 'rb')
        main(fo)
        fo.close()
    # produce some files in data/
    fo = open('cams.xml', 'wb')
    fo.write('<chart><chart_type>line</chart_type>\n')
    fo.write('<legend_label layout="vertical" /><chart_data>\n')

    fo.write('<row><null />')
    for a in sys.argv[1:]:
        #TODO: basename
        fo.write('<string>%s</string>' % a)
    fo.write('</row>\n')

    for (title, series) in zip(interesting_cams, zip(*stats_cams)):
        fo.write('<row><string>%s</string>\n' % title) #TODO: prettify
        for s in series:
            fo.write('<number>%d</number>' % s)
        fo.write('</row>\n')
    fo.write('</chart_data></chart>\n')
"""



def describe_regex(r):
    if r.startswith('^'):
        return r[1:] + '*'
    if '(' in r:
        # aack
        return r
    return r.replace(r'\\', '')

def prettyfile(f):
    return os.path.basename(f)

if __name__ == '__main__':
    main(sys.argv[1:])
