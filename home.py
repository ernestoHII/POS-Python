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
            ("POS Report", "img/Reports.png"),  # Corrected path
            ("Discounting", "img/Discounting.png"),  # Corrected path
            ("Cash In/Out", "img/Disbursement.png"),  # Corrected path
            ("Remittance Report", "img/Reports.png"),
            ("Settings", "img/Settings.png"),  # Corrected path
            ("Customer", "img/Customer.png"),  # Corrected path
            ("Stock In", "img/Stock In.png"),  # Corrected path
            ("Inventory Report", "img/Reports.png"),
            ("Utilities", "img/Utilities.png"),  # Corrected path
            ("User", "img/User.png"),  # Corrected path
            ("Stock Out", "img/Stock Out.png"),  # Corrected path
            ("Stock Count", "img/Stock Count.png"),  # Corrected path
            ("System Tables", "img/System Tables.png"),  # Corrected path
        ]

        for row in range(4):
            for col in range(4):
                index = row * 4 + col
                if index < len(button_info):
                    button_text, icon_path = button_info[index]
                    container = QWidget()
                    layout = QVBoxLayout(container)
                    button = QPushButton()
                    size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    button.setSizePolicy(size_policy)

                    pixmap = QPixmap()
                    if not pixmap.load(icon_path):
                        print("Error loading image:", pixmap.isNull())
                    else:
                        pixmap = pixmap.scaledToHeight(128)
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

                    grid_layout.addWidget(container, row, col)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
