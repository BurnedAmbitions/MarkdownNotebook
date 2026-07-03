import sys
from PySide6.QtWidgets import QApplication
from scripts.simpletexteditor import TextEditor


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
