''' create a function that takes a dictionary of student names and returns a list of student names
    in alphabetical order '''


def get_student_names(students):
    new_lst = []
    new_lst = students.values()
    return sorted(new_lst)

print(get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}))