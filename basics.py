#!/usr/bin/python3


def concatenate(list):
    ''' concatenate all elements in a list into a string and return it '''
    concatenated = ''.join(map(str, list))
    return concatenated

def inlist_1(list_1, list_2):
    ''' returns items in list 1 that are not in list 2 '''
    return set(list_1) - set(list_2)

def gcd(a, b):
    ''' returns the greatest common denominator '''
    if b:
        return gcd(b, a % b)
    else:
        return a

def lcm(a, b):
    ''' returns the least common multiple '''
    return (a * b / (gcd(a, b)))

def sumthree(a, b, c):
    ''' returns the sum of 3 numbers unless 2 of them are identical '''
    l = [a, b, c]
    set_l = set(l)
    if len(set_l) < 3:
        return 0
    else:
        return a + b + c

def addint(a, b):
    ''' add numbers together if they are int objects'''
    try:
        return a + b
    except TypeError:
        return'not integers'

def findfile(filename):
    ''' check whether a file exists '''
    import os.path
    return os.path.isfile(filename)
