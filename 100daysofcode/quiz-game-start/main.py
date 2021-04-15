from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for key in question_data:
    ques = key["text"]
    ans = key["answer"]
    new_question = Question(ques, ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
