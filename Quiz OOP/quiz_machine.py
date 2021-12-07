class QuizMachine:
  def __init__ (self, qList):
    self.question_number = 0
    self.question_list = qList
    self.score = 0

  def more_question(self):
    return self.question_number < len(self.question_list)

  def nextQuestion(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q. {self.question_number}: {current_question.text} (True\False) ")
    self.check_ans(user_answer,current_question.answer)

  def check_ans(self, user_ans, current_ans):
    if user_ans.lower() == current_ans.lower():
      self.score += 1
      print('You got it right')
      print(f'Your Current Score is {self.score}/{self.question_number}')
    else:
      print('Wrong answer')
      print(f'Correct answer was {current_ans}')
      print(f'Your Current Score is {self.score}/{self.question_number}')
    print('\n')
