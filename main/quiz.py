import datetime
import random

from questions import Add, Multiply, Subtract

class Quiz:
    questions = []
    answers = []

    def __init__(self):
        # generate 10 random question with numbers from 1 to 10
        # add these questions to self.questions
        question_types = (Add, Multiply, Subtract)
        for _ in range(10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            question = random.choice(question_types)(num1,num2)
            self.questions.append(question)

    def take_quiz(self):
        # log the start time
        # ask all of the questions
        # log correct answers
        # log end time
        # show summary
        pass
    def ask(self,questions):
        # log start time
        # capture answer
        # check answer
        # log end time
        # if answer is correct send back True
        # else False
        # send back elapsed time
        pass
    def total_correct(self):
        # return the total number of correct answers
        total = 0 
        for answer in self.answers:
            if answer[0]:
                total +=1
        return total
        
    def summary(self):
        # print how many correct out of total eg 5/10
        # print total time

        print(f'You got {self.total_correct}/{len(self.questions)}')
        print(f'Completion time: {(self.endtime - self.starttime).seconds}')