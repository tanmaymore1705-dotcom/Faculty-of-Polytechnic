total = 0


# BUG: this function ignores its job. It reads and OVERWRITES the global
#      `total` instead of adding `price` to a running total and RETURNING it.
# TODO: refactor to  def add_item(running_total, price):  and
#       return  running_total + price   (no `global`, no reading the global).
def add_item(price):
    global total
    total += price          # overwrites the running total every single time!
    return total


# BUG: this function reads the global `total` instead of receiving the
#      cart total as a PARAMETER. If `total` changes elsewhere, this lies.
# TODO: refactor to  def apply_tax(cart_total):  and return cart_total * 1.05
def apply_tax():
    return total * 5/100


def main():
    add_item(40)    # bread
    add_item(25)    # milk
    add_item(15)    # eggs

    print(f"Items added. Cart total: {total}")
    print(f"With 5% tax: {apply_tax():.2f}")


if __name__ == "__main__":
    main()
