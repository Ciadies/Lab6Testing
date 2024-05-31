'''
Created on Oct. 31, 2023
Unit test for this (you can ignore this part this is a note to myself: To run the unit test, go all the way to the src file then run <python -m pytest "TEST FILE NAME">)
@author: Sebastian
'''

from yahtzee1 import sum_of_given_number, fill_upper_section

def test_sum_of_given_number_all_different():
    """
    Tests sum_of_given_number() with one roll
    where all dice have different face values.
    """
    roll = (2,3,4,6,5)
    assert sum_of_given_number(roll, 1) == 0
    assert sum_of_given_number(roll, 2) == 2
    assert sum_of_given_number(roll, 3) == 3
    assert sum_of_given_number(roll, 4) == 4
    assert sum_of_given_number(roll, 5) == 5
    assert sum_of_given_number(roll, 6) == 6

def test_sum_of_given_number_all_same():
    """
    Test sum_of_given_number() with one roll
    where all dice have the same face value.
    """
    roll = (6,6,6,6,6)
    assert sum_of_given_number(roll, 1) == 0
    assert sum_of_given_number(roll, 2) == 0
    assert sum_of_given_number(roll, 3) == 0
    assert sum_of_given_number(roll, 4) == 0
    assert sum_of_given_number(roll, 5) == 0
    assert sum_of_given_number(roll, 6) == 30

def test_sum_of_given_number_some_different():
    """
    Test sum_of_given_number() with one roll
    where some dice have the same face value.
    """
    roll = (2,3,5,2,2)
    assert sum_of_given_number(roll, 1) == 0
    assert sum_of_given_number(roll, 2) == 6
    assert sum_of_given_number(roll, 3) == 3
    assert sum_of_given_number(roll, 4) == 0
    assert sum_of_given_number(roll, 5) == 5
    assert sum_of_given_number(roll, 6) == 0

def test_fill_upper_section():
    """
    Test fill_upper_section() with any one roll of your choice.
    """
    roll = (2,5,4,4,6)
    assert fill_upper_section(roll) == [0,2,0,8,5,6]