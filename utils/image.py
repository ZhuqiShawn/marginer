from dataclasses import dataclass

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QPainter, QPixmap


@dataclass
class Margin:
    margin_left: int = 0
    margin_right: int = 0
    margin_top: int = 0
    margin_bottom: int = 0
    color: tuple = (255, 255, 255, 255)


class Image:
    def __init__(self):
        self.path: str = None
        self.original_image: QPixmap = QPixmap()
        self.image_metainfo: dict = None
        self.margin: Margin = Margin()
        self.scaled_image: QPixmap = None
        self.preview_image: QPixmap = None
        self.__edit_log: dict = None

    def load_image(self, path: str):
        try:
            self.path = path
            self.original_image.load(self.path)
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
            self.margin.color = color

    def scaled(self, size: QSize) -> QPixmap:
        """Function to scale original image to fitted size"""
        self.scaled_image = self.original_image.scaled(
            size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

    def edit_image(self) -> QPixmap:
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
        new_image.fill(QColor(*self.margin.color))

        painter = QPainter(new_image)
        painter.drawPixmap(
            self.margin.margin_left, self.margin.margin_top, self.scaled_image
        )
        painter.end()
        self.preview_image = new_image
