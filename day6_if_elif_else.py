#  Function to convert numeric score to letter grade
def calculate_grade(score):
    if score > 100 or score < 0:
        return "invalid score"
    else:    
        if score >= 90:
           return "A"
        elif score >= 85:
           return "A-"
        elif score >= 80:
           return "B+"
        elif score >= 75:
           return "B"
        elif score >= 70:
           return "B-"
        elif score >= 65:
           return "C+"
        elif score >= 60:
           return "C"
        elif score >= 50:
            return "D"
        else:
            return "F"

# Function to print grade summary
def print_grade_summary(name, score):
    grade = calculate_grade(score)
    if grade == "Invalid Score":
        print(f" Error: {name} entered an invalid score ({score}). Must be between 0 and 100.")
    else:
        print(f" Student {name} scored {score} = Grade: {grade}")

# dummy data
students = [
    {"name": "Zara", "score": 87.5},
    {"name": "Ali", "score": 73},
    {"name": "Fatima", "score": 101}, 
    {"name": "Ahmed", "score": 58.2}
]

for student in students:
    print_grade_summary(name=student["name"], score=student["score"])
