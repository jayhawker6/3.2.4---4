from course import Course
from student import Student

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")
computer_science = Course("Computer Science I")
nerd = Course("Becoming An Introvert I")

test_student1 = Student("Jill", "Sample")
test_student1.add_course(math)
test_student1.add_course(language)
test_student1.add_course(science)
test_student1.add_course(history)

test_student2 = Student("Bill", "Sample")
test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)

test_student3 = Student("Ligma", "Sample")
test_student3.add_course(nerd)
test_student3.add_course(science)
test_student3.add_course(computer_science)
test_student3.add_course(history)



# TODO print student_list
print(Student.student)
# TODO iterate over each of the students in the list and print their names and course schedules.
    # Each iteration should:
        # print the student
"""
 for this part you may need to review the other skeleton code to:
    - see how to get items from a list
    - see if there is code (like a function) in that file you can call in this file
    - verify that running this file gets you the correct output with information from that file
  Also, review syntax of pulling items from a list from other activities 
"""