from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for d in question_data:
    question_bank.append(Question(d['question'], d['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    score = quiz.next_question()

print(f"You've completed the quiz!")
print(f"Your final score is {score}/{len(question_bank)}")