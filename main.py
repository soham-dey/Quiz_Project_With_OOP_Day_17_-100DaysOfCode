from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for i in question_data:
    new_question = Question(i["text"], i["answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
    quiz_brain.question_number += 1

print(f"You've completed the quiz.\nYour final score is {quiz_brain.current_score}/{quiz_brain.current_total_score}.")