class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_score = 0
        self.current_total_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False)?: ")
        self.current_total_score += 1
        if user_answer == current_question.answer:
            self.current_score += 1
            print(f"You got it right!\nThe correct answer was: {current_question.answer}\nYour current "
                  f"score is: {self.current_score}/{self.current_total_score}\n")
        else:
            print(f"You got it wrong!\nThe correct answer was: {current_question.answer}\nYour current "
                  f"score is: {self.current_score}/{self.current_total_score}\n")