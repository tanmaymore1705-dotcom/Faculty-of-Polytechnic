#1

n=5
students=[]
for x in range (n):
  name=input (f" Enter the name of student {x+1}:")
  students.append(name)
print(students)  # FIX(faculty): print the list variable, not the literal string "students"

#2
num=10
unum=0
while True:
  uinp=int(input ("guess a num 1 to 10:"))
  if uinp!=num:
      print ("incorrect")
  else:
      print ("correct")
      break
