import sys
import socket  # Import the socket module for network connectivity check
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QTabWidget, QTextEdit

class POSApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple POS System")
        self.setGeometry(100, 100, 1366, 768)  # Set the GUI size to 1366x768

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.total_amount = 0
        self.total_label = QLabel("Total Amount: $0.00")
        self.layout.addWidget(self.total_label)

        self.product_buttons = []
        self.product_quantities = {}  # Dictionary to store product quantities

        # Sample product buttons
        products = [("Product A", 5.99), ("Product B", 9.99), ("Product C", 2.49)]
        for product_name, product_price in products:
            button = QPushButton(f"{product_name} - ${product_price:.2f}")
            button.clicked.connect(lambda _, name=product_name, price=product_price: self.add_to_total(name, price))
            self.product_buttons.append(button)
            self.layout.addWidget(button)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        # Create a tab for printing (initially disabled)
        self.print_tab = QWidget()
        self.tab_widget.addTab(self.print_tab, "Print")
        self.print_tab.setEnabled(False)

        self.print_layout = QVBoxLayout()
        self.print_button = QPushButton("Print Receipt")
        self.print_button.clicked.connect(self.print_receipt)
        self.print_layout.addWidget(self.print_button)
        self.print_text = QTextEdit()
        self.print_layout.addWidget(self.print_text)
        self.print_tab.setLayout(self.print_layout)

        self.central_widget.setLayout(self.layout)

    def add_to_total(self, product_name, price):
        self.total_amount += price
        self.total_label.setText(f"Total Amount: ${self.total_amount:.2f}")

        # Enable the "Print" tab when there's a transaction
        self.print_tab.setEnabled(True)

        # Increment product quantity or initialize to 1 if it's the first time
        if product_name in self.product_quantities:
            self.product_quantities[product_name] += 1
        else:
            self.product_quantities[product_name] = 1

    def is_network_online(self):
        try:
            # Attempt to connect to a known external server (e.g., Google's DNS server)
            socket.create_connection(("8.8.8.8", 53), timeout=5)
            return True
        except OSError:
            pass
        return False

    def print_receipt(self):
        receipt_text = "Receipt:\n"

        for product_name, quantity in self.product_quantities.items():
            receipt_text += "{} x {} - ${:.2f}\n".format(product_name, quantity, quantity * float(self.product_buttons[0].text().split(' - $')[1]))

        receipt_text += f"Total Amount: ${self.total_amount:.2f}\n"

        # Check network connectivity before setting the receipt text
        if not self.is_network_online():
            receipt_text += "\nNetwork is offline. Data will be synced as soon as the network is back online."

        self.print_text.setPlainText(receipt_text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = POSApp()
    window.show()
    sys.exit(app.exec_())
