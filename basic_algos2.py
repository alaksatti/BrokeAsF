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


def txt_freq(str):
    ''' take a string and print words and occurences'''
    words = str.split()
    freq = [words.count(n) for n in words]
    print(list(zip(words, freq)))

    
    
def target_value(la, lb, lc, target):
    ''' check the sum of three elements from different arrays is equal to target value '''
    fin = []
    for a in la:
        for b in lb:
            for c in lc:
                if a + b + c == target and (a, b, c) not in fin:
                    fin.append((a, b, c))

                    print(fin)

def median(x, y, z):
    '''find the median in a list of three numbers'''
    l = [x, y, z]
    l.sort()
    return(l[1])

 
def rev_even(txt):
    ''' reverses all words with an even length '''
    words = txt.split()
    words = ' '.join(word[::-1] if len(word) % 2 == 0 else word for word in words)    
    return words


def ish(num):
    ''' checks if an int is oddish or evenish by summing the idv. digits'''

    sum_num = eval('+'.join(d for d in str(num)))

    if sum_num % 2 == 0:
        return 'evenish'
    return 'oddish'



def running(list, idx=1):
    ''' returns list of running total '''

    if len(list) <= 1:
        return list
    
    list[idx] = list[idx] + list[idx - 1]

    if idx + 1 < len(list):
        running(list, idx + 1)

    return list

