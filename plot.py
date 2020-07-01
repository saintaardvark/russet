"""Russet module for plotting stuff
"""

import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
import matplotlib.patches as mpatch
import matplotlib.image as mpimg

from cthief_wrapper import ColorThiefWrapper

def RussetPlot(image):
    """Plot stuff about an image
    """
    cthief = ColorThiefWrapper(image)
    cmap = cthief.get_palette_cmap()


    # Based on
    # https://matplotlib.org/3.1.0/tutorials/colors/colors.html#xkcd-v-x11-css4
    # Thanks, matplotlib!
    fig = plt.figure(figsize=[4.8, 16])
    ax = fig.add_axes([0, 0, 1, 1])

    i = 0

    # FIXME: There's a better way to do this
    total_pixels = 0
    for vb in cmap.vboxes.contents:
        total_pixels += vb['vbox'].count

    for vb in reversed(cmap.vboxes.contents):
        weight = None

        # Need to map to tuple of range(0, 1)
        cn = tuple(map(lambda x: x / 255.0, vb['color']))

        r1 = mpatch.Rectangle((0, i), 1, 1, color=cn)
        r2 = mpatch.Rectangle((1, i), 1, 1, color=cn)
        txt = ax.text(2, i+.5, '  ' + "hello", va='center', fontsize=10,
                      weight=weight)
        ax.add_patch(r1)
        ax.add_patch(r2)
        ax.axhline(i, color='k')

        color_label = '{}'.format(vb['color'])
        pixel_count = (vb['vbox'].count / total_pixels) * 100

        ax.text(.5, i + 1.5, '{0:.2f} %'.format(pixel_count), ha='center', va='center')
        ax.text(1.5, i + 1.5, color_label, ha='center', va='center')
        ax.set_xlim(0, 3)
        ax.set_ylim(0, i + 2)
        ax.axis('off')
        i = i + 1

    plt.show()
