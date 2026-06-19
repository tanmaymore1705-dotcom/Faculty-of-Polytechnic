def add_item(running_total, price):
    return running_total + price
def apply_tax(cart_total):
    return cart_total * 1.05
def main():
    total = 0
    total = add_item(total, 40)
    total = add_item(total, 25)
    total = add_item(total, 15)
    print(f"Items added. Cart total: {total}")
    taxed_total = apply_tax(total)
    print(f"With 5% tax: {taxed_total:.2f}")
main()
