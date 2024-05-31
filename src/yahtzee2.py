'''
Created on Oct. 31, 2023
Yahtzee with part of the additional scoring methods
@author: Sebastian

'''
import random

def make_roll():
    '''
    Randomly selects 5 numbers from 1 to 6 inclusive
    '''
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    r3 = random.randint(1,6)
    r4 = random.randint(1,6)
    r5 = random.randint(1,6)
    return r1,r2,r3,r4,r5

def sum_of_given_number(roll, target):
    '''
    sums all occurences of a given number in a list
    '''
    sum_num = 0
    for number in roll :
        if number == target:
            sum_num += target
    return sum_num
    
def fill_upper_section(roll): 
    '''
    Takes a tuple of numbers from 1 to 6 and adds the sum of all occurences of every number to a list
    For example (2,4,5,3,2) would make the list [0,4,3,4,5,0]
    '''
    upper_list = [sum_of_given_number(roll, 1),sum_of_given_number(roll, 2),sum_of_given_number(roll, 3),sum_of_given_number(roll, 4),
                  sum_of_given_number(roll, 5),sum_of_given_number(roll, 6)]
    return upper_list
    
def display_upper_section(upper_section):
    '''
    prints a formatted text of all the values in the upper section
    '''
    print(f"Aces: {upper_section[0]} \nTwos: {upper_section[1]}\nThrees: {upper_section[2]} \nFours: {upper_section[3]} \nFives: {upper_section[4]} \nSixes {upper_section[5]}")
    
def num_of_a_kind(roll, number):
    """
    If a roll has EXACTLY `number` dice of the same face value,
    returns the sum of all five values in the roll.
    Otherwise, returns 0.
    """
    list = fill_upper_section(roll)
    for idx in range(len(list)) :
        if list[idx] == (idx+1)*number :
            return sum_of_all_numbers(roll)
    return 0

def sum_of_all_numbers(roll):
    '''
    Sums all numbers in a roll
    '''
    total = 0
    for num in roll :
        total += num
    return total
    
def yahtzee(roll):
    """
    Returns 50 if the roll is a Yahtzee (all dice in the roll have the same
    face value). Otherwise, returns 0.
    """
    list = fill_upper_section(roll)
    for idx in range(len(list)) :
        if list[idx] == (idx+1)*5 :
            return 50
    return 0

def main():
    roll = make_roll()
    print(f"Rolling the dice... {roll}")
    upper_section = fill_upper_section(roll)
    print("Upper Section:")
    display_upper_section(upper_section)
    print("Lower Section:")
    print(f"Three of a Kind: {num_of_a_kind(roll, 3)}")
    print(f"Four of a Kind: {num_of_a_kind(roll, 4)}")
    print(f"Yahtzee: {yahtzee(roll)}")
    
if __name__ == "__main__" :
    main()