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



def sum_zero(list, idx1=0, idx2=1, idx3=2):
    l = [list[idx1], list[idx2], list[idx3]]

    u = [-x if x < 0 else x for x in l]

    if len(set(u)) == 3 and sum(l) == 0:
        print(l)

    if idx3 + 1 < len(list):
        sum_zero(list, idx1+1, idx2+1, idx3+1)
        
    return

sum_zero([1, -6, 4, 2, -1, 2, 0, -2, 0])
