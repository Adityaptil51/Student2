import sys

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

marks = []
print("\nEnter marks for 5 subjects:")

for i in range(1, 6):
    m = float(input(f"Subject {i}: "))
    marks.append(m)

avg = sum(marks) / 5

