from collections import deque, namedtuple
from dataclasses import dataclass

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QPainter, QPixmap, QTransform

Color = namedtuple("Color", ["r", "g", "b", "alpha"])


@dataclass
class Margin:
    margin_left: int = 0
    margin_right: int = 0
    margin_top: int = 0
    margin_bottom: int = 0
    color: tuple = Color(255, 255, 255, 255)

    def __str__(self) -> str:
        return str(
            [
                self.margin_left,
                self.margin_right,
                self.margin_top,
                self.margin_bottom,
                self.color,
            ]
        )


class Image:
    def __init__(self):
        self.path: str = None
        self.original_image: QPixmap = QPixmap()
        self.image_metainfo: dict = None
        self.margin: Margin = Margin()
        self.scaled_image: QPixmap = None
        self.preview_image: QPixmap = None
        self.flip_vertical: bool = False
        self.flip_horizontal: bool = False
        self.num_of_90_deg_rotation: int = 0
        self.__edit_log: deque = deque()
        self.__temp_log: deque = deque()

    def load_image(self, path: str):
        try:
            self.path = path
            self.original_image.load(self.path)
            self.__edit_log.append(str(self.margin))
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")

    def set_margins(
        self,
        margin_left: int = None,
        margin_right: int = None,
        margin_top: int = None,
        margin_bottom: int = None,
        color: tuple = None,
    ):
        if margin_left is not None:
            self.margin.margin_left = margin_left
        if margin_right is not None:
            self.margin.margin_right = margin_right
        if margin_top is not None:
            self.margin.margin_top = margin_top
        if margin_bottom is not None:
            self.margin.margin_bottom = margin_bottom
        if color is not None:
            self.margin.color = Color(*color)

    def get_log(self):
        print(self.__edit_log)

    def push_edit_log(self):
        self.__edit_log.append(str(self.margin))

    def undo_edit(self):
        if len(self.__edit_log) > 1:
            self.__temp_log.append(self.__edit_log.pop())
            self.margin = Margin(*eval(self.__edit_log[-1]))
            self.update_preview_image()

    def redo_edit(self):
        if self.__temp_log:
            self.__edit_log.append(self.__temp_log.pop())
            self.margin = Margin(*eval(self.__edit_log[-1]))
            self.update_preview_image()

    def empty_temp_log(self):
        if self.__temp_log:
            self.__temp_log.clear()

    def rotate_90_deg(self, clockwise: bool = False):
        if clockwise:
            self.num_of_90_deg_rotation = (self.num_of_90_deg_rotation + 1) % 4
        else:
            self.num_of_90_deg_rotation -= (self.num_of_90_deg_rotation + 3) % 4

    def scaled(self, size: QSize):
        """Function to scale original image to fitted size"""
        self.scaled_image = self.original_image.scaled(
            size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

    def update_preview_image(self):
        """Function to fill in the scaled image the margins"""
        new_width = (
            self.scaled_image.width()
            + self.margin.margin_left
            + self.margin.margin_right
        )
        new_height = (
            self.scaled_image.height()
            + self.margin.margin_top
            + self.margin.margin_bottom
        )

        new_image = QPixmap(new_width, new_height)
        new_image.fill(
            QColor(
                self.margin.color.r,
                self.margin.color.g,
                self.margin.color.b,
                self.margin.color.alpha,
            )
        )

        painter = QPainter(new_image)
        painter.drawPixmap(
            self.margin.margin_left, self.margin.margin_top, self.scaled_image
        )
        painter.end()
        self.preview_image = new_image
