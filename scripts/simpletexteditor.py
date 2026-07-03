import sys
from PySide6.QtWidgets import QMainWindow
from layout_color import Color

# Right now, all this shows is a red color.

print(sys.path)


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        # set window size and title

        # give the central widget text edit
        self.text_edit = Color('red')
        self.setCentralWidget(self.text_edit)

        # create toolbar -> file with opening and saving

        # open action

        # save action
        pass

    # widget for main window  # widget for text editing

    # actions for opening and saving  # connect actions to methods

    # create menu bar and file menu  # add saving and opening

    # create layout for central wdiget and add text edit

    # set layout as central wediget

    # def open file

    # def save file
