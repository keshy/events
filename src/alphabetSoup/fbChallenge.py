'''
Created on Jan 31, 2013

@author: Krishnan_Narayan
'''
# module to extract input
def extractLines(filename):
    if not filename:
        print("Please enter valid file name")
    
    try: 
        lines = tuple(open(filename, 'r'))
        totalCases = 0
        if int(lines[0]) is not None or lines.__len__() > 2:
            totalCases = int(lines[0])
            return lines, totalCases
        else:
            print ("Number of lines in line 1 and the number of lines following do not add up")
            return None
    except IOError as e:
        print ("I/O error ({0}): {1}".format(e.errno, e.strerror)) 
    

def extractSet(lines, index):
    if not lines:
        print("no lines received")
        
    
    
    n_m = lines[0].split(' ')
    if n_m is None or n_m.__len__() < 2:
        return None  
    n = n_m[0]
    m = n_m[1]   
    army_cost = {}
    
    i = index
    index += (n + m)
    
    # load costs into array
    while i < (i + n):
        cost = lines[i].split(' ')
        if cost is not None and cost.__len__() == 2:
            
         
        i += 1           
                
    # map roads to array
    
    while i < index:
        roads = lines[i].split(' ')
        if roads is not None and roads.__len__() == 2:
            
            
             
         
