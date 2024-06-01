class QuizBrain:

    score = 0

    def __init__(self, question_list):
        self.q_list = question_list
        self.q_num = 0
        self.score = 0

    def next_question(self):
        question = self.q_list[self.q_num]
        self.q_num += 1
        answer = input(f"Q.{self.q_num}: {question.text}. (True/False)?: ")
        self.check_answer(answer, question.answer)

    def still_has_questions(self):
        return self.q_num < len(self.q_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.q_num}")
        print("\n")


