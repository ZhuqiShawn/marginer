from PySide6.QtCore import QSize
from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import (QColorDialog, QFileDialog, QListWidgetItem,
                               QMainWindow)

from ui_mainwindow import Ui_MainWindow
from utils import Image

DEFAULT_MAIN_WINDOW_WIDTH, DEFAULT_MAIN_WINDOW_HEIGHT = 1400, 800
MIN_MAIN_WINDOW_WIDTH, MIN_MAIN_WINDOW_HEIGHT = 800, 500


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        # Initialize an empty image
        self.displaying_img = Image()

        # Main window title and dimensions
        self.setWindowTitle("Marginer")
        self.setGeometry(
            800, 1000, DEFAULT_MAIN_WINDOW_WIDTH, DEFAULT_MAIN_WINDOW_HEIGHT
        )
        self.setMinimumSize(QSize(MIN_MAIN_WINDOW_WIDTH, MIN_MAIN_WINDOW_HEIGHT))

        # Connections
        self.add_file_button.clicked.connect(self.add_images)
        self.file_explorer_listwidget.currentItemChanged.connect(self.show_image)
        self.remove_file_button.clicked.connect(self.remove_images)

        self.margin_left_slider.valueChanged.connect(self.update_margin_left)
        self.margin_right_slider.valueChanged.connect(self.update_margin_right)
        self.margin_top_slider.valueChanged.connect(self.update_margin_top)
        self.margin_bottom_slider.valueChanged.connect(self.update_margin_bottom)
        self.color_picker_button.clicked.connect(self.update_margin_color)
        self.margin_h_lock.clicked.connect(self.h_lock_changed)
        self.margin_v_lock.clicked.connect(self.v_lock_changed)

    def show_image(self, file: QListWidgetItem):
        if self.logo_svg.isVisible():
            self.logo_svg.hide()

        if not self.preview_window.isVisible():
            self.preview_window.setVisible(True)

        if not file:
            return

        self.displaying_img.load_image(file.text())
        self.update_image_size()

    def update_image_size(self):
        self.change_display_area_size(
            0.4 * self.size().width(), 0.7 * self.size().height()
        )
        # Scale the original image to fit the display area
        self.displaying_img.scaled(self.preview_window.size())
        # Add margins to the scaled image
        self.displaying_img.edit_image()
        # Display the edited scaled image
        self.preview_window.setPixmap(self.displaying_img.preview_image)

    def change_display_area_size(self, width, height):
        self.preview_window.resize(int(width), int(height))

    def add_images(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Image Files (*.jpg *.jpeg *.png)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.file_explorer_listwidget.addItems(selected_files)
        self.file_explorer_listwidget.sortItems()

    def remove_images(self):
        self.file_explorer_listwidget.takeItem(
            self.file_explorer_listwidget.currentRow()
        )
        if self.file_explorer_listwidget.count() == 0:
            self.preview_window.setVisible(False)
            self.logo_svg.setVisible(True)

    # ------------------------------ Margin Control -------------------------------- #

    def update_margin_left(self, value):
        if self.margin_h_lock.isChecked():
            self.margin_right_slider.setValue(value)
            self.displaying_img.set_margins(margin_right=value)
        self.displaying_img.set_margins(margin_left=value)
        if self.preview_window.isVisible() and self.displaying_img is not None:
            self.displaying_img.edit_image()
            self.change_display_area_size(
                self.preview_window.width() + value, self.preview_window.height()
            )
            self.preview_window.setPixmap(self.displaying_img.preview_image)

    def update_margin_right(self, value):
        if self.margin_h_lock.isChecked():
            self.margin_left_slider.setValue(value)
            self.displaying_img.set_margins(margin_left=value)
        self.displaying_img.set_margins(margin_right=value)
        if self.preview_window.isVisible() and self.displaying_img is not None:
            self.displaying_img.edit_image()
            self.change_display_area_size(
                self.preview_window.width() + value, self.preview_window.height()
            )
            self.preview_window.setPixmap(self.displaying_img.preview_image)

    def update_margin_top(self, value):
        if self.margin_v_lock.isChecked():
            self.margin_bottom_slider.setValue(value)
            self.displaying_img.set_margins(margin_bottom=value)
        self.displaying_img.set_margins(margin_top=value)
        if self.preview_window.isVisible() and self.displaying_img is not None:
            self.displaying_img.edit_image()
            self.change_display_area_size(
                self.preview_window.width(), self.preview_window.height() + value
            )
            self.preview_window.setPixmap(self.displaying_img.preview_image)

    def update_margin_bottom(self, value):
        if self.margin_v_lock.isChecked():
            self.margin_top_slider.setValue(value)
            self.displaying_img.set_margins(margin_top=value)
        self.displaying_img.set_margins(margin_bottom=value)
        if self.preview_window.isVisible() and self.displaying_img is not None:
            self.displaying_img.edit_image()
            self.change_display_area_size(
                self.preview_window.width(), self.preview_window.height() + value
            )
            self.preview_window.setPixmap(self.displaying_img.preview_image)

    def update_margin_color(self, color):
        color = QColorDialog().getColor()
        self.displaying_img.set_margins(color=color.getRgb())
        self.displaying_img.edit_image()
        self.preview_window.setPixmap(self.displaying_img.preview_image)

    def h_lock_changed(self):
        if self.margin_h_lock.isChecked():
            self.margin_left_slider.setValue(
                max(self.margin_left_slider.value(), self.margin_right_slider.value())
            )
            self.margin_right_slider.setValue(
                max(self.margin_left_slider.value(), self.margin_right_slider.value())
            )

    def v_lock_changed(self):
        if self.margin_v_lock.isChecked():
            self.margin_top_slider.setValue(
                max(self.margin_top_slider.value(), self.margin_bottom_slider.value())
            )
            self.margin_bottom_slider.setValue(
                max(self.margin_top_slider.value(), self.margin_bottom_slider.value())
            )

    # ------------------------------------------------------------------------------- #

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        if self.preview_window.isVisible() and self.displaying_img is not None:
            self.update_image_size()
