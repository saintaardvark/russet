"""Colourthief wrapper
"""

from colorthief import ColorThief, MMCQ, CMap

class ColorThiefWrapper(ColorThief):
    """Wrapper for ColorThief.
    """

    def __init__(self, file):
        super().__init__(file)

    def get_palette_cmap(self, color_count=10, quality=10):
        """This is very nearly an exact copy of the superclass method; the one
        difference is that we return the CMap object.

        :param color_count: the size of the palette, max number of colors
        :param quality: quality settings, 1 is the highest quality, the bigger
                        the number, the faster the palette generation, but the
                        greater the likelihood that colors will be missed.
        :return : CMap object

        """
        image = self.image.convert('RGBA')
        width, height = image.size
        pixels = image.getdata()
        pixel_count = width * height
        valid_pixels = []
        for i in range(0, pixel_count, quality):
            r, g, b, a = pixels[i]
            # If pixel is mostly opaque and not white
            if a >= 125:
                if not (r > 250 and g > 250 and b > 250):
                    valid_pixels.append((r, g, b))

        # Send array to quantize function which clusters values
        # using median cut algorithm
        cmap = MMCQ.quantize(valid_pixels, color_count)
        return cmap

if __name__ == '__main__':
    cthief = ColorThiefWrapper("russet_test-0001.png")
    print(cthief.get_palette_cmap())
