from q_model import Question
from data import question_data
from quiz_machine import QuizMachine

question_bank = []

for question in question_data:
  newQuestion = Question(question["question"],question['correct_answer'])
  #print(newQuestion)
  question_bank.append(newQuestion)

quiz = QuizMachine(question_bank)

while quiz.more_question():
  quiz.nextQuestion()

print('You"ve Completed The Quiz')
print(f'Your Final Score is {quiz.score}/{quiz.question_number}')
