#!/usr/bin/python3

def dif(list):
    ''' returns True if all numbers in list are different otherwise False '''
    return len(list) == len(set(list))

def rm_third(list, index=0):
    ''' remove every third number from a list of numbers '''
    print(list)
    
    l = len(list)

    if l == 0:
        return

    index = (index + 2) % l

    list.remove(list[index])
    rm_third(list)




rm_third([10, 20, 30, 40, 50, 60, 70, 80, 90])
