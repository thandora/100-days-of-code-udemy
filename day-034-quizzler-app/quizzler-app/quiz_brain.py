import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.n_questions = len(q_list)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        question_text = html.unescape(self.current_question.text)
        self.question_number += 1
        question_prompt = f"Q: {self.question_number}/{self.n_questions}\n{question_text}"
        return question_prompt

    def check_answer(self, user_answer: str) -> bool:
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            return True
        else:
            return False
