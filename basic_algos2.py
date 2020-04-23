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
    rm_third(list, index)



def sum_zero(list, idx1=0, idx2=1, idx3=2):
    ''' prints unique triplets that sum to 0 in list '''
    ''' unique where abs value of ints are unequal '''
    l = [list[idx1], list[idx2], list[idx3]]

    u = [-x if x < 0 else x for x in l]

    if len(set(u)) == 3 and sum(l) == 0:
        print(l)

    if idx3 + 1 < len(list):
        sum_zero(list, idx1+1, idx2+1, idx3+1)
        
    return


