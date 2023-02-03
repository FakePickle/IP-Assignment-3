class Evaluate:
    def __init__(self,factor1,factor2,factor3,factor4,factor5):
        self.F1 = factor1
        self.F2 = factor2
        self.F3 = factor3
        self.F4 = factor4
        self.F5 = factor5
    
    def calculate(self):
        score = 4 + self.F1 * 6 + self.F2 * 6 - self.F3 - self.F4 - self.F5
        return score

class Calculating_Factors:
    def __init__(self,assignment):
        self.assnmt = assignment
    
    def factor1(self):
        unique_words = 0
        total_words = 0
        for i in self.assnmt.split(' '):
            counter = 0
            for j in self.assnmt.split(' '):
                if i == j:
                    counter += 1
            if counter > 1:
                unique_words += 1
            total_words += 1
        return unique_words/total_words
    
    def factor2(self):
        top_occur = []
        total_words = 0
        for i in self.assnmt.split(' '):
            counter = 0
            for j in self.assnmt.split(' '):
                if j == i:
                    counter += 1
            total_words += 1
            top_occur.append(counter)
        sorted_top_occur = sorted(top_occur,reverse=True)
        sum_top_occur = 0
        for i in range(5):
            sum_top_occur += sorted_top_occur[i]
        return sum_top_occur/total_words

    def factor3(self):
        sentences = self.assnmt.split('. ')
        total_count_sentences = 0
        for i in sentences:
            if len(i) > 35 or len(i) < 5:
                total_count_sentences += 1
        return total_count_sentences/len(sentences)
    
    def factor4(self):
        frequency = 0
        total_words = 0
        for i in self.assnmt.split(' '):
            full_stops = 0
            comma = 0
            colon = 0
            semi_colon = 0
            for j in i:
                if j == '.':
                    full_stops += 1
                elif j == ',':
                    comma += 1
                elif j == ':':
                    colon += 1
                elif j == ';':
                    semi_colon += 1
            if full_stops > 1 or comma > 1 or colon > 1 or semi_colon > 1:
                frequency += 1
            total_words += 1
        return frequency/total_words

    def factor5(self):
        if len(self.assnmt) > 750:
            return 1
        else:
            return 0

def main():
    