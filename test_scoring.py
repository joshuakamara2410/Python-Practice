MAXIMUM_SCORE = 100
MINIMUM_SCORE = 1
testScore = int(input("Test Score?: "))
if testScore >= 90:
    grade = "A"
elif testScore >= 70:
    grade = "B"
elif testScore >= 60:
    grade = "C"
elif testScore >= 45:
    grade = "D"
elif testScore >= 20:
    grade = "E"
elif testScore <= 20:
    grade = "F"
if testScore > MAXIMUM_SCORE or testScore < MINIMUM_SCORE:
    print("That score is invalid")
else:
    print(f"Your score is {testScore} and your grade is {grade}")

    
