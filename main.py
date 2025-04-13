score = int(input("How many scores do you get? "))

grade = 0

if score >= 80:
    grade = "A"
elif score >= 75 and score < 80:
    grade = "B+"
elif score >= 70 and score < 75:
    grade = "B"
elif score >= 65 and score < 70:
    grade = "C+"
elif score >= 60 and score < 65:
    grade = "C"
elif score >= 55 and score < 60:
    grade = "D+"
elif score >= 50 and score < 55:
    grade = "D"
else: grade = "F"

print(f"your grade is {grade}")

#hello