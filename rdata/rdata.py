"""Module for Russet data handling
"""

from influxdb import InfluxDBClient


influxdb_measurement = 'russet'

def send_to_influxdb(image_data):
    """Send line to InfluxDB
    """
    print('{}'.format(image_data.metadata))

    for datapoint in image_data.colour_data:
        line = build_line_format(datapoint, image_data.metadata)
        print('[FIXME] {}'.format(line))


def build_line_format(image_data, metadata):
    """Build line format for InfluxDB
    """

    ms_string = build_measurement_string(image_data)
    tag_string = build_tag_string(image_data)
    field_string = build_field_string(image_data)
    ts_string = build_timestamp_string(metadata)

    lf_string = "{ms_string},{tag_string} {field_string} {ts_string}" .format(
        ms_string=ms_string,
        tag_string=tag_string,
        field_string=field_string,
        ts_string=ts_string
    )

    return lf_string


def build_measurement_string(datapoint):
    """Build measurement string
    """
    return influxdb_measurement


def build_tag_string(datapoint):
    """Build tag string from image colours
    """
    color = datapoint['color']
    color_tuple = (color['r'], color['g'], color['b'])
    hex_color = '{}'.format(rgb_to_hex(color_tuple))
    return 'tag=#{}'.format(hex_color)


def build_field_string(datapoint):
    """Build value string
    """
    count_string = 'count={}'.format(datapoint['count'])
    percentage_string = 'percentage={:2.2f}'.format(datapoint['percentage'])
    return '{},{}'.format(count_string, percentage_string)


def build_timestamp_string(metadata):
    """Build up timestamp string from image name
    """
    return metadata['date']


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
