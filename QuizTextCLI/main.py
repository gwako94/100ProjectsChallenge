from random import random
import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


questions = [Question(question['text'], question['answer']) for question in question_data]

quiz = QuizBrain(questions)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
