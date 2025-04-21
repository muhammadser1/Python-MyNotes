from data import question_data
from question_model import Question
from quiz import Quiz

question_bank = []
for i in range(len(question_data)-5):
    question = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(question)
quiz = Quiz(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
