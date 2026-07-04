import sys

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLayout, QSizePolicy
from layout_color import Color

# Right now, all this shows is a red color.

print(sys.path)

wColors = {
    "text_edit" : QColor(221, 23, 34), # red
    "file_tree" : QColor(0, 94, 173), # blue
    "tabs" : QColor(136, 0, 24), # dark red
    "upper_bar" : QColor(118, 0, 197), # purple
    "sidebar" : QColor(245, 40, 145), # pink
    "status_bar" : QColor(0, 204, 95) # green
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window size and title
        self.setWindowTitle("Markdown Editor")

        # TODO: Window Size, Minimum/Maximum

        # TODO: text editor widget
        text_widget = Color(wColors["text_edit"])

        # TODO: file tree widget
        file_tree_widget = Color(wColors["file_tree"])

        # TODO: sidebar widget
        sidebar_widget = Color(wColors["sidebar"])

        sidebar_widget.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)

        # TODO: upper bar widget
        upper_bar_widget = Color(wColors["upper_bar"])

        # TODO: tabs widget
        tabs_widget = Color(wColors["tabs"])

        # TODO: status bar
        status_bar_widget = Color(wColors["status_bar"])

        #layout with status bar, textedit, tabs
        layout1 = QVBoxLayout()
        layout1.addWidget(tabs_widget)
        layout1.addWidget(text_widget)
        layout1.addWidget(status_bar_widget)

        layout2 = QHBoxLayout()
        layout2.addWidget(sidebar_widget)
        layout2.addWidget(file_tree_widget)
        layout2.addLayout(layout1)

        layout2.setContentsMargins(0,0,0,0)
        layout2.setSpacing(0)

        central_widget = QWidget()
        central_widget.setLayout(layout2)
        self.setCentralWidget(central_widget)

        pass

