i, j = 0, 0 #학점 총합, 전공과목별 (학점 × 과목평점)의 합
grade_info = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
for _ in range(20):
    course, score, grade = input().split()
    if grade == 'P':
        continue
    else:
        i += float(score)
        j += float(score) * grade_info[grade]
print("{0:.6f}".format(j/i))