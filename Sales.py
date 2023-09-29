import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QComboBox, QHBoxLayout, QTabWidget, QVBoxLayout, QTextEdit, QDateEdit, QLineEdit

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Table from MS SQL Server")
        self.setGeometry(100, 100, 1366, 768)  # Set the window size to 1366x768 pixels

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(central_widget)

        # Create the calendar widget as a dropdown
        calendar_dropdown = QDateEdit(self)
        calendar_dropdown.setCalendarPopup(True)  # Show calendar when clicked
        
        # Create the second dropdown box with input box
        label2 = QLabel("Dropdown 2:", self)
        combo_box2 = QComboBox(self)
        combo_box2.addItem("Option A")
        combo_box2.addItem("Option B")
        input_box2 = QLineEdit(self)

        # Create a horizontal layout for the input boxes and calendar
        input_layout = QHBoxLayout()
        input_layout.addWidget(label2)
        input_layout.addWidget(combo_box2)
        input_layout.addWidget(input_box2)
        input_layout.addWidget(calendar_dropdown)  # Add the calendar to the same layout

        # Create a QTabWidget with three tabs
        tab_widget = QTabWidget(self)
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()

        # Add text editors to each tab
        text_edit1 = QTextEdit(tab1)
        text_edit2 = QTextEdit(tab2)
        text_edit3 = QTextEdit(tab3)

        # Add tabs to the tab widget
        tab_widget.addTab(tab1, "Tab 1")
        tab_widget.addTab(tab2, "Tab 2")
        tab_widget.addTab(tab3, "Tab 3")

        # Create a vertical layout for the tab widget
        tab_layout = QVBoxLayout()
        tab_layout.addWidget(tab_widget)

        # Calculate the button height based on the window size
        button_height = int(self.height() * 1.25)  # Convert to integer

        # Calculate the maximum height for the buttons
        max_button_height = int(button_height * 0.5)  # Set the maximum height to 50% of the calculated height

        # Create two buttons
        button1 = QPushButton("Button 1", self)
        button2 = QPushButton("Button 2", self)

        # Set the fixed height for both buttons to the maximum height
        button1.setFixedHeight(max_button_height)
        button2.setFixedHeight(max_button_height)

        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        # Add widgets to the layout
        grid_layout.addLayout(input_layout, 0, 0, 1, 6)  # Align input boxes and calendar horizontally
        grid_layout.addLayout(tab_layout, 1, 0, 1, 6)  # Align tab widget horizontally
        grid_layout.addLayout(button_layout, 2, 0, 1, 6)  # Align buttons horizontally

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
