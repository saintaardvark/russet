"""Class for working with Russet images
"""

from pathlib import Path
import re

from cthief_wrapper.cthief_wrapper import ColorThiefWrapper

class Rimage():
    """Class for Russet Images
    """

    def __init__(self, image_path=""):
        self.image_path = image_path
        self.colour_data = self.build_colour_data()
        self.metadata = self.build_metadata()
        pass

    def build_colour_data(self):
        """Return color data for image
        """
        cthief = ColorThiefWrapper(self.image_path)
        cmap = cthief.get_palette_cmap()

        total_pixels = self.get_total_pixels(cmap.vboxes.contents)

        # FIXME: better variable name
        all_colours = []
        for vb in cmap.vboxes.contents:
            rgb_values = dict(zip(['r', 'g', 'b'], vb['color']))
            count = vb['vbox'].count
            percentage = float((count / total_pixels) * 100.0)
            point = {'color': rgb_values,
                     'count': count,
                     'percentage': percentage
            }
            all_colours.append(point)

        return all_colours

    def build_metadata(self):
        """Return metadata
        """
        # FIXME: Need better metadata
        img_date = self.build_image_date()
        metadata = {'date': img_date,
                    'filename': self.image_path,
                    'cam': 67890,}
        return metadata

        metadata = build_metadata(image)

    def build_image_date(self):
        """Build image date out of filename

        Assumes epoch seconds is in filename
        """
        fullpath = Path(self.image_path)
        filename = fullpath.name

        r = re.compile(r'\d+')
        try:
            return r.findall(filename)[0]
        except IndexError:
            return ""

    def get_total_pixels(self, contents):
        """Count total pixels
        """
        total_pixels = 0
        for vb in contents:
            total_pixels += vb['vbox'].count

        return total_pixels
