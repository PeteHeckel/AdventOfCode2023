"""Day 1 of Advent Code: Trebuchet?!

Keyword arguments: 
calibration_input:str -- input file containing calibration codes 
Return: Calibration Value:int -- Final calibration result 
"""

import numbers
from pathlib import PosixPath
import sys


def get_calibration_value_with_strings(cal_val: str ):
    num_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
                'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    num_list = [str(i) for i in range(10)]
    num_list.extend(list(num_dict.keys()))

    first_num = None
    first_num_idx = None
    last_num = None
    last_num_idx = None
    for number in num_list:
        f_idx = cal_val.find(number)
        l_idx = cal_val.rfind(number)
        if f_idx != -1:
            if  first_num_idx is None or f_idx < first_num_idx:
                first_num_idx = f_idx
                first_num = number
            if  last_num_idx is None or l_idx > last_num_idx:
                last_num_idx = l_idx
                last_num = number
    if first_num is None:
        return 0
    
    if first_num in num_dict.keys():
        first_num = num_dict[first_num]
    if last_num in num_dict.keys():
        last_num = num_dict[last_num]

    cal_val = 10*int(first_num) + int(last_num)
    print(cal_val)
    return cal_val

def get_calibration_value( cal_val: str ):
    first_digit = None

    for char in cal_val:
        if char.isnumeric():
            first_digit = int(char)
            break

    if first_digit is None:
        return 0

    for char in reversed(cal_val):
        if char.isnumeric():
            second_digit = int(char)        
            break

    return 10*first_digit + second_digit

def sum_coefficients( input_file ):

    output_sum = 0
    part2_sum = 0
    with open(input_file, "r") as f:
        for line in f:
            output_sum += get_calibration_value(line)
            part2_sum += get_calibration_value_with_strings(line)
    return (output_sum, part2_sum)


if __name__ == '__main__':
    if (len(sys.argv) != 2) or not PosixPath(sys.argv[1]).is_file() :
        print('Error 1 file argument needed')
        exit(1)
    
    cal_sum, part2_sum = sum_coefficients(sys.argv[1])

    print(f"Calibration Value Sum = {cal_sum}")
    print(f"Part 2 Calibration Value Sum = {part2_sum}")

    exit(0)
