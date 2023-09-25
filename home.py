import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QVBoxLayout, QLabel, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 4x4 Grid of Buttons")
        self.setGeometry(100, 100, 1366, 768)  # Set the window size to 1366x768 pixels

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(central_widget)

        # Create and add buttons to the grid layout
        button_info = [
            ("Item", "img/Item.png"),
            ("POS - F2", "img/POS.png"),
            ("Sales Report", "img/Reports.png"),
            ("POS Report", "img/Reports.png"),
            ("Discounting", "icon5.png"),
            ("Cash In/Out", "icon6.png"),
            ("Remittance Report", "img/Reports.png"),
            ("Settings", "icon8.png"),
            ("Customer", "icon9.png"),
            ("Stock In", "icon10.png"),
            ("Inventory Report", "img/Reports.png"),
            ("Utilities", "icon12.png"),
            ("User", "icon13.png"),
            ("Stock Out", "icon14.png"),
            ("Stock Count", "icon15.png"),
            ("System Tables", "icon16.png"),
        ]

        for row in range(4):
            for col in range(4):
                index = row * 4 + col
                if index < len(button_info):
                    button_text, icon_path = button_info[index]
                    button = QPushButton()
                    layout = QVBoxLayout()
                    button.setLayout(layout)
                    size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    button.setSizePolicy(size_policy)
                    
                    # Load the icon and resize it to double its default size
                    pixmap = QPixmap(icon_path)
                    pixmap = pixmap.scaledToHeight(128)  # Set the height as needed
                    icon = QIcon(pixmap)
                    button.setIcon(icon)
                    button.setIconSize(pixmap.size())
                    
                    # Create a label for the button title (text)
                    title_label = QLabel(button_text)
                    title_label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)  # Align text to bottom center
                    
                    # Make the text bold
                    font = QFont()
                    font.setBold(True)
                    title_label.setFont(font)
                    
                    layout.addWidget(button)
                    layout.addWidget(title_label)
                    
                    grid_layout.addWidget(button, row, col)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
