import sys

if len(sys.argv) != 6:
    print("Usage: <SUB1> <SUB2> <SUB3> <SUB4> <SUB5>")
    sys.exit(1)

marks = list(map(float, sys.argv[1:6]))

print("Marks:", marks)

# Calculate average
avg = sum(marks) / 5

# Very good marks > 90
vg_marks = [m for m in marks if m > 90]

if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\n===== RESULT =====")
print("Average:", avg)
print("Grade:", grade)
