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


def greater(list, num):
    ''' returns numbers that are greater than a specified number'''
    return ' '.join(str(i) for i in list if int(i) > num)


def numchar(str, char):
    ''' returns the number of occurences of a character in a string'''
    if char is None or str is None:
        return

    return str.count(char)


def swap(a, b):
    ''' swap two variables '''
    a, b = b, a
    return a, b


def numeric_string(number):
    ''' determine if string is numeric or not '''
    
    try:
        return int(number)
    except:
        return 'not a nummeric number'

def print_url_contents(url):
    '''request and print contents of url'''
    import requests

    r = requests.get(url)
    print(r.content)

def divfif(lists):
    ''' with anonymous function find numbers divisible by 15 in a list '''
    for x in list(map(lambda x: x, filter(lambda x: x % 15 == 0, lists))):
        print(x, end=' ')

    print()

def filpos(lists):
    ''' filter positive numbers from a list'''
    return list(filter(lambda x: x > 0, lists))



def prod_int(list_int):
    ''' compute the products of a list of ints '''
    
    '''
    from functools import reduce
    try: 
        return reduce(lambda x, y: int(x) * int(y), list_int)


    except:
        return 'must be integers'
    '''

    list_int = list(map(str, list_int))
    return eval('*'.join(list_int))


def two_is_same(str1, str2):
    '''check if two strings of the same value point to same memory location'''
    return str1 is str2

def lowercase(str1):
    '''check if lowercase character exists in a string'''
    return list(filter(lambda x: x.islower(), str1))

def ljust(str1):
    ''' add trailing zeros to a string '''
    return str1.ljust(10, '0')


def singleline_int():
    ''' take two ints taken from input and display on a single line '''
    x, y = map(int, input('input x and y: ').split())
    return x, y

def oneandzero(str):
    ''' converts true to 1 and 0 to false '''
    if str.lower() not in ['true', 'false']:
        return 'string not true or false'

    return 1 if str.lower() == 'true' else 0

def binary(num):
    ''' convert a number to binary and keep leading zeros'''
    return "{0:b}".format(num)


def cubem(n):
    ''' returns the sum of the cube of all positive numbers smaller than specified number '''
    if not isinstance(n, int) or n < 0:
        return
    
    return sum(i ** 3 for i in range(1, n))
    
def oddprod(list):
    ''' find the odd product of any two numbers in a list '''
    l = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if i != j:
                if (list[i] * list[j]) & 1:
                    l.append(str(list[i] * list[j]))
    return ' '.join(l)

