# Day 4: Student Record System using Tuples and Sets

#  Step 1: Store student IDs as an immutable tuple
student_ids = ("S101", "S102", "S103", "S104")
print("Student IDs: ", student_ids)

#  Step 2: Create a set of unique course names
courses = {"Python", "AI", "ML"}
print("Initial Courses:", courses)

#  Step 3: Add a new course to the set
courses.add("Data Science")
print("Courses after adding 'Data Science':", courses)

#  Step 4: Remove a course (if it exists)
courses.remove("ML")
print("Courses after removing 'ML':", courses)

#  Step 5: Print all available courses one by one
print("Current course list:")
print(courses)

# Note: Sets do not allow duplicate values and are unordered
