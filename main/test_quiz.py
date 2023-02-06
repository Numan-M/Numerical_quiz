import pytest
from questions import Add, Multiply, Subtract
from quiz import Quiz

def test_question_text_and_answer_types():
    add = Add(1,2)
    assert add.text == '1 + 2'
    assert isinstance(add.answer, int)
    
    multiply = Multiply(1,2)
    assert multiply.text == '1 x 2'
    assert isinstance(multiply.answer, int)
    
    subtract = Subtract(1,2)
    assert subtract.text == '1 - 2'
    assert isinstance(subtract.answer, int)
    
def test_quiz_question_count():
    quiz = Quiz()
    assert len(quiz.questions) == 10
    


def test_total_correct_answers():
    quiz = Quiz()
    quiz.answers = [(True, 0), (True, 0), (False, 0), (True, 0), (False, 0)]
    assert quiz.total_correct() == 3
