# Function to calculate GPA based on list of grades
def calculate_gpa(grades, total_credit_hours=15):
    
    if not grades:
        return 0.0
    
    total_points = sum(grades)
    gpa = total_points / len(grades)
    return round(gpa, 2)

# Demonstration of function call with named argument
grades_list = [3.7, 3.3, 2.7, 4.0, 3.0]  # Sample grade points
 
#a=int(input("enter total credit hours"))
# Using named arguments to call function
student_gpa = calculate_gpa(grades=grades_list, total_credit_hours=15)

# Display result
print(f" The calculated GPA is: {student_gpa}")
