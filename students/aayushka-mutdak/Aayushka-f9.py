for x in range(3):
    n= input("enter name:")
    a = int(input("enter marks:"))
    b = int(input("enter marks:"))
    c = int(input("enter marks:"))
    t = a + b + c
    av = t / 3
    print("Name: " + n)
    print("Marks: " + str(a) + ", " + str(b) + ", " + str(c))
    print("Total: " + str(t) + " / 300")
    print("Average: " + str(round(av, 2)))
    if av < 35:
     print("Result: FAIL")
    elif av >= 75:
     print("Result: PASS (Distinction)")
    else:
     print("Result: PASS")
print("-----------------------")
