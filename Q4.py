class Course:
    def __init__(self,course_no,credits,policy,assessments):
        self.course_number = course_no
        self.policy = policy
        self.assessments = assessments
    
    def final_cutoff(self,grade_list):
        grade_check = [max([abs(j-i) for j in grade_list]) for i in grade_list]
        difference = max(grade_check)
        indices = [i for i in range(len(grade_check)) if grade_check[i] == difference]
        for i in range(len(indices)):
            indices[i] = grade_list[indices[i]]
        return sum(indices)/len(indices)
    
    def Upload_marks(self,filename):
        with open(filename) as inline:
            inline = inline.read().splitlines()

class student:
    def __init__(self,name,rollno,marks_list,max_marks_list,assessments):
        self.name = name
        self.roll_no = rollno
        self.marks = marks_list
        self.assessments = assessments
        self.max_marks = max_marks_list
    
    def calculating_marks(self):
        student_percentile = 0
        for i in self.marks:
            for j in range(len(i)):
                student_percentile += (self.assessments[j][1]*i/self.max_marks[j])
        return student_percentile
    
    