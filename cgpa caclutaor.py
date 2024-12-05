print("cgpa calcator ")
A_plus=4
A=3.7
B_plus=3.5
B=3.3
C_plus=3
C=2.7
D_plus=2.5
D=2.3
total_english=int(input("enter the total marks of english"))
english=int(input("enter the marks you obtain in english"))
total_math=int(input("enter the total marks of math"))
math=int(input("enter the marks you obtain in math"))
total_marks=total_math+total_english
obtain_marks=english+math
percentage=(obtain_marks*100)/total_marks
total_CGPA_POINTS=8
math_percent=(math*100)/total_math
english_percent=(english*100)/total_english
if english_percent>=85 and english_percent<100:
    print("you got an A1 in English ")
    ge=A_plus
elif english_percent>=80 and english_percent<85:
    print("you got A- in English ")
    ge=A
elif english_percent>=70 and english_percent<80:
    print("you got B+ in English ")
    ge=B_plus
elif english_percent>=65 and english_percent<70:
    print("you got B- in English ")
    ge=B
elif english_percent>=55 and english_percent<65:
    print("you got C+ in English ")
    ge=C_plus
elif english_percent>=50 and english_percent<55:
    print("you got C- in English ")
    ge=C
elif english_percent>=45 and english_percent<50:
    print("you got D+ in English ")
    ge=D_plus
elif english_percent>=40 and english_percent<45:
    print("you got D- in English ")
    ge=D
else :
    print("fail sorry")
print("your percentage in english ",english_percent)
print("your grade point in english is ",ge)
if math_percent>=85 and math_percent<100:
    print("you got an A1 in math ")
    gm=A_plus
elif math_percent>=80 and math_percent<85:
    print("you got A- in math ")
    gm=A
elif math_percent>=70 and math_percent<80:
    print("you got B+ in math ")
    gm=B_plus
elif math_percent>=65 and math_percent<70:
    print("you got B- in math ")
    gm=B
elif math_percent>=55 and math_percent<65:
    print("you got C+ in math ")
    gm=C_plus
elif math_percent>=50 and math_percent<55:
    print("you got C- in math ")
    gm=C
elif math_percent>=45 and math_percent<50:
    print("you got D+ in math ")
    gm=D_plus
elif math_percent>=40 and math_percent<45:
    print("you got D- in math ")
    gm=D
else :
    print("sorry fail")
print("your percentage in math is ", math_percent)
print("your grade point in math is ",gm )
obtain_grade=ge+gm
percentage_cgpa=obtain_grade/2

if percentage_cgpa>=3.7 and percentage_cgpa<4:
    print("you got  CGPA  ",percentage_cgpa)

elif percentage_cgpa>=3.5 and percentage_cgpa<3.7:
    print("you got  CGPA ",percentage_cgpa)

elif percentage_cgpa>=3.3 and percentage_cgpa<3.5:
    print("you got  CGPA  ",percentage_cgpa)

elif percentage_cgpa>=3 and percentage_cgpa<3.3:
    print("you got  CGPA ",percentage_cgpa)

elif percentage_cgpa>=2.7 and percentage_cgpa<3:
    print("you got  CGPA ",percentage_cgpa)

elif percentage_cgpa>=2.5 and percentage_cgpa<2.7:
    print("you got  CGPA ",percentage_cgpa)

elif percentage_cgpa>=2.3 and percentage_cgpa<2.5:
    print("you got  CGPA ",percentage_cgpa)

elif percentage_cgpa>=2 and percentage_cgpa<2.3:
    print("you got  CGPA ",percentage_cgpa)
else:
    print("FAIL SORRY")
print("Your percentage ",percentage)


