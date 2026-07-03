# based on tutorial from: https://www.w3resource.com/python-exercises/pyqt/python-pyqt-widgets-exercise-3.php

import sys

from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import QMainWindow, QToolBar, QApplication, QWidget, QTextEdit, QFileDialog, QVBoxLayout
from layout_color import Color

#imports from PySide

print (sys.path)

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        # set window size and title

        # give the central widget text edit
        self._text_edit = Color('red')
        self.setCentralWidget(self._text_edit)

        # create toolbar -> file with opening and saving


        #open action

        # save action
        pass



    #widget for main window
    #widget for text editing

    #actions for opening and saving
    #connect actions to methods

    #create menu bar and file menu
    #add saving and opening

    #create layout for central wdiget and add text edit

    #set layout as central wediget

    #def open file

    #def save file


#def main

#directly from tutorial bc idk what this does
def main():
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    app.exec()
    pass


if __name__ == "__main__":
    main()


