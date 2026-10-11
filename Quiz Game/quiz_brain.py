class QuizBrain():
    def __init__(self,qList):
        self.question_number=0
        self.question_list=qList
        self.score=0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    def check_answer(self,userAnswer,corrAnswer):
        if userAnswer==corrAnswer:
            print("Correct! ")
            self.score+=1
        else:
            print(f"Wrong \n The correct answer was {corrAnswer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        userAnswer=input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(userAnswer,current_question.answer)
