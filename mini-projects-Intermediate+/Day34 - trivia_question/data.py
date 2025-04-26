import requests
from question_model import Question

AMOUNT = 10
TYPE = "boolean"
CATEGORY = 18


def fetch_questions():
    response = requests.get(f"https://opentdb.com/api.php?amount={AMOUNT}&category={CATEGORY}&type={TYPE}")
    response.raise_for_status()
    questions = response.json()["results"]
    question_bank = []
    for i in range(AMOUNT):
        question_text = questions[i]['question']
        question_answer = questions[i]['correct_answer']
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank