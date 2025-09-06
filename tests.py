import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_create_choice_with_invalid_text():
    with pytest.raises(Exception):
        Choice(text='')
    with pytest.raises(Exception):
        Choice(text='a'*101)
    with pytest.raises(Exception):
        Choice(text='a'*500)

def test_remove_choice():
    question = Question(title='q1')

    question.add_choice('a', False)

    choice = question.choices[0]
    question.remove_choice_by_id(1)
    assert len(question.choices) == 0

def test_remove_non_existing_choice():
    with pytest.raises(Exception):
        question.remove_choice_by_id(1)

def test_remove_all_questions():
    question = Question(title='q1')

    question.add_choice('a', False)
    question.add_choice('b', False)

    assert len(question.choices) == 2 
    question.remove_all_choices()
    assert len(question.choices) == 0

def test_correct_choice():
    question = Question(title='q1')

    question.add_choice('a', False)
    question.set_correct_choices([1])

    assert question.correct_selected_choices([1]) == [1]

def test_multiple_correct_choices():
    question = Question(title='q1')

    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.set_correct_choices([2, 3])
    assert question.correct_selected_choices([2]) == [2]
    assert question.correct_selected_choices([3]) == [3]

def test_select_more_than_max_selections_allowed():
    question = Question(title='q1', max_selections=2)

    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.set_correct_choices([2, 3])

    with pytest.raises(Exception):
        question.correct_selected_choices([1, 2, 3])

def test_correct_wrong_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.set_correct_choices([2, 3])

    assert question.correct_selected_choices([1]) == []

def test_create_question_with_invalid_points(): 
    with pytest.raises(Exception):
        question = Question(title='q1', points=101)

def test_if_generated_choices_ids_are_sequential():
    question = Question(title='q1')

    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)

    question.remove_choice_by_id(2)

    question.add_choice('d', False)
    choice = question.choices[2]
    assert choice.id == 4
