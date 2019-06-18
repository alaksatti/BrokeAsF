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
    nums = set(l)
    if len(nums) < 3:
        return 0
    else:
        return sum(map(int, nums))

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

def listfiles(directory):
    ''' list files in a particular directory '''
    from os import listdir
    #from os.path import isfile, join
    #file_list = [f for f in listdir(directory) if isfile(join(directory, f))]
    file_list = [ f for f in listdir(directory)]
    return file_list


def profile(function):
    ''' returns the profile of a file'''
    from cProfile import run
    try:
        run(function)
    except:
        print('make sure funciton exists and is passed as a string')


def sumofnpos(list, n):
    ''' returns the first n pos numbers in a list '''
    counter = 0
    
    if n is None or list is None or n > len(list):
        return
    
    newlist = []
    
    for i in list:
        if counter != n and int(i) > 0:
            newlist.append(i)
            counter+=1

    return ', '.join(map(str, newlist))

def height_cm(ft, inch):
    ''' convert height to cm '''
    ft = int(ft) * 12
    total  = (ft + int(inch)) * 2.54
    return round(total, 2)


def abspath(filename):
    ''' returns abs path of filename'''
    import os.path
    return os.path.abspath(str(filename))


def sumdigits(ints):
    ''' return sum of digits in a number'''
    ints = str(ints)
    return sum((int(i)) for i in ints)


def sorter(a, b, c):
    ''' sorts 3 ints without conditions or loops'''
    num = sorted([a, b, c])
    return ' '.join(map(str, num)) 

