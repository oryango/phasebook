import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):

    fave_numbers_1 = sort_matches(fave_numbers_1)
    fave_numbers_2 = sort_matches(fave_numbers_2)
    memo = []
    for number in fave_numbers_2:

        if(len(memo) > 3):
            truth_val, temp = search_number(number, memo[-3])
            if(truth_val):
                continue

        truth_val, memo = search_number(number, fave_numbers_1) 
        if(not truth_val):
            return False

    return True


def sort_matches(user_numbers):
    right_index = len(user_numbers)//2

    half_index = right_index

    left_half = user_numbers[:half_index]
    right_half = user_numbers[right_index:]

    if(half_index > 0):
        left_half = sort_matches(left_half)
        right_half = sort_matches(right_half)

    left_counter = 0
    right_counter = 0
    last_movement = 'left'
    sorted_matches = []

    while(left_counter < len(left_half) and right_counter < len(right_half)):
        if(left_half[left_counter] <= right_half[right_counter]):
            sorted_matches.append(left_half[left_counter])
            left_counter += 1
            last_movement = 'left'
        else:
            sorted_matches.append(right_half[right_counter])
            right_counter += 1
            last_movement = 'right'

    if(last_movement == 'left'):
        sorted_matches = sorted_matches + right_half[right_counter:]
    else:
        sorted_matches = sorted_matches + left_half[left_counter:]


    return sorted_matches

"""
def search_number(number, fave_numbers):
    half = len(fave_numbers)//2-1

    
    if(number == fave_numbers[half]):
        return True
    elif(number < fave_numbers[half]):
        new_half = fave_numbers[:half]
        if(len(new_half) <= 1):
            if(len(new_half) == 1 and new_half[0] == number):
                return True
            else:
                return False
        return search_number(number,new_half)
    elif(number > fave_numbers[half]):
        new_half = fave_numbers[half+1:]

        if(len(new_half) <= 1):
            if(len(new_half) == 1 and new_half[0] == number):
                return True
            else:
                return False
        return search_number(number,new_half)
"""
def search_number(number, fave_numbers):
    memo = []
    old_half = fave_numbers
    while(True):
        half = len(old_half)//2-1
        if(number == old_half[half]):
            return True, memo
        elif(number < old_half[half]):
            new_half = old_half[:half]
            if(len(new_half) <= 1):
                if(len(new_half) == 1 and new_half[0] == number):
                    return True, memo
                else:
                    return False, []
            old_half = new_half
            memo.append(new_half)
        elif(number > old_half[half]):
            new_half = old_half[half+1:]
            if(len(new_half) <= 1):
                if(len(new_half) == 1 and new_half[0] == number):
                    return True, memo
                else:
                    return False, []
            old_half = new_half
            memo.append(new_half)
    return True, memo