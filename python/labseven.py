##This plug-in supports a simple format, which has a 128-byte header consisting of the words
##“SPAM” followed by the width, height, and pixel size in bits.
##The header fields are separated by spaces. The image data follows directly
##after the header, and can be either bi-level, greyscale, or 24-bit true color.
##Source: https://pillow.readthedocs.io/en/4.1.x/handbook/writing-your-own-file-decoder.html

from PIL import Image, ImageFile
import string

class SpamImageFile(ImageFile.ImageFile):

    format = "SPAM"
    format_description = "Spam raster image"

    def _open(self):

        # check header
        header = self.fp.read(128)
        if header[:4] != "SPAM":
            raise SyntaxError, "not a SPAM file"

        header = string.split(header)

        # size in pixels (width, height)
        self.size = int(header[1]), int(header[2])

        # mode setting
        bits = int(header[3])
        if bits == 1:
            self.mode = "1"
        elif bits == 8:
            self.mode = "L"
        elif bits == 24:
            self.mode = "RGB"
        else:
            raise SyntaxError, "unknown number of bits"

        # data descriptor
        self.tile = [
            ("raw", (0, 0) + self.size, 128, (self.mode, 0, 1))
        ]

Image.register_open(SpamImageFile.format, SpamImageFile)

Image.register_extension(SpamImageFile.format, ".spam")
Image.register_extension(SpamImageFile.format, ".spa") 