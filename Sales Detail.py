import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt  # Import the Qt module

import pyodbc

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Table from MS SQL Server")
        self.setGeometry(100, 100, 1366, 768)  # Set the window size to 1366x768 pixels
        
        # Create a QLabel to display connection status
        self.connection_status_label = QLabel("Sales Detail", self)
        self.connection_status_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # Set alignment to top-left corner

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)        
        grid_layout = QGridLayout(central_widget)
        
        grid_layout.addWidget(self.connection_status_label, 0, 0, 2, 2) #0, 0, 2(row position from grid), 2
        
        # Add 10 buttons after the label with doubled size
        for i in range(1, 11):
            button = QPushButton(f"Button {i}", self)
            button.setFixedSize(100, 50)  # Set a fixed size (width=100, height=50)
            grid_layout.addWidget(button, 0, i + 1)

        # Create a QLineEdit with coordinates (20, 80) and size (300, 30)
        input_box = QLineEdit(central_widget)
        input_box.setGeometry(10, 70, 1345, 80)
                
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
