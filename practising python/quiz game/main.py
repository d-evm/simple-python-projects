from quiz_brain import QuizBrain
import os
from data import question_data
from question_model import question
os.system('cls')

question_bank = []

for ques in question_data:
    ques_text = ques["text"]
    ques_ans = ques["answer"]

    new_question = question(ques_text, ques_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
