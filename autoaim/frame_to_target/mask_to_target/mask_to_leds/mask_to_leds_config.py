import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))
NAME = os.path.basename(DIR)
ASSETS_DIR = DIR / f'{NAME}_assets'

HEIGHT_1M_REL = 0.078
DISTANCE_OFFSET = 0.027
EPSILON = 1E-5


class CRITERIA:
    DISTANCE = (0, 100)  # (0.4, 3) todo: fix temporary distance criteria patch
    DIMS_RATIO = (2, 10)
    ANGLE = (-15, 15)


class DRAW:
    COLOR_LED = (255, 180, 0)
    COLOR_NOT_LED = (0, 180, 255)

    THICKNESS = 2
    FONT = 0  # choose OpenCV font
    FONT_SIZE = 0.46
    LABEL_OFFSET = (7, 4)
