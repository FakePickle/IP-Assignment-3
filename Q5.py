import time

#function to calculate the final cutoff
def final_cutoff(policy,grade_list,index):
    grade_check = [abs(grade_list[i]-grade_list[i+1]) for i in range(0,len(grade_list)-1)]
    if grade_check == []:
        return policy[index]
    else:
        difference = max(grade_check)
        return (grade_list[grade_check.index(difference)+1] + grade_list[grade_check.index(difference)])/2

#function to do the grading according to the new cutoffs
def doGrade(policy,student_percentile,grade):
    for i in policy:
        if student_percentile > i:
            indice = policy.index(i)
            break
        else:
            indice = policy.index(i)+1
    return grade[indice]

#calculating the percentiles of students
def calculating_marks(assessments,marks,max_marks):
    percentile_list = []
    for i in range(len(marks)): 
        student_percentile = (assessments[i][1]*int(marks[i])/max_marks[i]) 
        percentile_list.append(student_percentile)
    return sum(percentile_list),percentile_list

#getting the summary of the data as an option given to user
def GetSummary(course_name,credits,assessments,cutoff,grading_summary):
    keys = sorted(grading_summary.keys())
    grading_summary = {i: grading_summary[i] for i in keys}
    print('-'*50)
    print('\t\tCOURSE INFO')
    print('\t   Course '+course_name+'  Credits '+str(credits))
    for i in assessments:
        print(i[0]+'-'+str(+i[1]),end = ', ')
    print('\n\t\t', end='')
    for i in cutoff:
        print(i,end = ' ')
    print('\n\t    ',end='')
    for k,v in grading_summary.items():
        print(k+'-'+str(v),end = ', ')
    print()
    print('-'*50)

#function to write the grades marks and roll number in a file
def student_grade(rollno,totalmarks,student_grade_list):
    start = time.time()
    outline = open('IP_Grades.txt','w')
    count = 0
    for i in range(len(rollno)):
        outline.write(str(rollno[i])+' '+str(totalmarks[i])+' '+str(student_grade_list[i])+'\n')
        count += 1
    end = time.time()
    return 'Time = '+ str(end - start),count

#searching data based on the roll number taken input from user
def search(student_grade_list,student_list,user_input_rollno,markslist,totalmarks):
    start = time.time()
    count = 0
    for i in student_list:
        if i == user_input_rollno:
            print(user_input_rollno)
            print('Marks in assessments : '+str(markslist[student_list.index(i)][1]))
            print('Total Marks : '+str(totalmarks[student_list.index(i)]))
            print('Grade : '+str(student_grade_list[student_list.index(i)]))
            break
        count += 1
    end = time.time()
    return 'Time = '+ str(end - start),count


def main():
    policy = [80,65,50,40]
    assessments = [('labs',30),('midsems',15),('assignments',30),('endsem',25)]
    max_marks = [30,15,30,25]
    course_name = input("Enter the coruse name : ")  # taking input for course name
    credits = int(input("Enter the number of credits for that course : ")) # taking input for credits
    grade = ['A','B','C','D','F']
    total_marks = [] #total marks list
    marks_list = [] # percentile list
    student_list = [] #student roll number list
    with open('IP_Marks.txt') as inline:
        inline = inline.read().splitlines()
        for i in inline:
            marks = 0
            student_marks = i.split(', ')
            student_list.append(student_marks[0])  #appending roll numbers
            for j in range(1,len(student_marks)): marks += eval(student_marks[j])
            total_marks.append(marks) # appending total marks
            marks_list.append(calculating_marks(assessments,student_marks[1::],max_marks)) #appending total percentile and percentile per assessment
    #updating the policy
    for i in range(len(policy)):
        temp_list = [j[0] for j in marks_list if abs(j[0] - policy[i])<=2]
        temp_list.sort(reverse=True)
        policy[i] = final_cutoff(policy,temp_list,i)
    grade_list = [doGrade(policy,i[0],grade) for i in marks_list] #grading students based on updated policy
    grading_summary = {}
    for i in grade_list:
        count = 0
        for j in grade_list:
            if i == j:
                count += 1
        grading_summary[i] = count #getting the count of each and every grade
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
            writing_data_in_file_time,writing_count = student_grade(student_list,total_marks,grade_list)
        elif user_input == '3':
            user_input_rollno = input('Enter the roll number of user given : ')
            search_time,search_count = search(grade_list,student_list,user_input_rollno,marks_list,total_marks)
        else:
            print('Invalid Input!')
    return writing_data_in_file_time,writing_count,search_time,search_count

write_q5_time,write_q5_count,search_q5_time,search_q5_count = main()