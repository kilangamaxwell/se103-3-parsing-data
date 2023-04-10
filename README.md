# se103-3-parsing-data

Parsing Classroom Data
You were called to help your instructors, again!
What should I do?
In the file classroom_simple.txt there is valuable information about students in the classroom.
Each student is described with the following format in the file:
###
name (str)
country (str)
grade1 (int)
grade2 (int)
grade3 (int)
Each student has exactly 3 grades. A blank line separates two records of students.
An example of records of two students:
###
Ron
Germany
100
90
81

###
Jonathan
United States
85
45
66
Blank Line
As you already know, each line in a text file ends with a newline character, \n. A blank line is a line which contains nothing but \n. From the example above:
...100\n90\n81\n\n###\nJonathan\nUnited States...
Hence, a blank line can be identified in this file as two consecutive characters of newline: \n\n. The first one is the ending of the previous line, and the second one is the blank line containing nothing but \n.
You task is to parse the files and to create a data structure that is more easy to work with in Python. In this case, we describe each student with a dictionary, and we store all the students in a list.

#######################################################################################################################################################################
Step 1 - Simple Classroom
In this step, you’ll implement the function parse_simple_classroom(file_path) which takes the path of a simple classroom file, as shown in the previous page, and parse it.
The file path is classroom_simple.txt, the same file we showd in the previous page.
Specification
The function should return a list of dictionaries, each dictionary in the format:
{
  'name': 'Ron',
  'country': 'Germany',
  'grades': [100, 90, 81]
}
So the complete list of students should be:
[
  {
    'name': 'Ron',
    'country': 'Germany',
    'grades': [100, 90, 81]
  },
  {
    'name': 'Stephanie',
    'country': 'Portugal',
    'grades': [89, 92, 98]
  },
  ...
]
#######################################################################################################################################################################
Don’t change the file
Please do not change the file, since the automatic tests (explained below) rely that the content of the file stay the same.
If you want to make changes to the file, you can copy it, change it and then restore it later.
#######################################################################################################################################################################
💡 Hint
There are some different ways to solve it:
You can parse the file line-by-line and handle it.
You can read the entire text file as a string, and then perform string manipulation on the entire text, with functions that you already know.
Both ways are fine, choose the right one for you. It’s OK if you still don’t know how to approach it, the best way would be to just try! Play with the file.
#######################################################################################################################################################################
Notes & Assumptions
Return value from your function
Note that your function must return the above list. Do not print it inside the function.
However, it’s fine and even recommended to print it outside of the function, like this:
students = parse_simple_classroom(file_path)
print(students)
It can help you to test your code.
No newline at the end of file
You can assume there is no newline at the end of file, i.e., the file ends with the last grade of the last students.
At least one student
You can assume there is at least one student in the file.
Exactly 3 grades
You can assume each student has exactly three grades.
Newline between students
Assume there is always exactly one newline between two records of students.
Testing Your Code
We provide tests for you so you can test that your code works properly and correctly styled.
#######################################################################################################################################################################
Functionality Tests
There is only one test and it checks that the return value from your function is the same as expected.

#######################################################################################################################################################################
Step 2 - Student's Average
In this step, you’ll write a function that gets a name of a student and calculates their grades average.
Specification
Write a function called student_avg(students_list, student_name) that gets two parameters:
students_list - the list of students (each student is a dictionary) that your function returned from the previous step.
student_name - a string representing a name of one student.
Your function should return the average of grades of the student. In case student_name doesn’t exist in student_list, the function should return None.
Main function
In addition, create a main function that gets student name from the user input, and then prints the average of grades.
In case the user doesn’t exist in the file, the function prints a nice message and exists.
Skeleton example
Here is a code skeleton to help you understand how the program should be structured. It’s not the complete code, it’s just for you to get the sense of the solution:
###

def main():
  student_name = input(...)
  students_list = parse_simple_classroom(...)
  avg = student_avg(students_list, student_name)
  if avg is None:
    ...
  else:
    ...

###
Testing Your Code
We provide tests for you so you can test that your code works properly and correctly styled.

Functionality Tests
There are no functionality tests for this step. You should check your code with different cases.

Pass the tests
Make sure you pass the tests before moving on to the next step.
If you didn’t pass the tests, fix the errors and try it again.

Bonus - Complex Classroom
Bonus Step
This is a bonus step, you can skip it if you want.
################################################################################################################################################################
Specification
In this step, we will not assume anymore there are only 3 grades for a student, and we will not assume there is exactly one newline between each student.
Examine the file classroom_complex.txt (in the file tree on the left), where there is an arbitrary number of newlines (sometimes even no newline at all) between each student.
In addition, each student have a different number of grades, but you can assume it’s at least one.
Create a new function called parse_complex_classroom(file_path) that takes a file path of a complex classroom, and returns the same structure as before, with all the available grades.
################################################################################################################################################################
Testing Your Code
We provide tests for you so you can test that your code works properly and correctly styled.
Functionality Tests
There are no functionality tests for this step. You should check your code with different cases.
