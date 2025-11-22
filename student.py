import sys

# --- Command-line input handling ---
if len(sys.argv) == 3:
    script_name = sys.argv[0]
    name = sys.argv[1]
    rollno = sys.argv[2]
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    name = "Aditya"
    rollno = "270"
    print("No input given - using default values:")

print("Script Name:", script_name)
print("Student Name:", name)
print("Roll Number:", rollno)

# --- Input marks for 5 subjects ---
marks = []
print("\nEnter marks for 5 subjects:")

for i in range(1, 6):
    m = float(input(f"Subject {i}: "))
    marks.append(m)

# --- Calculate average ---
avg = sum(marks) / 5

# --- Identify very good marks (>90) ---
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
print("Marks:", marks)
print("Average:", avg)
print("Very Good Marks (>90):", vg_marks if vg_marks else "None")
print("Grade:", grade)
