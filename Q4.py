class Course:
    def __init__(self,course_no,policy,assessments):
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
    
    