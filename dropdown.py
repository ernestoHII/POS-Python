import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QLabel, QVBoxLayout, QWidget

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

        setup_menu = self.menuBar().addMenu("Setup")

        # Create submenu items
        item_action = QAction("Item", self)
        item_action.triggered.connect(self.item_action_triggered)

        customer_action = QAction("Customer", self)
        customer_action.triggered.connect(self.customer_action_triggered)

        discount_action = QAction("Discount", self)
        discount_action.triggered.connect(self.discount_action_triggered)

        currency_action = QAction("Currency", self)
        currency_action.triggered.connect(self.currency_action_triggered)

        user_action = QAction("User", self)
        user_action.triggered.connect(self.user_action_triggered)

        # Add submenu items to the "Setup" menu
        setup_menu.addAction(item_action)
        setup_menu.addAction(customer_action)
        setup_menu.addAction(discount_action)
        setup_menu.addAction(currency_action)
        setup_menu.addAction(user_action)

    def item_action_triggered(self):
        print("Item menu item clicked.")

    def customer_action_triggered(self):
        print("Customer menu item clicked.")

    def discount_action_triggered(self):
        print("Discount menu item clicked.")

    def currency_action_triggered(self):
        print("Currency menu item clicked.")

    def user_action_triggered(self):
        print("User menu item clicked.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
