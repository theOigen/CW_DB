import math

BUDGET = 'budget'
REVENUE = 'revenue'


def isNoneValue(value) -> bool:
    return value is None


def isIncorrectNum(value) -> bool:
    return (type(value) is int or type(value) is float) and math.isnan(value)


def isBudgetOrRevenueNil(key: str, value: int) -> bool:
    return (key == BUDGET or key == REVENUE) and int(value) == 0


def filter_movies(record):
    is_valid = False
    for key in record.keys():
        value = record[key]
        if isNoneValue(value) or isIncorrectNum(value) or isBudgetOrRevenueNil(key, value):
            return False
        is_valid = True
    return is_valid
