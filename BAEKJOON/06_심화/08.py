import sys

total_weighted_score = 0
total_score = 0

for i in range(20):
    sub, score, grade = input().split()
    score = float(score)

    if grade == "A+":
        grade_score = 4.5
    elif grade == "A0":
        grade_score = 4.0
    elif grade == "B+":
        grade_score = 3.5
    elif grade == "B0":
        grade_score = 3.0
    elif grade == "C+":
        grade_score = 2.5
    elif grade == "C0":
        grade_score = 2.0
    elif grade == "D+":
        grade_score = 1.5
    elif grade == "D0":
        grade_score = 1.0
    elif grade == "F":
        grade_score = 0.0
    elif grade == "P":
        continue

    total_score += score
    total_weighted_score += score * grade_score

average = total_weighted_score / total_score
print(average)
