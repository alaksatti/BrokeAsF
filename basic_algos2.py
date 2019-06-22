#!/usr/bin/python3

def dif(list):
    ''' returns True if all numbers in list are different otherwise False '''
    return len(list) == len(set(list))

