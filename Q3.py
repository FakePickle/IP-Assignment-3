import random #random to get the random 5 words

#using class to evaluate the score
class Evaluate:
    def __init__(self,factor1,factor2,factor3,factor4,factor5):
        self.F1 = factor1
        self.F2 = factor2
        self.F3 = factor3
        self.F4 = factor4
        self.F5 = factor5
    
    #function where the final score is calculated
    def calculate(self):
        score = 4 + self.F1 * 6 + self.F2 * 6 - self.F3 - self.F4 - self.F5
        return score

#class to calculate the factors
class Calculating_Factors:
    def __init__(self,assignment):
        self.assnmt = assignment

    # factor one calculation
    def factor1(self):
        unique_words = [i for i in self.assnmt.split(' ') if i.strip(',.;: ') not in unique_words] #getting all the unique words
        total_words = 0
        for i in self.assnmt.split(' '): total_words += 1 #total words
        return len(unique_words)/total_words #returning the value

    #factor two calculation
    def factor2(self):
        d={}
        #assigning the words to their number of occurences
        for i in self.assnmt.split(' '):
            j = i.strip(',.;:()/- ')
            if j.isalpha():
                if j == '':
                    pass
                elif j.lower() not in d:
                    d[j.lower()] = 1
                else:
                    d[j.lower()] += 1
        new_d = {}
        sorted_values = sorted(d.values(),reverse=True)
        for i in sorted_values:
            for k in d.keys():
                if d[k] == i:
                    new_d[k] = d[k]
        top_occur = 0
        sorted_dict = {}
        keys,values = list(new_d.keys()),list(new_d.values())
        if len(d) >= 5:
            for i in range(5):
                sorted_dict[keys[i]] = values[i]
                top_occur += values[i]
        else:
            for k,v in d.items():
                sorted_dict[k] = v
                top_occur += v
        return top_occur/len(self.assnmt.split(' ')),sorted_dict,d

    #calculating factor 3
    def factor3(self):
        sentences = self.assnmt.split('. ')
        total_count_sentences = 0
        for i in sentences:
            if len(i.split()) > 35 or len(i.split()) < 5:
                total_count_sentences += 1
        print(total_count_sentences,len(sentences))
        return total_count_sentences/len(sentences)

    #calculating factor 4
    def factor4(self):
        frequency = 0
        total_words = 0
        for i in self.assnmt.split(' '):
            #getting the count of fullstops,comma,colon,semi-colon in each and every word
            full_stops = 0
            comma = 0
            colon = 0
            semi_colon = 0
            for j in i:
                if j.isalpha():
                    pass
                elif j == '.':
                    full_stops += 1
                elif j == ',':
                    comma += 1
                elif j == ':':
                    colon += 1
                elif j == ';':
                    semi_colon += 1
            #frequency increases by one if any of them are more than one
            if full_stops > 1 or comma > 1 or colon > 1 or semi_colon > 1:
                frequency += 1
            total_words += 1
        return frequency/total_words

    #calculating factor 5
    def factor5(self):
        if len(self.assnmt) > 750:
            return 1
        else:
            return 0

    #calculating the factors and opening the file
def calc(filename):
    with open(filename) as inline:
        assignment = ''
        inline = inline.read()
        for i in inline:
            #making new line as a space
            if i == '\n':
                assignment += ' '
            else:
                assignment += i
    calculate = Calculating_Factors(assignment)
    factor1 = calculate.factor1()
    factor2,sorted_dictionary,dictionary = calculate.factor2()
    factor3 = calculate.factor3()
    factor4 = calculate.factor4()
    factor5 = calculate.factor5()
    return factor1,factor2,factor3,factor4,factor5,sorted_dictionary,dictionary

#main function
def main():
    user_input_file_number = int(input('Enter the number of files you want to calculate assessment for : ')) #taking input from user to input the number of files
    with open('scores.txt','w') as outline:
        for i in range(user_input_file_number):
            filename = input('Enter the name of the file : ')
            factor1,factor2,factor3,factor4,factor5,sorted_dictionary,dictionary = calc(filename)
            print(calc(filename))
            outline.write(filename+'\n')
            outline.write('Score '+str(Evaluate(factor1, factor2, factor3, factor4, factor5).calculate())+'\n')
            sort = ''
            for i in sorted_dictionary.keys():
                sort += i + ' '
            outline.write(sort+'\n')
            shuffle = [i for i in dictionary.keys()]
            outline.write(str(random.choices(shuffle,k = 5))+'\n\n')

#calling the function
main()