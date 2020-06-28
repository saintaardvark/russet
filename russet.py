#!/usr/bin/env python3

from cthief_wrapper import ColorThiefWrapper

def main(img="russet_test-0001.png"):
    """Main entry point.
    """
    cthief = ColorThiefWrapper(img)
    cmap = cthief.get_palette_cmap()

    for vb in cmap.vboxes.contents:
        color = vb['color']
        count = vb['vbox'].count
        print("{}: has {} pixels".format(color, count))


if __name__ == '__main__':
    main()
