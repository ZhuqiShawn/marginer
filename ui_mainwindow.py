from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (QGridLayout, QGroupBox, QHBoxLayout, QLabel,
                               QListWidget, QPushButton, QSizePolicy, QSlider,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        self.photo_display = QLabel(self)
        self.photo_display.setVisible(False)

        self.mid_layout = QHBoxLayout()
        self.mid_layout.addWidget(self.photo_display, Qt.AlignCenter, Qt.AlignCenter)
        self.mid_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        # -------------------------------------------------------------------------

        # Margin control group
        self.margin_controler_group = QGroupBox("Margin Control")
        self.margin_controler_group.setFixedWidth(250)

        self.margin_h_label = QLabel("Margin x: ")
        self.margin_h_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.margin_h_slider = QSlider(Qt.Orientation.Horizontal)
        self.margin_h_slider.setFixedWidth(150)
        self.margin_h_slider.setMinimum(0)
        self.margin_h_slider.setMaximum(400)
        self.margin_h_slider.setValue(0)

        self.margin_v_label = QLabel("Margin y: ")
        self.margin_v_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.margin_v_slider = QSlider(Qt.Orientation.Horizontal)
        self.margin_v_slider.setFixedWidth(150)
        self.margin_v_slider.setMinimum(0)
        self.margin_v_slider.setMaximum(600)
        self.margin_v_slider.setValue(0)

        self.margin_h_offset_label = QLabel("Offset x: ")
        self.margin_h_offset_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.margin_h_offset_slider = QSlider(Qt.Orientation.Horizontal)
        self.margin_h_offset_slider.setFixedWidth(150)
        self.margin_h_offset_slider.setMinimum(-200)
        self.margin_h_offset_slider.setMaximum(200)
        self.margin_h_offset_slider.setValue(0)

        self.margin_v_offset_label = QLabel("Offset y: ")
        self.margin_v_offset_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.margin_v_offset_slider = QSlider(Qt.Orientation.Horizontal)
        self.margin_v_offset_slider.setFixedWidth(150)
        self.margin_v_offset_slider.setMinimum(-300)
        self.margin_v_offset_slider.setMaximum(300)
        self.margin_v_offset_slider.setValue(0)

        # Color Picker
        self.color_picker_button = QPushButton("Color")

        self.margin_controler_layout = QGridLayout()
        self.margin_controler_layout.addWidget(self.margin_h_label, 0, 0)
        self.margin_controler_layout.addWidget(self.margin_h_slider, 0, 1)
        self.margin_controler_layout.addWidget(self.margin_v_label, 1, 0)
        self.margin_controler_layout.addWidget(self.margin_v_slider, 1, 1)
        self.margin_controler_layout.addWidget(self.color_picker_button, 2, 0, 1, 2)
        self.margin_controler_group.setLayout(self.margin_controler_layout)
        self.margin_controler_layout.addWidget(self.margin_h_offset_label, 3, 0)
        self.margin_controler_layout.addWidget(self.margin_h_offset_slider, 3, 1)
        self.margin_controler_layout.addWidget(self.margin_v_offset_label, 4, 0)
        self.margin_controler_layout.addWidget(self.margin_v_offset_slider, 4, 1)

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
