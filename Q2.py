class Off_campus:
    def __init__(self,name,crossing,Gate_number,Time):
        self.name = name
        self.cross = crossing
        self.gate = Gate_number
        self.time = Time
    
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

def creating_dictionary(dictionary,data_list):
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

def finding_data_by_name(dictionary):
    user_input = input('Enter student name : ')
    user_input_time = input('Enter current time : ')
    temp_list = []
    temp_list_2 = []
    outline = open('output_data_q1.txt','w')
    outline.write(user_input+'\n')
    for k,v in dictionary.items():
        if k==user_input:
            for j in v:
                outline.write(str([j])+'\n')
                if j['Time']<=user_input_time:
                    temp_list.append(dictionary)
                else:
                    temp_list_2.append(dictionary)
    try:
        for k,v in temp_list[-1].items():
            for j in v:
                if j['Crossing'] == 'ENTER':
                    return user_input+' is inside the campus at '+user_input_time
                elif j['Crossing'] == 'EXIT':
                    return user_input+' is outside the campus at '+user_input_time
    except:
        try:
            for k,v in temp_list_2[0].items():
                for j in v:
                    if j['Crossing'] == 'ENTER':
                        return user_input+' is outside the campus at '+user_input_time
                    elif j['Crossing'] == 'EXIT':
                        return user_input+' is inside the campus at '+user_input_time
        except:    
            print("There is no student named "+user_input)

def finding_data_by_time(dictionary):
    outline = open('output_data_q2.txt','w')
    temp_list = []
    start_time = input("Enter the starting time : ")
    end_time = input("Enter the ending time : ")
    for k,v in dictionary.items():
        for j in v:
            if start_time <= j['Time'] <= end_time:
                temp_list.append(k)
                temp_list.append(j['Crossing'])
                temp_list.append(j['Gate Number'])
                temp_list.append(j['Time'])
    outline.write('TA, Crossing, Gate number, Time\n')
    for i in range(0,len(temp_list),4):
        outline.write(temp_list[i]+', '+temp_list[i+1]+', '+temp_list[i+2]+', '+temp_list[i+3]+'\n')

def finding_data_by_gate(dictionary):
    gate_input = input("Enter the gate number of your choice : ")
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

if __name__ == '__main__':
    temp_dict = {}
    Data = []
    creating_dictionary(temp_dict,Data)
    main(temp_dict)