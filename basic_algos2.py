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
lists = [1, -6, 4, 2, -1, 2, 0, -2, 0]

idx1, idx2, idx3 = 0, 1, 2

while idx3 < len(lists):
    l = [lists[idx1], lists[idx2], lists[idx3]]

    u = [-x if x < 0 else x for x in l]

    if len(set(u)) == 3 and sum(l) == 0:
        print(l)


    idx1+=1
    idx2+=1
    idx3+=1
