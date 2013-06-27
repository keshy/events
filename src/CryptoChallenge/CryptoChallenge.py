'''
Created on Feb 19, 2013

@author: Krishnan_Narayan
'''
import hackerUtils.ExtractContent

def split2Ascii(line):
    
    if line is None:
        return None
    
    i = 0
    dec = 0
    result = [] 
    while i < line.__len__():
        dec = int(line[i]) * 10 + int(line[i + 1])
        i += 2
        result.append(chr(dec))
        dec = 0
        
    if result is not None:
        f = open("../lib/cipher_to_ascii.txt", 'w')
        for char in result:
            f.write(char + ' ')
        
        f.close()
        
 
def planSubstitution(singleDigitFlag, line):
    
    if line is None:
        return None
    
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w' , 'x', 'y', 'z']
    resultCase1 = []
    resultCase2 = []
    if singleDigitFlag:
        for char in line:
            if char.isnumeric():
                resultCase1.append(alpha[int(char) - 1])
    else:
        # go through the list and see if there is a number less than 25 then use two at a time else use one digit at a time  
        i = 0
        while i < line.__len__():
            dec = int(line[i]) * 10 + int(line[i + 1])
            if dec > 26:
                # for each digit take the substitution value as in case 1
                resultCase2.append(alpha[int(line[i]) - 1])
                resultCase2.append(alpha[int(line[i + 1]) - 1])
            else:
                resultCase2.append(alpha[dec - 1])
            
            i += 2
            
    if resultCase1 is not None and resultCase1.__len__() > 0:
        writeToFile(resultCase1, "singleDigitSubstitution.txt") 
    elif resultCase2 is not None and resultCase2.__len__() > 0:
        writeToFile(resultCase2, "twoDigitSubstitution.txt")


def writeToFile(result, filename):
    if result is None or result.__len__() == 0:
        return None
    f = open("../lib/" + filename, 'w')
    for char in result:
        f.write(char + ' ')
    f.close()
    
def charFreq(line):
    # function to get a count of the number of characters occuring for each character identified
    result = {}
    for char in line:
        if result.get(char) is None:
            result[char] = 1
        else:
            i = result.get(char)
            i += 1
            result[char] = i
            
    f = open("../lib/freq.txt", 'w')
    for res in result.keys():
        f.write(res + ":" + str(result.get(res)) + "\n")
    f.close()
                        
    
split2Ascii(hackerUtils.ExtractContent.extractLines("../lib/crypto.txt")[1])
planSubstitution(True, hackerUtils.ExtractContent.extractLines("../lib/crypto.txt")[1])
charFreq(hackerUtils.ExtractContent.extractLines("../lib/cipherFreq.txt")[1])
