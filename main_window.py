from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QResizeEvent
from PySide6.QtWidgets import QColorDialog, QFileDialog, QMainWindow

from ui_mainwindow import Ui_MainWindow

DEFAULT_MAIN_WINDOW_WIDTH, DEFAULT_MAIN_WINDOW_HEIGHT = 1400, 800
MIN_MAIN_WINDOW_WIDTH, MIN_MAIN_WINDOW_HEIGHT = 600, 300


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        # Initialize an empty image
        self.displaying_img = None

        # Main window title and dimensions
        self.setWindowTitle("Marginer")
        self.setGeometry(
            300, 400, DEFAULT_MAIN_WINDOW_WIDTH, DEFAULT_MAIN_WINDOW_HEIGHT
        )
        self.setMinimumSize(QSize(MIN_MAIN_WINDOW_WIDTH, MIN_MAIN_WINDOW_HEIGHT))

        # Connections
        self.add_file_button.clicked.connect(self.add_images)
        self.file_explorer_listwidget.currentItemChanged.connect(self.show_image)
        self.remove_file_button.clicked.connect(self.remove_images)
        self.margin_h_slider.valueChanged.connect(self.print_value)
        self.margin_v_slider.valueChanged.connect(self.print_value)
        self.margin_h_offset_slider.valueChanged.connect(self.print_value)
        self.margin_v_offset_slider.valueChanged.connect(self.print_value)
        self.color_picker_button.clicked.connect(self.color_button_clicked)

    def show_image(self, file):
        if self.logo_svg.isVisible():
            self.logo_svg.hide()

        if not self.photo_display.isVisible():
            self.photo_display.setVisible(True)

        if not file:
            return

        self.displaying_img = QPixmap(file.text())
        self.update_image_size()

    def update_image_size(self):
        self.photo_display.resize(
            int(0.4 * self.size().width()), int(0.7 * self.size().height())
        )

        self.photo_display.setPixmap(
            self.displaying_img.scaled(
                self.photo_display.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.FastTransformation,
            )
        )

    def add_images(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Image Files (*.jpg *.jpeg *.png)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.file_explorer_listwidget.addItems(selected_files)
        self.file_explorer_listwidget.sortItems()

    def color_button_clicked(self):
        color = QColorDialog().getColor()
        if color.isValid():
            print(color.name(), color.getRgb())

    def remove_images(self):
        self.file_explorer_listwidget.takeItem(
            self.file_explorer_listwidget.currentRow()
        )
        if self.file_explorer_listwidget.count() == 0:
            self.photo_display.setVisible(False)
            self.logo_svg.setVisible(True)

    def print_value(self, value):
        print(value)

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        if self.photo_display.isVisible() and self.displaying_img is not None:
            self.update_image_size()
