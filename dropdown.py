import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QLabel, QVBoxLayout, QWidget, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python PyQt5 Setup Menu")
        self.setGeometry(100, 100, 800, 600)  # Set the window size

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        label = QLabel("Welcome to Setup Menu", self)
        layout.addWidget(label)

        setup_menu = QMenu("Setup", self)

        # Create submenu items (unchanged)
        item_action = QAction("Item", self)
        item_action.triggered.connect(self.item_action_triggered)

        customer_action = QAction("Customer", self)
        customer_action.triggered.connect(self.customer_action_triggered)

        # Create a submenu for "Discount" and add items to it (unchanged)
        discount_submenu = QMenu("Discount", self)

        fixed_discount_action = QAction("Fixed Discount", self)
        fixed_discount_action.triggered.connect(self.fixed_discount_action_triggered)

        percentage_discount_action = QAction("Percentage Discount", self)
        percentage_discount_action.triggered.connect(self.percentage_discount_action_triggered)

        discount_submenu.addAction(fixed_discount_action)
        discount_submenu.addAction(percentage_discount_action)

        currency_action = QAction("Currency", self)
        currency_action.triggered.connect(self.currency_action_triggered)

        user_action = QAction("User", self)
        user_action.triggered.connect(self.user_action_triggered)

        # Add submenu items to the "Setup" menu (unchanged)
        setup_menu.addAction(item_action)
        setup_menu.addAction(customer_action)
        
        # Add the "Discount" submenu to the "Setup" menu (unchanged)
        setup_menu.addMenu(discount_submenu)

        setup_menu.addAction(currency_action)
        setup_menu.addAction(user_action)

        # Set the menu bar to display the "Setup" menu
        self.menuBar().addMenu(setup_menu)

        # Create a button to toggle the menu
        self.toggle_menu_button = QPushButton("Toggle Menu", self)
        self.toggle_menu_button.clicked.connect(self.toggle_menu)
        layout.addWidget(self.toggle_menu_button)

        self.menu_visible = True

    def item_action_triggered(self):
        print("Item menu item clicked.")

    def customer_action_triggered(self):
        print("Customer menu item clicked.")

    def fixed_discount_action_triggered(self):
        print("Fixed Discount menu item clicked.")

    def percentage_discount_action_triggered(self):
        print("Percentage Discount menu item clicked.")

    def currency_action_triggered(self):
        print("Currency menu item clicked.")

    def user_action_triggered(self):
        print("User menu item clicked.")

    def toggle_menu(self):
        if self.menu_visible:
            self.menuBar().setVisible(False)
            self.menu_visible = False
        else:
            self.menuBar().setVisible(True)
            self.menu_visible = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
