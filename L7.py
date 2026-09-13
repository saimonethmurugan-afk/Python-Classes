"""
1) Add the project title.
   a) Use a comment to label the program as "School Class Organiser".


2) Create a list of classmates.
   a) Store student names inside a list.
   b) Print the full class list.

3) Access list values.
   a) Use `len()` to find the total number of students.
   b) Use index `0` to print the first student.
   c) Use index `-1` to print the last student.
   d) Use slicing to print the first three students.

4) Modify the list.
   a) Use `append()` to add a new student.
   b) Use `remove()` to delete a student.
   c) Use `sort()` to arrange names alphabetically.
   d) Use `reverse()` to reverse the list order.

5) Create a teacher dictionary.
   a) Store teacher details using key-value pairs.
   b) Add name, subject, and experience.

6) Perform dictionary operations.
   a) Access the subject using its key.
   b) Use `get()` to safely access experience.
   c) Update the experience value.
   d) Add an email key.
   e) Use `pop()` to remove experience.

7) Create a student directory.
   a) Create one list for roll numbers.
   b) Create one list for student names.
   c) Use `zip()` to pair roll numbers with names.
   d) Convert the pairs into a dictionary using `dict()`.

8) Access a student from the directory.
   a) Use the roll number key to print the student name.
"""
#School Class Organiser

#Creating List

students = ["Josh", "Arjun", "Aryan", "Luca","Surya"]
print("Student Names: ",students)

#Accessing Values from List

print("Total No. Students: ",len(students))
print("First Student: ",students[0])
print("Last Student: ",students[1])
print("First Three Students: ",students[:3])

#Modifying the List

students.append("Sai")
print("Updated List: ",students)

students.remove("Aryan")
print("After Removing: ",students)
students.sort()
print("Alphabetically sorted list: ",students)
students.reverse()
print("Reversed Order: ",students)

#  Create a staff dictionary

staff = {"name": "Mr.Samuel","subject":"Maths","experience":7.5/10}
print("Teacher Profile: ",staff)

# Dictionary operations
print("Subject:", staff["subject"])
print("Experience:", staff.get("experience", "N/A"))
staff["experience"] = 8
staff["email"] = "samuel@school.com"
staff.pop("experience")
print("Updated teacher profile:", staff)

# Convert lists to a student directory
roll_numbers = [1, 2, 3, 4, 5]
students = ["Josh", "Arjun", "Aryan", "Luca","Surya"]
student_directory = dict(zip(roll_numbers, students))
print("\nStudent Directory:", student_directory)
print("Student at Roll 3:", student_directory[4])
