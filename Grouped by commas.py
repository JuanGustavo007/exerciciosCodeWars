"""
Finish the solution so that it takes an input n (integer) and returns a string that is the decimal
representation of the number grouped by commas after every 3 digits.

"""

def group_by_commas(n):
    formatted = format(n, ',')
    return formatted# Saída: 1.000.000

group_by_commas(1234)