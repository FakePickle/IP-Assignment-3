class Course:
    def __init__(self,course_no,credits,policy,assessments):
        self.course_number = course_no
        self.assessments = assessments
        self.grade = ['A','B','C','D','F']
    
    def final_cutoff(self,grade_list):
        grade_check = [abs(grade_list[i]-grade_list[i+1]) for i in range(0,len(grade_list)-1)]
        difference = max(grade_check)
        index_difference = grade_check.index(difference)+1
        return (grade_check[index_difference] + grade_check[index_difference-1])/2
    
    def doGrade(self,student_percentile):
        for i in self.policy:
            if student_percentile > i:
                indice = self.policy.index(i)
                break
            else:
                indice = self.policy.index(i)+1
        return self.grade[indice]


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

class IP:
    def __init__(self,rollno,course_name,credit,assessments,policy,grade_list,cutoff,total_marks):
        self.rollno = rollno
        self.course_name = course_name
        self.credits = credit
        self.total_marks = total_marks
        self.assessments = assessments
        self.cutoff = cutoff
        self.policy = policy
        self.student_grade = grade_list
    
    def GetSummary(self,grading_summary):
        print('-'*50)
        print('\tCOURSE INFO')
        print('\t'+self.course_name,self.credits)
        print('\t'+self.assessments)
        print('\t'+self.cutoff)
        print('\t'+grading_summary)
        print('-'*50)
    
    def student_grade(self,outline):
        outline.write(self.rollno,self.total_marks,self.student_grade)
    
    def search(self,user)