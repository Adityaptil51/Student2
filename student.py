import sys

script_name = sys.argv[0]

# Check if 5 subject marks are provided as command-line arguments
if len(sys.argv) == 6:
    print("Marks received from Jenkins parameters.")
    marks = list(map(float, sys.argv[1:6]))
else:
    print("No parameters given — enter marks manually.")
    marks = []
    for i in range(1, 6):
        m = float(input(f"Enter marks for Subject {i}: "))
        marks.append(m)

print("\nScript Name:", script_name)
print("Marks:", marks)

# --- Calculate average ---
avg = sum(marks) / 5

# --- Very Good Marks (above 90) ---
vg_marks = [m for m in marks if m > 90]

# --- Grade calculation ---
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

# --- Output ---
print("\n----- RESULT -----")
print("Average:", avg)
print("Very Good Marks (>90):", vg_marks if vg_marks else "None")
print("Grade:", grade)
