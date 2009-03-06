#!/usr/bin/env python
"""%s [options] data_file image_file

Script to read in a camera data file and create a pretty plot.  The output
file is a png."""

# this script was developed using matplotlib 0.98.5.2 and numpy 1.2.1
# written by Berto Aguilar, updated by Tim Hatch

import datetime
import numpy
import optparse
import os
import sys

import matplotlib

COLORS = [
    '#097845', '#401700', '#e80300', '#e5e000',
    '#1ee544', '#383ce5', '#e52ce1',
    '#ff0000', '#990099', #FIXME these are random, find something better.
    ]

# only do this when running as a script
if __name__ == '__main__':
    matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
from matplotlib.dates import DateFormatter

def annotate(ax, plt):
    # annotate an interesting position
    text_date = datetime.date(2008, 10, 1)
    x_date = datetime.date(2008, 5, 1)
    pos = (x_date, 10.2)

    # create an ellipse to circle the interesting position.  the width and
    # height correspond to the unit range in their respective axis.  not sure
    # why there is an additional 1.5 factor for the y range.
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    xrange = (xlim[1] - xlim[0])
    yrange = (ylim[1] - ylim[0]) * 1.5

    axis_ratio = yrange / xrange

    ellipse_width = 75
    ellipse_height = (ellipse_width * axis_ratio)

    patch = mpatch.Ellipse(pos, ellipse_width, ellipse_height, fc='w')
    ax.add_patch(patch)
    plt.annotate('D300 beats the D70!',
                 pos,
                 (text_date, 18),
                 ha='right',
                 va='center',
                 arrowprops=dict(arrowstyle="fancy",
                                 shrinkA=5, # gap between text and arrow
                                 shrinkB=18, # gap between arrow and patch
                                 fc="w", # foreground color
                                 ec="k", # edge color
                                 connectionstyle="arc3, rad=-0.05"))

def dupe_axes(ax):
    # create a duplicate axes in order to put y-axis labels on the right side.
    ax2 = ax.twinx()
    ax2.plot_date(x, y, '-')
    ax2.yaxis.set_label_position('right')

    # hide the xlabels because we don't want them
    # www.mail-archive.com/matplotlib-users@lists.sourceforge.net/msg10475.html
    for xlabel in ax2.get_xticklabels():
        xlabel.set_visible(False)

def get_data(data_file):
    fobj = open(data_file, 'r')
    cameras = fobj.readline().split()[1:]
    data = []

    for line in fobj.readlines():
        line_split = line.split()
        data.append([float(x) for x in line_split[1:]])
    fobj.close()

    return cameras, data

def get_events(event_file):
    events = []

    fobj = open(event_file, 'r')
    for line in fobj.readlines():
        line = line.strip()
        if line == '':
            break

        year = 2000 + int(line[-2:])
        month = int(line[:-2])
        day = 1

        date = datetime.date(year, month, day)

        events.append(date)
    fobj.close()

    return events

def plot_data(events, cameras, data, buf, options):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    legend_lines = []
    x = events

    # get all the datapoints from the data list.  because each row of data in
    # the file corresponds to the popularity of a camera per event, we
    # transpose the data so each row corresponds to one camera.
    datapoints = numpy.array(data).transpose()

    ylim = 0
    # plot each of the cameras
    for i in range(len(cameras)):
        y = [ypoint * 100 for ypoint in datapoints[i]]

        t = ax.plot_date(x, y, '-', color=COLORS[i], label=cameras[i])
        legend_lines.append(t[0])
        ylim = max(ylim, max(y))

    # fix up the xaxis so it all fits nice
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m'))
    fig.autofmt_xdate()

    ax.set_ylim(0, ylim * 1.3)

    # create the legend
    legend = plt.legend(loc='best', ncol=3, mode='expand',
                        shadow=True, fancybox=True)
    legend.get_frame().set_alpha(0.3)
    for line in legend.get_lines():
        line.set_marker('o')

    # add the labels
    ax.set_title(options.title or 'Camera Data')
    ax.set_xlabel('Event Date')
    ax.set_ylabel('Percentage of Users')

    # TODO: attempt to duplicate the y tick labels on the right side.  right
    # now this is borked.
    #dupe_axes(ax)

    # add in vertical color bars
    for year in range(events[0].year, events[-1].year+1, 2):
        plt.axvspan(datetime.date(year, 12, 1), datetime.date(year+1, 12, 1),
                    facecolor='#cccccc', alpha=0.25)

    # add a grid
    plt.grid(True)

    #annotate(ax, plt)

    # write out an image file
    plt.savefig(buf)

def setup_parser(doc):
    parser = optparse.OptionParser(doc)

    parser.add_option('-e', '--event-file', help=(
            'File with the events data.  Format should be: X MMYY, '
            'where X is a 0-based index.  By default the script will '
            'look for events.txt along side the data_file.'))
    parser.add_option('-t', '--title', help='Plot title')

    return parser

if __name__ == '__main__':
    parser = setup_parser(__doc__ % (os.path.basename(sys.argv[0]),))
    (options, args) = parser.parse_args()

    try:
        data_file = args[0]
        image_file = args[1]
    except:
        parser.print_help()
        sys.exit(-1)

    event_file = options.event_file
    if event_file is None:
        event_file = os.path.join(os.path.dirname(data_file), 'events.txt')

    if not os.path.exists(event_file):
        message = 'Event list file not found at %s.'
        if options.event_file is None:
            message += 'You can specify an event file using -e.'
            parser.print_help()

        sys.exit(message % (event_file,))

    events = get_events(event_file)
    cameras, data = get_data(data_file)

    # save the figure out to a file
    fobj = open(image_file, 'wb')
    plot_data(events, cameras, data, fobj, options)
    fobj.close()
