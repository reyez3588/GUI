# Only needed for access to command line arguments
import sys
#Necesarias para cargar librerias QT
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 300))
        self.setWindowTitle("My first GUI")
        button = QPushButton("Push One")
        self.setCentralWidget(button) #agregar el botón creado a la ventana principal

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window. any could be a window
#window = QWidget()
#window = QPushButton(" Botototon ")
window = mainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()
# Your application won't reach here until you exit and the event
# loop has stopped.
