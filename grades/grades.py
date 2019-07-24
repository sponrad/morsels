import math


# https://stackoverflow.com/questions/10093783/rounding-error-in-python-with-non-odd-number/10093820#10093820
# does 0.5 rounding UP instead of bankers rounding
def my_round(x):
    return int(x + math.copysign(0.5, x))


def suffixize(percent, grade):
    ones = percent % 10
    suffix = ''
    if ones >= 7 or (percent == 100):
        suffix = '+'
    elif ones < 3:
        suffix = '-'
    return '{}{}'.format(grade, suffix)


def percent_to_grade(percent, *, suffix=False, round=False):
    grade = None
    if round:
        percent = my_round(percent)
    if percent >= 90:
        grade = 'A'
    elif percent >= 80:
        grade = 'B'
    elif percent >= 70:
        grade = 'C'
    elif percent >= 60:
        grade = 'D'
    if grade:
        return suffixize(percent, grade) if suffix else grade
    return 'F'


GPAS = {
    'A+': 4.33,
    'A': 4.00,
    'A-': 3.67,
    'B+': 3.33,
    'B': 3.00,
    'B-': 2.67,
    'C+': 2.33,
    'C': 2.00,
    'C-': 1.67,
    'D+': 1.33,
    'D': 1.00,
    'D-': 0.67,
    'F': 0.00,
}


def calculate_gpa(grades):
    return sum(GPAS[grade] for grade in grades) / len(grades)
