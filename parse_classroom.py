COMPLEX_CLASSROOM_PATH = "classroom_complex.txt"
SIMPLE_CLASSROOM_PATH = "classroom_simple.txt"


def parse_simple_classroom(file_path):
  """ Parse classroom file that is given in `file_path` parameter.
   Returns a list of dictionaries describing the students in the
    classroom, each student is describe with the dictionary: {
        'name': ...,  'country': ...,  'grades': [...]}"""
  students = []
  student_info = []
  grades = []
  with open(file_path, "r") as file:
    data = file.read().split()
  for item in data:
    if item != "###" and not item.isdigit():
      student_info.append(item)
    if item.isdigit():
      grades.append(int(item))
    if len(grades) == 3:
      student = {}
      student['name'] = student_info[0]
      if len(student_info) > 2:
        student['country'] = student_info[1] + " " + student_info[2]
      else:
        student['country'] = student_info[1]
      student['grades'] = grades
      students.append(student)
      student_info = []
      grades = []
  return students


def parse_complex_classroom(file_path):
  """ Parse complex classroom file that is given in `file_path`
   parameter. Returns a list of dictionaries describing the
    students in the classroom, each student is describe with the
     dictionary: {  'name': ...,  'country': ...,  'grades': [...]
     }"""
  students = []
  student_info = []
  grades = []
  with open(file_path, "r") as file:
    data = file.read().split()
    for i, item in enumerate(data):
        if item != "###" and not item.isdigit():
            student_info.append(item)
        if item.isdigit():
            grades.append(int(item))
        if item == "###" and len(grades) > 0:
            student = {}
            student['name'] = student_info[0]
            if len(student_info) > 2:
              student['country'] = student_info[1] + " " + student_info[2]
            else:
                student['country'] = student_info[1]
            student['grades'] = grades
            students.append(student)
            student_info = []
            grades = []
        if i == len(data) - 1 and len(grades) > 0:
            student = {}
            student['name'] = student_info[0]
            if len(student_info) > 2:
                student['country'] = student_info[1] + " " + student_info[2]
            else:
                student['country'] = student_info[1]
            student['grades'] = grades
            students.append(student)
  return students


def student_avg(students_list, student_name):
  """Searches for student's name in students list and calculates
   the student's average."""
  student_names = []
  avg = 0
  for student_record in students_list:
    student_names.append(student_record['name'])
    if student_record['name'] == student_name:
      grades = student_record['grades']
      total = 0
      for grade in grades:
        total += grade
      avg = total / len(grades)
  if student_name not in student_names:
    return None
  return avg


def main():
  """Requests for student's name, generates a list of dictionaries
   containing student information and returns the student's average."""
  student_name = input("Enter the student's name: ")
  students_list = parse_simple_classroom(SIMPLE_CLASSROOM_PATH)
  avg = student_avg(students_list, student_name)
  if avg is None:
    print("Sorry. The student does not exist in the system.")
  else:
    print(f"Average: {avg}")
  print(parse_complex_classroom(COMPLEX_CLASSROOM_PATH))


if __name__ == "__main__":
  main()
