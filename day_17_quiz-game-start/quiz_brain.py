class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False

    def next_question(self):
        question = self.question_list[self.question_number]
        question_text = question.text
        question_answer = question.answer
        user_answer = input(f" {question_text} (True/False) : ")
        if self.check_answer(user_answer, question_answer):
            print(f"You are right!")
            self.score += 1
        else:
            print(f"You are wrong.")

        print(f"The correct answer was {question_answer}")
        print(f"Your current score is {self.score}/{self.question_number + 1}")
        self.question_number += 1
        return self.score

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            return True
        return False