def main():
    print('Welcome to the Off_campus Program\n'
    '1. Getting data by inputting student name and whether he is in the campus or not\n'
    '2. Getting all the students who entered the campus during a certain that is inputted by the user\n'
    '3. Getting all the students who entered through the gate from the specific gate number\n'
    '4. Exit')
    temp_dict = {}
    Data = []
    creating_dictionary(temp_dict,Data)
    while True:
        user_input = int(input('Please enter you choice : '))
        if(user_input==1):
            finding_data_by_name(Data)
        elif(user_input==2):
            finding_data_by_time(Data)
        elif(user_input==3):
            finding_data_by_gate(Data)
        elif(user_input==4):
            break
        else:
            print("Invalid Input")

class Off_campus:
    def __init__(self,name,crossing,Gate_number,Time):
        self.name = name
        self.cross = crossing
        self.gate = Gate_number
        self.time = Time
    
    def dictionary(self,day_scholar_cross):
        temp_dict = {}
        temp_dict[self.name] = [{
            'Crossing': self.cross,
            'Gate Number': self.gate,
            'Time': self.time
        }]
        if day_scholar_cross == {}:
            day_scholar_cross = temp_dict
        else:
            for k,v in day_scholar_cross.items():
                temp_list = []
                if self.name == k:
                    temp_list.extend(v)
                    temp_list.extend(temp_dict[self.name])
                    day_scholar_cross[self.name] = temp_list
                else:
                    day_scholar_cross = temp_dict
        return day_scholar_cross

def creating_dictionary(dictionary,data_list):
    with open('data.txt') as infile:
        line_split = infile.read().splitlines()
        for i in range(1,len(line_split)):
            line_split[i] = line_split[i].split(', ')
            comma_split = Off_campus(line_split[i][0],line_split[i][1],line_split[i][2],line_split[i][3])
            temp_list = [comma_split.dictionary(dictionary)]
            data_list.extend(temp_list)

def finding_data_by_name(data_list):
    user_input = input()
    temp_list = []
    for i in data_list:
        for k,v in i.items():
            if k==user_input:
                for j in v:
                    if j['Time']>='06:00:00' and j['Time']<='19:00:00':
                        temp_list.append(i)
                        print(i)
    try:
        for k,v in temp_list[-1].items():
            for j in v:
                if j['Crossing'] == 'ENTER':
                    print(user_input+' is inside the campus')
                else:
                    print(user_input+' is outside the campus')
    except:
        print("There is no student named "+user_input)

def finding_data_by_time(data_list):
    start_time = input("Enter the starting time : ")
    end_time = input("Enter the ending time : ")


def finding_data_by_gate(data_list):
    a = 1

main()