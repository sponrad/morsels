import math
from decimal import Decimal


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


def calculate_gpa(grades):
    gpas = {
        'A+': Decimal('4.33'),
        'A': Decimal('4.00'),
        'A-': Decimal('3.67'),
        'B+': Decimal('3.33'),
        'B': Decimal('3.00'),
        'B-': Decimal('2.67'),
        'C+': Decimal('2.33'),
        'C': Decimal('2.00'),
        'C-': Decimal('1.67'),
        'D+': Decimal('1.33'),
        'D': Decimal('1.00'),
        'D-': Decimal('0.67'),
        'F': Decimal('0.00'),
    }
    grade_gpas = [gpas[grade] for grade in grades]
    return float(sum(grade_gpas) / len(grade_gpas))
