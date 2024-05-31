'''
Created on Oct. 31, 2023
Unit test for yahtzee 2
@author: Sebastian
'''
from yahtzee2 import sum_of_given_number, fill_upper_section, sum_of_all_numbers, num_of_a_kind, yahtzee

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
    
def test_three_of_a_kind_found():
    """
    Tests num_of_a_kind() with a roll that has "3 of a kind".
    """
    roll = (3,5,3,2,3)
    assert num_of_a_kind(roll, 3) == 16

def test_three_of_a_kind_not_found():
    """
    Tests num_of_a_kind() with a roll that doesn't have "3 of a kind".
    """
    roll = (1,2,3,4,5)
    assert num_of_a_kind(roll, 3) == 0

def test_four_of_a_kind_found():
    """
    Tests num_of_a_kind() with a roll that has "4 of a kind".
    """
    roll = (4,4,2,4,4)
    assert num_of_a_kind(roll, 4) == 18

def test_four_of_a_kind_not_found():
    """
    Tests num_of_a_kind() with a roll that doesn't have "4 of a kind".
    """
    roll = (1,2,3,4,5)
    assert num_of_a_kind(roll, 4) == 0

def test_yahtzee_found():
    """
    Tests yahtzee() with a roll that has a yahtzee.
    """
    roll = (1,1,1,1,1)
    assert yahtzee(roll) == 50

def test_yahtzee_not_found():
    """
    Tests yahtzee() with a roll that has no yahtzee.
    """
    roll = (1,2,3,4,5)
    assert yahtzee(roll) == 0
