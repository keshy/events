'''
Created on Jan 30, 2013

@author: Krishnan_Narayan
'''
import hackerUtils.ExtractContent
import math

def getHackerCupCount(line):
    count_h = 0
    count_a = 0
    count_c = 0
    count_k = 0
    count_e = 0
    count_r = 0
    count_u = 0
    count_p = 0
    
    for char in line:
        if char == 'h' or char == 'H':
            count_h += 1
        elif char == 'a' or char == 'A':
            count_a += 1
        elif char == 'c' or char == 'C':
            count_c += 1
        elif char == 'k' or char == 'K':
            count_k += 1
        elif char == 'e' or char == 'E':
            count_e += 1    
        elif char == 'r' or char == 'R':
            count_r += 1        
        elif char == 'u' or char == 'U':
            count_u += 1    
        elif char == 'p' or char == 'P':
            count_p += 1
    numbers = []
    numbers.append(count_h)
    numbers.append(count_a)
    numbers.append(count_c)
    numbers.append(count_k)
    numbers.append(count_e)
    numbers.append(count_r)
    numbers.append(count_u)
    numbers.append(count_p)
    
    minVal, index = minNum(numbers)
    if minVal is not 0:
        if index == 2:
            return math.floor(count_c / 2)
        elif numbers[index] <= count_c / 2:
                return math.floor(numbers[index])
        else:
            return math.floor(count_c / 2)
    else:
        return 0        

        
    
    
def minNum(numbers):
    minNum = numbers[0]
    index = 0
    i = 0
    while i < numbers.__len__():
        if numbers[i] < minNum:
            minNum = numbers[i]
            index = i
        i += 1    
    return minNum, index            
    
            
def getFrequency(lines):
    i = 1
    while i < lines.__len__():
        print ("case" + str(i) + ":" + str(getHackerCupCount(lines[i])))
        i += 1
            
            
getFrequency(hackerUtils.ExtractContent.extractLines('../lib/test_input'))        
    
            
            
