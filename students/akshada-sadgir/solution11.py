#problem1
number_of_subjects= 3
pass_mark= 35
distinction_mark= 75

def print_report(name,mark1,mark2, mark3):
    total=mark1+mark2+mark3
    average=total/number_of_subjects

    print("Name:",name)
    print("Total:",total)
    print("Average:",average)

    if mark1>=pass_mark and mark2 >=pass_mark and mark3 >=pass_mark:
        print("Result:Pass")
    else:
        print("Result:Fail")

    if average>=distinction_mark:
        print("Grade:Distinction")
        print()

for i in range(3):
    name=input("Enter name:")
    mark1=int(input("Enter mark 1:"))
    mark2=int(input("Enter mark 2:"))
    mark3=int(input("Enter mark 3:"))

    print_report(name,mark1,mark2, mark3)
