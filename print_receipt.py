import textwrap

def print_receipt(products, total_amount):
    print("********** Receipt **********")
    for product, quantity, price in products:
        wrapped_name = textwrap.fill(product, width=20)
        line = f"{wrapped_name:<25} {quantity} x ${price:.2f}"
        print(line)
    print("-----------------------------")
    print(f"Total Amount: ${total_amount:.2f}")
    print("*****************************")

# Sample data
products = [("Product A", 3, 5.99), ("Product B", 2, 9.99), ("Product C", 1, 2.49)]
total_amount = sum(quantity * price for _, quantity, price in products)

# Call the print_receipt function
print_receipt(products, total_amount)
