name= input('enter your name')
mark = int(input("enter your mark"))

if mark >=90:
    grade ="A+"
elif mark>=80:
    grade ="A"
elif mark>=70:
    grade ="B+" 
elif mark>=60:
    grade ="B"
elif mark>=50:
    grade="C+"
elif mark>=40:
    grade="C"
else:
    grade ="FAIL"
print()
print("student",name)
print("mark",mark)
print("grade",grade)


