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
