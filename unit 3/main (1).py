class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(students):
    """
    Sort the list of student objects based on CGPA in descending order.
    
    Args:
    students (list): List of student objects.
    
    Returns:
    list: Sorted list of student objects based on CGPA in descending order.
    """
    sorted_students = sorted(students, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage:
# Create student objects
students = [Student("Alice", "001", 3.8),
            Student("Bob", "002", 3.9),
            Student("Charlie", "003", 3.7),
            Student("David", "004", 4.0)]

# Sort the students based on CGPA
sorted_students = sort_students(students)

# Print sorted student list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
