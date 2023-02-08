import time

class Course:
    def __init__(self,policy):
        self.policy = policy
        self.grade = ['A','B','C','D','F']
    
    def final_cutoff(self,grade_list,index):
        grade_check = [round(abs(grade_list[i]-grade_list[i+1]),2) for i in range(0,len(grade_list)-1)]
        if grade_check == []:
            return self.policy[index]
        else:
            difference = max(grade_check)
            return round((grade_list[grade_check.index(difference)+1] + grade_list[grade_check.index(difference)]),2)/2

    def doGrade(self,student_percentile):
        for i in self.policy:
            if student_percentile > i:
                indice = self.policy.index(i)
                break
            else:
                indice = self.policy.index(i)+1
        return self.grade[indice]

class student:
    def __init__(self,rollno,marks_list,max_marks_list,assessments):
        self.roll_no = rollno
        self.marks = marks_list
        self.assessments = assessments
        self.max_marks = max_marks_list
    
    def calculating_marks(self):
        student_percentile = 0
        for i in range(len(self.marks)):
            student_percentile += (self.assessments[i][1]*int(self.marks[i])/self.max_marks[i])
        return student_percentile

class IP:
    def __init__(self,student_list,assessments,grade_list,cutoff):
        self.student_list = student_list
        self.course_name = input('Enter course name : ')
        self.credits = int(input('Enter the credits for that course : '))
        self.assessments = assessments
        self.cutoff = cutoff
        self.student_grade_list = grade_list
    
    def GetSummary(self,grading_summary):
        keys = sorted(grading_summary.keys())
        grading_summary = {i: grading_summary[i] for i in keys}
        print('-'*50)
        print('\t\tCOURSE INFO')
        print('\t   Course '+self.course_name+'  Credits '+str(self.credits))
        for i in self.assessments:
            print(i[0]+'-'+str(+i[1]),end = ', ')
        print('\n\t\t', end='')
        for i in self.cutoff:
            print(i,end = ' ')
        print('\n\t',end='')
        for k,v in grading_summary.items():
            print(k+'-'+str(v),end = ', ')
        print()
        print('-'*50)
    
    def student_grade(self,rollno,totalmarks):
        start = time.time()
        outline = open('IP_Grades.txt','w')
        for i in range(len(rollno)):
            outline.write(str(rollno[i])+', '+str(totalmarks[i])+', '+str(self.student_grade_list[i])+'\n')
        end = time.time()
        return 'Time = '+ str(end - start)

    def search(self,user_input_rollno,markslist,totalmarks):
        start = time.time()
        flag = True
        for i in self.student_list:
            if i == user_input_rollno:
                print(user_input_rollno)
                print('Marks in assessments : '+str(markslist[self.student_list.index(i)]))
                print('Total Marks : '+str(totalmarks[self.student_list.index(i)]))
                print('Grade : '+str(self.student_grade_list[self.student_list.index(i)]))
                flag = True
                break
            else:
                flag = False
        if flag:
            pass
        else:
            print('Student is not in the databse')
        end = time.time()
        return 'Time = '+ str(end - start)

def main():
    policy = [80,65,50,40]
    assessments = [('labs',30),('midsems',15),('assignments',30),('endsem',25)]
    max_marks = [100,100,100,100]
    total_marks = []
    marks_list = []
    grade_list = []
    student_list = []
    with open('IP_Marks.txt') as inline:
        inline = inline.read().splitlines()
        for i in inline:
            marks = 0
            student_marks = i.split(', ')
            student_list.append(student_marks[0])
            for j in range(1,len(student_marks)): marks += eval(student_marks[j])
            total_marks.append(marks)
            Student = student(student_marks[0],student_marks[1::],max_marks,assessments)
            marks_list.append(Student.calculating_marks())
    for i in range(len(policy)):
        temp_list = [j for j in marks_list if abs(j - policy[i])<=2]
        temp_list.sort(reverse=True)
        policy[i] = Course(policy).final_cutoff(temp_list,i)
    course = Course(policy)
    grade_list = [course.doGrade(i) for i in marks_list]
    grading_summary = {}
    for i in grade_list:
        count = 0
        for j in grade_list:
            if i == j:
                count += 1
        grading_summary[i] = count
    IP_Course = IP(student_list,assessments,grade_list,policy)
    print('\tWELCOME TO AUTOMATIC GRADING SYSTEM FOR IP COURSE\n'
        '1. Get a Summary\n'
        '2. Grade the students\n'
        '3. Search based on roll number\n\n')
    while True:
        user_input = input('Enter your choice : ')
        if (len(user_input)==0):
            break
        elif user_input == '1':
            IP_Course.GetSummary(grading_summary)
        elif user_input == '2':
            writing_into_file_time = IP_Course.student_grade(student_list,total_marks)
        elif user_input == '3':
            user_input_rollno = input('Enter the roll number of user given : ')
            search_input_time = IP_Course.search(user_input_rollno,marks_list,total_marks)
        else:
            print('Invalid Input!')
    return writing_into_file_time,search_input_time

write_q4_time,search_q4_time = main()