class QuizBrain:
    def __init__(self,question_list):
        self.question=question_list
        self.question_number=0
        self.score=0
    def next_question(self):
        current_question=self.question[self.question_number]
        self.question_number+=1
        user_answer=input(f"{self.question_number},{current_question.question} True/False")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self,user_answer,correct_answer):
        if(user_answer==correct_answer):
            print("You got it right")
            self.score+=1
        else:
            print(f"The correct answer is {correct_answer} and your current score is {self.score}")
    def has_questions(self):
        return self.question_number<len(self.question)





