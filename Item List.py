import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QLabel
import pyodbc
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Table from MS SQL Server")
        self.setGeometry(100, 100, 1366, 768)  # Set the window size to 1366x768 pixels

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(central_widget)

        # Create a QLabel to display connection status
        self.connection_status_label = QLabel()
        grid_layout.addWidget(self.connection_status_label, 0, 0, 1, 2)

        # Create a QTableWidget with columns for specific data
        self.table_widget = QTableWidget()
        headers = ["Item Code", "Barcode", "Item Description", "Unit", "Category", "Default Supplier", "Price", "Quantity", "Inventory", "Locked"]
        self.table_widget.setColumnCount(len(headers))
        self.table_widget.setHorizontalHeaderLabels(headers)

        # Attempt to fetch data from MS SQL Server and populate the table
        if self.fetch_data_and_populate_table():
            self.connection_status_label.setText("Connected to database")
        else:
            self.connection_status_label.setText("Failed to connect to database")

        # Add the QTableWidget to the layout
        grid_layout.addWidget(self.table_widget, 1, 0, 1, 2)

    def fetch_data_and_populate_table(self):
        try:
            # Get database credentials from environment variables
            db_server = os.getenv("DB_SERVER")
            db_database = os.getenv("DB_DATABASE")
            db_username = os.getenv("DB_USERNAME")
            db_password = os.getenv("DB_PASSWORD")

            # Establish a connection to the database            
            connection_string = f'DRIVER={{SQL Server}};SERVER={db_server};DATABASE={db_database};UID={db_username};PWD={db_password}'
            conn = pyodbc.connect(connection_string)

            # Create a cursor
            cursor = conn.cursor()

            # Execute SQL query to fetch specific columns from MstItem table
            query = '''
            SELECT MI.ItemCode, MI.Barcode, MI.ItemDescription, MU.Unit AS Unit, MI.Category, MS.Supplier AS Supplier, MI.Price, MI.OnhandQuantity, MI.IsInventory, MI.IsLocked
            FROM MstItem AS MI
            LEFT JOIN MstUnit AS MU ON MI.UnitId = MU.Id
            LEFT JOIN MstSupplier AS MS ON MI.DefaultSupplierId = MS.Id
            ORDER BY MI.ItemDescription ASC  -- Order by ItemDescription in ascending order (alphabetical)
            '''

            cursor.execute(query)

            # Fetch all rows from the query result
            rows = cursor.fetchall()

            # Populate the QTableWidget with data
            self.table_widget.setRowCount(len(rows))
            for row_num, row_data in enumerate(rows):
                for col_num, cell_value in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_value))
                    self.table_widget.setItem(row_num, col_num, item)

            # Close the cursor and connection
            cursor.close()
            conn.close()

            return True

        except Exception as e:
            print(f"Error: {str(e)}")
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
