"""Module for making memes.

This Module is responsible for manipulating and drawing text onto images.
"""

import os
import random
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime


class MemeEngine:
    """Meme Engine class for making memes."""

    def __init__(self, output_dir):
        """Validate and create the output directory for the memes."""
        self.output_dir = output_dir
        self.imgcounter = 1
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Meke Meme method create the meme and return the output file."""
        img = Image.open(img_path)
        outfile = os.path.join(self.output_dir, f"img-{self.imgcounter}.jpg")
        self.imgcounter += 1
        aspect_ratio = width/float(img.size[0])
        height = int(aspect_ratio*float(img.size[1]))
        img.thumbnail((width, height))
        font = ImageFont.truetype("./_data/fonts/CaviarDreams_Italic.ttf",
                                  size=20)
        text_position = random.choice(range(30, height - 50))
        draw = ImageDraw.Draw(img)
        draw.text((30, text_position), f"{text} - {author}",
                  font=font, stroke_width=1)
        img.save(outfile, "JPEG")
        return outfile
