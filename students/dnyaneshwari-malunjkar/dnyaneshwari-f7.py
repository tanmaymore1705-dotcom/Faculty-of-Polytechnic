#problem
def add_item(price, subtotal):
    return subtotal + price

def apply_tax(subtotal, tax_rate):
    tax = subtotal * tax_rate
    return subtotal + tax

def main():
    
    total = 0
    
    total = add_item(10, total)
    total = add_item(25, total)   
    total = add_item(5, total)    
    total = apply_tax(total, 0.10)  
    
    print(f"Correct total: {total}")

if __name__ == "__main__":
    main()
