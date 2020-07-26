"""Module for Russet data handling
"""

from influxdb import InfluxDBClient


influxdb_measurement = 'russet'


def build_line_format(image_data):
    """Build line format for InfluxDB
    """

    ms_string = build_measurement_string(image_data)
    tag_string = build_tag_string(image_data)
    value_string = build_value_string(image_data)
    ts_string = build_timestamp_string(image_data)

    lf_string = "{ms_string},{tag_string} {value_string} {ts_string}" .format(
        ms_string=ms_string,
        tag_string=tag_string,
        value_string=value_string,
        ts_string=ts_string
    )

    return lf_string


def build_measurement_string(image_data):
    """Build measurement string
    """
    return influxdb_measurement


def build_tag_string(image_data):
    """Build tag string from image data, probably colours
    """
    return 'FIXME_tag_string'


def build_value_string(image_data):
    """Build value string
    """
    return 'FIXME_value_string'

def build_timestamp_string(image_data):
    """Build up timestamp string from image name
    """
    return 'FIXME_timestamp'


def send_to_influxdb(image_data):
    """Send line to InfluxDB
    """
    line = build_line_format(image_data)
    print('[FIXME] {}'.format(line))
