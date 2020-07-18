#!/usr/bin/env python3

import json

import click

from cthief_wrapper import ColorThiefWrapper
from plot import RussetPlot

@click.group()
def russet():
    """
    Tool for tracking colour changes in images.
    """
    pass

@click.command('analyze',
               short_help='Analyze single image file')
@click.argument('image',
                required=True,
                type=click.Path(resolve_path=True))
def analyze(image):
    """Analyze single image and print colour/pixel counts in JSON
    """
    cthief = ColorThiefWrapper(image)
    cmap = cthief.get_palette_cmap()

    # FIXME: better variable name
    # FIXME: Make a class
    everything = []
    for vb in cmap.vboxes.contents:

        rgb_values = dict(zip(['r', 'g', 'b'], vb['color']))
        count = vb['vbox'].count
        point = {'color': rgb_values,
                 'count': count
        }
        everything.append(point)

    print(json.dumps(everything, indent=2))


@click.command('plot',
               short_help='Plot some image data')
@click.argument('image',
                required=True,
                type=click.Path(resolve_path=True))
def plot(image):
    RussetPlot(image)

russet.add_command(analyze)
russet.add_command(plot)

if __name__ == '__main__':
    russet()
