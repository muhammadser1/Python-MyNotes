from ui import QuizInterface
from data import fetch_questions
from quiz_brain import QuizBrain

question_bank = fetch_questions()
quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)
