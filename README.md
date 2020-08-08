# Russet

A project to track colour changes over the course of a year.

The rough plan:

- Set up a Raspberry Pi with a camera, and point it out my window.

- Take pictures of the view, say once an hour.  This will include a
  bunch of trees plus some sky.

- Downsample (is that the right word?) the picture:

  - Bucket the colours
  - Figure out how much of the image is covered by those colors
    (Example: 10% white, 5% grey, 20% brown, 40% deep green, 25% light
    green)

- Track those changes visually, over the course of a year, through a
  graph of some kind.


# Usage

## send_image: send image data to InfluxDB

To post to InfluxDB:

```
$ export INFLUX_HOST=influx.exampl.com
$ export INFLUX_PORT=8086
$ export INFLUX_USER=russet
$ export INFLUX_PASSWORD=password
$ ./russet.py send_image_data data/russet-1595042934.png
[FIXME] russet,tag=#2b2a2c count=457984,percentage=60.06 1595042934
[FIXME] russet,tag=#807d84 count=80037,percentage=10.50 1595042934
[FIXME] russet,tag=#c1bfbe count=14903,percentage=1.95 1595042934
[FIXME] russet,tag=#59545a count=128603,percentage=16.87 1595042934
[FIXME] russet,tag=#67626d count=28147,percentage=3.69 1595042934
[FIXME] russet,tag=#6b6c6e count=15282,percentage=2.00 1595042934
[FIXME] russet,tag=#4a4d4b count=35402,percentage=4.64 1595042934
[FIXME] russet,tag=#9693a8 count=1766,percentage=0.23 1595042934
[FIXME] russet,tag=#9ba4a0 count=364,percentage=0.05 1595042934
Points written!
```

## plot: plot colour info with Matplotlib

```
$ ./russet.py plot data/russet-1595042934.png
```


## analyze: analyze a single image and print out info in JSON format

```
$ ./russet.py analyze data/russet-1595042934.png
{
  "metadata": {
    "date": "0001",
    "filename": "/home/aardvark/dev/gitlab.com/saintaardvark/russet/data/russet_test-0001.png",
    "cam": 67890
  },
  "all_colours": [
    {
      "color": {
        "r": 209,
        "g": 209,
        "b": 213
      },
      "count": 211157,
      "percentage": 26.14477895610076
    },
[snip]
```
