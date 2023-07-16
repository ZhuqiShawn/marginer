import cv2
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QColorDialog, QFileDialog, QLabel, QMainWindow

from ui_mainwindow import Ui_MainWindow

MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT = 1400, 800
IMAGE_DISPLAY_WIDTH, IMAGE_DISPLAY_HEIGHT = 800, 600


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        # Main window title and dimensions
        self.setWindowTitle("Marginer")
        self.setGeometry(300, 400, MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)

        # Connections
        self.add_file_button.clicked.connect(self.add_images)
        self.file_explorer_listwidget.currentItemChanged.connect(self.show_image)
        self.remove_file_button.clicked.connect(self.remove_images)
        self.margin_h_slider.valueChanged.connect(self.print_value)
        self.margin_v_slider.valueChanged.connect(self.print_value)
        self.margin_h_offset_slider.valueChanged.connect(self.print_value)
        self.margin_v_offset_slider.valueChanged.connect(self.print_value)
        self.color_picker_button.clicked.connect(self.color_button_clicked)

    @Slot()
    def show_image(self, file):
        if self.logo_svg.isVisible():
            self.logo_svg.hide()
        
        if not self.photo_display.isVisible():
            self.photo_display.setVisible(True)
        
        if not file:
            return
        
        self.photo_display.setMinimumHeight(IMAGE_DISPLAY_HEIGHT)
        self.photo_display.setMinimumWidth(IMAGE_DISPLAY_WIDTH)

        img = QPixmap(file.text())
        self.photo_display.setPixmap(
            img.scaled(
                0.8 * self.photo_display.width(),
                0.8 * self.photo_display.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
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
        self.file_explorer_listwidget.takeItem(self.file_explorer_listwidget.currentRow())
        if self.file_explorer_listwidget.count() == 0:
            self.photo_display.setVisible(False)
            self.logo_svg.setVisible(True)

    def print_value(self, value):
        print(value)
