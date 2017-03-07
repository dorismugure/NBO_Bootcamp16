class Course:
   def __init__(self,course_code, description, credits, department):
       self.course_code = course_code
       self.description = description
       self.credits = credits
       self.department = department
       self.department.add_course(self)
       self.runnings = []

   def add_running(self, yearly):
       self.runnings.append(CourseRunning(self, yearly))
       return self.runnings[-1]

class CourseRunning:
    def __init__(self, course, yearly):
       self.course = course
       self.yearly = yearly
       self.students = []

    def add_student(self, student):
      self.students.append(student)
