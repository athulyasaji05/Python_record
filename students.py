def get_student_details():
    students = []
    n = int(input("Enter the number of students: "))

    for i in range(1, n + 1):
        print(f"Enter details for student {i}:")
        name = input("Name: ")
        roll_no = input("Roll No.: ")
        total_mark = float(input("Total Marks: "))
        student = {'name': name, 'roll_no': roll_no, 'total_mark': total_mark}
        students.append(student)

    return students

def find_student_with_highest_mark(students):
    if not students:
        return None

    highest_student = max(students, key=lambda x: x['total_mark'])
    return highest_student

def main():
    students = get_student_details()
    highest_student = find_student_with_highest_mark(students)

    if highest_student:
        print("\nDetails of the student with the highest total marks:")
        print(f"Name: {highest_student['name']}")
        print(f"Roll No.: {highest_student['roll_no']}")
        print(f"Total Marks: {highest_student['total_mark']}")
    else:
        print("No students found.")

if __name__ == "__main__":
    main()
