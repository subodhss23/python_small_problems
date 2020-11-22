''' Create a function that takes alist of student dictionaries and return a list of
    their top notes. If the student does not have notes then let's assume their top
    note is equal to 0.'''

def get_student_top_notes(students):
	
	top_notes = []
	
	for student in students:
		try:
			top_notes.append(max(student['notes']))
		except ValueError:
			top_notes.append(0)
	
	return top_notes


print(get_student_top_notes([
  {
    "id": 1,
    "name": "Jacek",
    "notes": [5, 3, 4, 2, 5, 5]
  },
  {
    "id": 2,
    "name": "Ewa",
    "notes": [2, 3, 3, 3, 2, 5]
  },
  {
    "id": 3,
    "name": "Zygmunt",
    "notes": [2, 2, 4, 4, 3, 3]
  }
]))