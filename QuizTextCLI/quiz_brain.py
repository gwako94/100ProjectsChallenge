class QuizBrain:
    """ Models the quiz brain """
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        correct_answer = current_question.answer
                
        if user_answer not in ('true', 'false'):
            print("Invalid answer, please choose true or false")
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, correct_answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            print(f"Your score is {self.score}/{self.question_number}")
        else:
            print("You got it wrong!")
        print(f"The correct answer was {correct_answer}. ")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")
