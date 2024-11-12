class QuizBrain:

    def __init__(self, q_list):
        self.q_no = 0
        self.score = 0
        self.question_list = q_list


    def still_has_questions(self):
        return self.q_no < len(self.question_list)

    def next_question(self):
            current_question = self.question_list[self.q_no]
            self.q_no += 1
            user_answer = input(f"Q.{self.q_no}: {current_question.text} (True/False):")
            self.check_answer(user_answer,current_question.answer)


    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct Answer.")
        else:
            print("Incorrect Answer")

        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.q_no}")

