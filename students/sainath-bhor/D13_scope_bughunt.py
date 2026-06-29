def add_item(running_total, price):
    return running_total + price

def apply_tax(cart_total):
    return cart_total * 1.05

def main():
    total = 0

    total = add_item(total, 40)
    total = add_item(total, 25)
    total = add_item(total, 15)

    print("Items added. Cart total:", total)
    print("With 5% tax:", f"{apply_tax(total):.2f}")

main()
