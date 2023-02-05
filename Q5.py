def final_cutoff(policy,grade_list,index):
    grade_check = [abs(grade_list[i]-grade_list[i+1]) for i in range(0,len(grade_list)-1)]
    if grade_check == []:
        return policy[index]
    else:
        difference = max(grade_check)
        index_difference = grade_check.index(difference)+1
        return (grade_list[index_difference] + grade_list[index_difference-1])/2

def doGrade(policy,student_percentile,grade):
    for i in policy:
        if student_percentile > i:
            indice = policy.index(i)
            break
        else:
            indice = policy.index(i)+1
    return grade[indice]

def calculating_marks(assessments,marks,max_marks):
    student_percentile = 0
    for i in range(len(marks)):
        student_percentile += (assessments[i][1]*marks[i]/max_marks[i])
    return student_percentile

def GetSummary(course_name,credits,assessments,cutoff,grading_summary):
    print('-'*50)
    print('\t\tCOURSE INFO')
    print('\t\t'+course_name+' Credits : '+str(credits))
    print(str(assessments))
    print('\t  '+str(cutoff))
    print('\t'+str(grading_summary))
    print('-'*50)

def student_grade(rollno,totalmarks,student_grade_list):
    outline = open('IP_Grades.txt','w')
    for i in range(len(rollno)):
        outline.write(str(rollno[i])+' '+str(totalmarks[i])+' '+str(student_grade_list[i])+'\n')

def search(student_grade_list,student_list,user_input_rollno,markslist,totalmarks):
    for i in student_list:
        if i == user_input_rollno:
            print(user_input_rollno)
            print('Marks in assessments : '+str(markslist[student_list.index(i)]))
            print('Total Marks : '+str(totalmarks[student_list.index(i)]))
            print('Grade : '+str(student_grade_list[student_list.index(i)]))

def main():
    policy = [80,65,50,40]
    assessments = [('labs',30),('midsems',15),('assignments',30),('endsem',25)]
    credits = 4
    max_marks = [100,40,45,100]
    grade = ['A','B','C','D','F']
    course_name = 'IP'
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
            for j in range(1,len(student_marks)):
                student_marks[j] = eval(student_marks[j])
                marks += student_marks[j]
            total_marks.append(marks)
            marks_list.append(calculating_marks(assessments,student_marks[1::],max_marks))
    for i in range(len(policy)):
        temp_list = []
        for j in marks_list:
            if abs(j-policy[i]) <= 4 :
                temp_list.append(j)
        policy[i] = final_cutoff(policy,temp_list,i)
    for i in range(len(marks_list)):
        grade_list.append(doGrade(policy,marks_list[i],grade))
    grading_summary = {}
    for i in grade_list:
        count = 0
        for j in grade_list:
            if i == j:
                count += 1
        grading_summary[i] = count
    print('\tWELCOME TO AUTOMATIC GRADING SYSTEM FOR IP COURSE\n'
        '1. Get a Summary\n'
        '2. Grade the students\n'
        '3. Search based on roll number\n\n')
    while True:
        user_input = input('Enter your choice : ')
        if (len(user_input)==0):
            break
        elif user_input == '1':
            GetSummary(course_name,credits,assessments,policy,grading_summary)
        elif user_input == '2':
            student_grade(student_list,total_marks,grade_list)
        elif user_input == '3':
            user_input_rollno = input('Enter the roll number of user given : ')
            search(grade_list,student_list,user_input_rollno,marks_list,total_marks)
        else:
            print('Invalid Input!')

main()