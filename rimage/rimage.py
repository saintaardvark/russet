"""Class for working with Russet images
"""

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

        # FIXME: better variable name
        all_colours = []
        for vb in cmap.vboxes.contents:

            rgb_values = dict(zip(['r', 'g', 'b'], vb['color']))
            count = vb['vbox'].count
            point = {'color': rgb_values,
                     'count': count
            }
            all_colours.append(point)
        return all_colours

    def build_metadata(self):
        """Return  metadata
        """
        # FIXME: Need better metadata
        metadata = {'date': 12345, 'cam': 67890}
        return metadata

        metadata = build_metadata(image)
