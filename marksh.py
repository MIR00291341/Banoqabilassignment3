sub1=int(input("Enter your Math Marks out of 100:" ))
sub2=int(input("Enter your Urdu Marks out of 100: "))
sub3=int(input("Enter your English Marks out of 100: "))
sub4=int(input("Enter your Computer Science Marks out of 100: "))
sum = sub1+sub2+sub3+sub4
print("Your total obtained Marks is", sum)
grade = (sum/400*100)

if grade >=90:
    print("\n\n Congratulations! Your grade is A+")
elif grade >=80:
    print("\n\n Congratulations! Your grade is A")
elif grade >=70:
    print("\n\n Congratulations! Your grade is B")
elif grade >=60:
    print("\n\n Congratulations! Your grade is C")
elif grade >=50:
    print("\n\n sorry! Your grade is D")
elif grade >=40:
    print("\n\n sorry! Your grade is F")
else:
    print("Your Are Fail")