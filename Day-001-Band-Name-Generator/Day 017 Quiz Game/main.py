import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in data.question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("Quiz compelted.")
print(f"Final score: {quiz_brain.score}/{len(quiz_brain.question_list)}.")
