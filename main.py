from PyQt5.QtWidgets import QApplication
import sys  # We need sys so that we can pass argv to QApplication
from app import ImageHandlerApp


def main():
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = ImageHandlerApp()      # We set the form to be our design
    form.show()                   # Show the form
    app.exec_()                   # and execute the app


# check if we're running file directly and not importing it
if __name__ == '__main__':
    main()                        # run the main function
