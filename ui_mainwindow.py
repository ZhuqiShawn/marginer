from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (QCheckBox, QGridLayout, QGroupBox, QHBoxLayout,
                               QLabel, QListWidget, QMainWindow, QPushButton,
                               QSizePolicy, QSlider, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        # -------------------------------------------------------------------------

        # File manager group
        self.file_explorer_groupbox = QGroupBox("Explorer")
        self.file_explorer_groupbox.setFixedWidth(330)
        self.file_explorer_listwidget = QListWidget(self)
        self.file_explorer_listwidget.setFixedWidth(300)
        self.file_explorer_layout = QVBoxLayout()
        self.file_explorer_layout.addWidget(self.file_explorer_listwidget)
        self.file_explorer_groupbox.setLayout(self.file_explorer_layout)

        # File manager buttons
        self.file_manager_groupbox = QGroupBox("Add/Remove Files")
        self.file_manager_groupbox.setFixedWidth(330)
        self.file_manager_groupbox.setFixedHeight(70)
        self.add_file_button = QPushButton("+")
        self.remove_file_button = QPushButton("-")

        self.file_manager_layout = QHBoxLayout()
        self.file_manager_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.file_manager_layout.addWidget(self.add_file_button)
        self.file_manager_layout.addWidget(self.remove_file_button)
        self.file_manager_groupbox.setLayout(self.file_manager_layout)

        # Left layout
        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.file_explorer_groupbox)
        self.left_layout.addWidget(self.file_manager_groupbox)
        self.left_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # -------------------------------------------------------------------------

        # Create a label for the display image
        self.logo_svg = QSvgWidget()
        self.logo_svg.load("assets/home_logo.svg")
        aspect_ratio = (
            self.logo_svg.renderer().defaultSize().width()
            / self.logo_svg.renderer().defaultSize().height()
        )
        self.logo_svg.setFixedSize(400, int(400 / aspect_ratio))
        self.preview_window = QLabel(self)
        self.preview_window.setVisible(False)

        self.mid_layout = QHBoxLayout()
        self.mid_layout.addWidget(
            self.preview_window,
            Qt.AlignmentFlag.AlignCenter,
            Qt.AlignmentFlag.AlignCenter,
        )
        self.mid_layout.addWidget(
            self.logo_svg,
            Qt.AlignmentFlag.AlignCenter,
            Qt.AlignmentFlag.AlignCenter,
        )

        # -------------------------------------------------------------------------

        # Margin control group
        self.margin_controler_group = QGroupBox("Margin Control")
        self.margin_controler_group.setFixedWidth(250)

        self.margin_left_label = QLabel("Left: ")
        self.margin_left_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.margin_left_slider = QSlider(Qt.Orientation.Horizontal)
        self.margin_left_slider.setFixedWidth(150)
        self.margin_left_slider.setMinimum(0)
        self.margin_left_slider.setMaximum(100)
        self.margin_left_slider.setValue(0)

        self.margin_right_label = QLabel("Right: ")
        self.margin_right_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.margin_right_slider = QSlider(Qt.Orientation.Horizontal)
        self.margin_right_slider.setFixedWidth(150)
        self.margin_right_slider.setMinimum(0)
        self.margin_right_slider.setMaximum(100)
        self.margin_right_slider.setValue(0)

        self.margin_top_label = QLabel("Top: ")
        self.margin_top_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.margin_top_slider = QSlider(Qt.Orientation.Horizontal)
        self.margin_top_slider.setFixedWidth(150)
        self.margin_top_slider.setMinimum(0)
        self.margin_top_slider.setMaximum(100)
        self.margin_top_slider.setValue(0)

        self.margin_bottom_label = QLabel("Bottom: ")
        self.margin_bottom_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.margin_bottom_slider = QSlider(Qt.Orientation.Horizontal)
        self.margin_bottom_slider.setFixedWidth(150)
        self.margin_bottom_slider.setMinimum(0)
        self.margin_bottom_slider.setMaximum(100)
        self.margin_bottom_slider.setValue(0)

        self.margin_h_lock = QCheckBox()
        self.margin_v_lock = QCheckBox()
        self.margin_h_lock.setChecked(True)
        self.margin_v_lock.setChecked(True)

        # Color Picker
        self.color_picker_button = QPushButton("Color")

        self.margin_controler_layout = QGridLayout()
        self.margin_controler_layout.addWidget(self.margin_left_label, 0, 0)
        self.margin_controler_layout.addWidget(self.margin_left_slider, 0, 1)
        self.margin_controler_layout.addWidget(self.margin_right_label, 1, 0)
        self.margin_controler_layout.addWidget(self.margin_right_slider, 1, 1)
        self.margin_controler_layout.addWidget(self.margin_h_lock, 0, 2, 2, 1)
        self.margin_controler_layout.addWidget(self.margin_top_label, 2, 0)
        self.margin_controler_layout.addWidget(self.margin_top_slider, 2, 1)
        self.margin_controler_layout.addWidget(self.margin_bottom_label, 3, 0)
        self.margin_controler_layout.addWidget(self.margin_bottom_slider, 3, 1)
        self.margin_controler_layout.addWidget(self.margin_v_lock, 2, 2, 2, 1)
        self.margin_controler_layout.addWidget(self.color_picker_button, 4, 0, 1, 2)
        self.margin_controler_group.setLayout(self.margin_controler_layout)

        # Right layout
        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(self.margin_controler_group)
        self.right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # -------------------------------------------------------------------------

        # Main window layout
        main_window_layout = QHBoxLayout()
        main_window_layout.addLayout(self.left_layout, 1)
        main_window_layout.addLayout(self.mid_layout, 3)
        main_window_layout.addLayout(self.right_layout, 1)
        self.setLayout(main_window_layout)

        # Central widget
        widget = QWidget(self)
        widget.setLayout(main_window_layout)
        self.setCentralWidget(widget)
