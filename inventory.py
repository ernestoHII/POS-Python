import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit

class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

class InventoryManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Management")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.product_name_label = QLabel("Product Name:")
        self.product_name_input = QLineEdit()
        self.layout.addWidget(self.product_name_label)
        self.layout.addWidget(self.product_name_input)

        self.product_category_label = QLabel("Product Category:")
        self.product_category_input = QLineEdit()
        self.layout.addWidget(self.product_category_label)
        self.layout.addWidget(self.product_category_input)

        self.product_price_label = QLabel("Product Price:")
        self.product_price_input = QLineEdit()
        self.layout.addWidget(self.product_price_label)
        self.layout.addWidget(self.product_price_input)

        self.product_quantity_label = QLabel("Product Quantity:")
        self.product_quantity_input = QLineEdit()
        self.layout.addWidget(self.product_quantity_label)
        self.layout.addWidget(self.product_quantity_input)

        self.add_product_button = QPushButton("Add Product")
        self.add_product_button.clicked.connect(self.add_product)
        self.layout.addWidget(self.add_product_button)

        self.check_low_stock_button = QPushButton("Check Low Stock")
        self.check_low_stock_button.clicked.connect(self.check_low_stock)
        self.layout.addWidget(self.check_low_stock_button)

        self.result_text = QTextEdit()
        self.layout.addWidget(self.result_text)

        self.inventory_manager = []

        self.central_widget.setLayout(self.layout)

    def add_product(self):
        name = self.product_name_input.text()
        category = self.product_category_input.text()
        price = float(self.product_price_input.text())
        quantity = int(self.product_quantity_input.text())

        product = Product(name, category, price, quantity)
        self.inventory_manager.append(product)

        self.result_text.append(f"Added Product: {name}, Category: {category}, Price: ${price:.2f}, Quantity: {quantity}")

    def check_low_stock(self):
        threshold = 10
        low_stock_products = []

        for product in self.inventory_manager:
            if product.quantity <= threshold:
                low_stock_products.append(product)

        if low_stock_products:
            self.result_text.append("Low Stock Products:")
            for product in low_stock_products:
                self.result_text.append(f"Name: {product.name}, Category: {product.category}, Quantity: {product.quantity}")
        else:
            self.result_text.append("No low stock products.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryManagerApp()
    window.show()
    sys.exit(app.exec_())
