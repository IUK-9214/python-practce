limitup = 100
limitdown = 0
GPe = 0
GPu = 0
english = float(input("Enter your marks in English : "))
if english > limitup and english < limitdown:
    print("Invalid Number!")
elif english >= 90 and english <= 100:
    print("Grade in English:")
    print("A")
elif english >= 80 and english < 90:
    print("Grade in English:")
    print("A-")

elif english >= 70 and english < 80:
    print("Grade in English:")
    print("B")

elif english >= 60 and english < 70:
    print("Grade in English:")
    print("B-")

elif english >= 50 and english < 60:
    print("Grade in English:")
    print("C")

elif english >= 40 and english < 50:
    print("Grade in English:")
    print("C-")

else:
    print("Fail")
GPe = (english / 200) * 4.0
print(f"Total Grade points: {GPe}")

urdu = float(input("Enter your marks in Urdu: "))
print("Grade in Urdu:")
if urdu > limitup and urdu < limitdown:
    print("Invalid Number!")
elif urdu >= 90 and urdu <= 100:
    print("A")

elif urdu >= 80 and urdu < 90:
    print("A-")

elif urdu >= 70 and urdu < 80:
    print("B")

elif urdu >= 60 and urdu < 70:
    print("B-")

elif urdu >= 50 and urdu < 60:
    print("C")

elif urdu >= 40 and urdu < 50:
    print("C-")

else:
    print("Fail")
GPu = (urdu / 200) * 4.0
print(f"Total Grade points: {GPu}")
ADD = urdu + english
total = 200
per = (ADD * 100) / total
print(f"Your Percentage is :{per}")
print("Your overall GRADE is: ")
if per > limitup or per < limitdown:
    print("Invalid Number!")
elif per >= 90:
    print("A")
elif per >= 80:
    print("A-")
elif per >= 70:
    print("B")
elif per >= 60:
    print("B-")
elif per >= 50:
    print("C")
elif per >= 40:
    print("C-")
else:
    print("Fail")
totalGP = GPe + GPu
print(f"CGPA = {totalGP}")