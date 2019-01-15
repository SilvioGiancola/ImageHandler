from PyQt5.QtWidgets import QMainWindow, QApplication # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication

from app import ImageHandlerApp # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer



def main():
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = ImageHandlerApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
