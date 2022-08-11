'''
####################################
Instructions:
-  In your laptop create a folder named 'images' and put inside there all there
.png files that you want to convert into a .gif file.

-  The script will follow
the order of the files in the folder. I recommend that the files are ordered by
time or that you add in front of them '01', '02', '03', etc.

-  There are two optional variables:
1) interval: this is the time interval between images. The default value is
400 ms.
2) looping: this value makes the gif animation to continue forever if it's set
to 0 (default value). Or it makes the animation to stop after one cycle if it's
set to 1.

- The exit file will be named 'animation.gif'.
#####################################
'''

import glob
import os
from PIL import Image

def make_gif(interval = 400, looping = 0):
    path_to_desktop = os.path.join(os.environ["HOMEPATH"], "Desktop", "images", "*.png")
    frames = [Image.open(image) for image in glob.glob(path_to_desktop)]
    frame_one = frames[0]

    frame_one.save("animation.gif", format="GIF", append_images=frames,
               save_all=True, duration=interval, loop=looping)


if __name__ == "__main__":
    path_to_desktop = os.path.join(os.environ["HOMEPATH"], "Desktop", "images", "*.png")
    make_gif(path_to_desktop)
