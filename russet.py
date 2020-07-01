#!/usr/bin/env python3

import click

from cthief_wrapper import ColorThiefWrapper

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
    """Analyze single image and print colour/pixel counts
    """
    cthief = ColorThiefWrapper(image)
    cmap = cthief.get_palette_cmap()

    for vb in cmap.vboxes.contents:
        color = vb['color']
        count = vb['vbox'].count
        print("{}: has {} pixels".format(color, count))


@click.command('plot',
              short_help='Plot some image data')
@click.argument('image',
                required=True,
                type=click.Path(resolve_path=True))
def plot(image):
    pass

russet.add_command(analyze)
russet.add_command(plot)

if __name__ == '__main__':
    russet()
