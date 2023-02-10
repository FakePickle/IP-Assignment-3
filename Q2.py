class Off_campus:
    def __init__(self,name,crossing,Gate_number,Time):
        self.name = name
        self.cross = crossing
        self.gate = Gate_number
        self.time = Time
    
    #function for making nested dictionaries
    def dictionary(self,day_scholar_cross):
        temp_dict = {}
        temp_dict[self.name] = {
            'Crossing': self.cross,
            'Gate Number': self.gate,
            'Time': self.time
        }
        for k,v in day_scholar_cross.items():
            temp_list = []
            if self.name == k:
                temp_list.extend(v)
                temp_list.append(temp_dict[self.name])
                day_scholar_cross[k] = temp_list

#reading data input from file and using it to make dictionaries
def creating_dictionary(dictionary):
    with open('data.txt') as infile:
        line_split = infile.read().splitlines()
        for i in range(1,len(line_split)):
            line_split[i] = line_split[i].split(', ')
        line_split.sort(key=lambda x:x[3])
        for i in range(1,len(line_split)):
            dictionary[line_split[i][0]] = []
        for  i in range(1,len(line_split)):
            comma_split = Off_campus(line_split[i][0],line_split[i][1],line_split[i][2],line_split[i][3])
            comma_split.dictionary(dictionary)

#fucntion to get the data by asking the user to input name
def finding_data_by_name(dictionary):
    user_input = input('Enter student name : ') #taking input from user for name
    user_input_time = input('Enter current time : ') #taking input from user for the current time
    temp_list = []
    temp_list_2 = []
    outline = open('output_data_q1.txt','w')
    outline.write(user_input+'\n')
    for k,v in dictionary.items():
        if k==user_input:
            for j in v:
                outline.write(str([j])+'\n') #writing everything in file
                if j['Time']<=user_input_time:
                    temp_list.append(dictionary)
                else:
                    temp_list_2.append(dictionary)
    try: #checking if the name that is taken input from user is inside the campus at that current time or not
        for k,v in temp_list[-1].items():
            for j in v:
                if j['Crossing'] == 'ENTER':
                    return user_input+' is inside the campus at '+user_input_time
                elif j['Crossing'] == 'EXIT':
                    return user_input+' is outside the campus at '+user_input_time
    except: #it will go in exception if the input time is before the first entry of that user
        try:
            for k,v in temp_list_2[0].items():
                for j in v:
                    if j['Crossing'] == 'ENTER':
                        return user_input+' is outside the campus at '+user_input_time
                    elif j['Crossing'] == 'EXIT':
                        return user_input+' is inside the campus at '+user_input_time
        except: #if there is no such name in the dictionary
            return "There is no student named "+user_input

#getting the data by taking input of start and end time
def finding_data_by_time(dictionary):
    outline = open('output_data_q2.txt','w')
    temp_list = []
    start_time = input("Enter the starting time : ") #taking input of start time
    end_time = input("Enter the ending time : ") #taking input of end time
    for k,v in dictionary.items():
        for j in v:
            if start_time <= j['Time'] <= end_time:
                temp_list.append(j)
    temp_list = sorted(temp_list, key = lambda x: x['Time'])
    outline.write('TA, Crossing, Gate number, Time\n')
    for i in temp_list:
        outline.write(i+'\n') #writing the data in the file

#function to calculate the data given by the gate number
def finding_data_by_gate(dictionary):
    gate_input = input("Enter the gate number of your choice : ") #taking user input for the desired gate number
    enter_gate = 0
    exit_gate = 0
    for v in dictionary.values():
        for j in v:
            if j['Gate Number'] == gate_input:
                if j['Crossing'] == 'ENTER':
                    enter_gate += 1
                elif j['Crossing'] == 'EXIT':
                    exit_gate += 1
    print('The Number of people entering from that gate are :',enter_gate)
    print('The Number of people exiting from that gate are :',exit_gate)

#main function where the user inputs are taken
def main(dictionary):
    print('Welcome to the Off_campus Program\n'
    '1. Getting data by inputting student name and whether he is in the campus or not\n'
    '2. Getting all the students who entered the campus during a certain that is inputted by the user\n'
    '3. Getting all the students who entered through the gate from the specific gate number\n'
    '4. Exit')
    while True:
        user_input = input('Please enter you choice : ')
        if(user_input=='1'):
            print(finding_data_by_name(dictionary))
        elif(user_input=='2'):
            finding_data_by_time(dictionary)
        elif(user_input=='3'):
            finding_data_by_gate(dictionary)
        elif(user_input=='4'):
            break
        else:
            print("Invalid Input")

#drivers code
if __name__ == '__main__':
    student_dict = {}
    creating_dictionary(student_dict)
    main(student_dict)