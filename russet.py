#!/usr/bin/env python3

import json
import sys

import click

from cthief_wrapper.cthief_wrapper import ColorThiefWrapper
from plot import RussetPlot
from rimage.rimage import Rimage
import rdata.rdata as rdata

@click.group()
def russet():
    """
    Tool for tracking colour changes in images.
    """
    pass



@click.command('send_image_data',
               short_help='Analyze image and send data')
@click.argument('image',
                required=True,
                type=click.Path(resolve_path=True))
def send_image_data(image):
    """Analyze image and send data
    """
    try:
        image_data = Rimage(image)
    except FileNotFoundError as e:
        print("Can't find that image: {}".format(e))
        sys.exit(1)

    rdata.send_to_influxdb(image_data)


@click.command('analyze',
               short_help='Analyze single image file')
@click.argument('image',
                required=True,
                type=click.Path(resolve_path=True))
def analyze(image):
    """Analyze single image and print colour/pixel counts in JSON
    """
    try:
        image_data = Rimage(image)
    except FileNotFoundError as e:
        print("Can't find that image: {}".format(e))
        sys.exit(1)

    everything = {'metadata': image_data.metadata,
                  'all_colours': image_data.colour_data}
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
russet.add_command(send_image_data)

if __name__ == '__main__':
    russet()
