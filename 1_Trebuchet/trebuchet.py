"""
A calibration document consists of lines of text. Each line originally contains
a calibration value that needs to be recovered. On each line, the calibration
value can be found by combining the first digit and the last digit to form a single
two-digit number. 

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

The calibration values of the four lines are 12, 38, 15 and 77. Added together they
form 142. What is the sum of all the calibration values?
"""

def calibration_value(input: str):

    numbers = [char for char in input if char.isdigit()]

    return int(int(numbers[0]) * 10 + int(numbers[-1]))

def total_calibration(doc):

    calibration_values = [calibration_value(line) for line in doc.split('\n')]

    return sum(calibration_values)

test = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"

print(total_calibration(test))