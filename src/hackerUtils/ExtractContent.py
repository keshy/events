'''
Created on Jan 30, 2013

@author: Krishnan_Narayan
'''
# File module to extract file contents of the format 
# Number of lines(n) 
#
# line-0
# ...
# line-n
# Returns an array of strings with each string containing a line


def extractLines(filename):
    if not filename:
        print ("Please enter a valid file name")
    try: 
        lines = tuple(open(filename, 'r'))
        if int(lines[0]) == (lines.__len__() - 1):
            return lines
        else:
            print ("Number of lines in line 1 and the number of lines following do not add up")
            return None
    except IOError as e:
        print ("I/O error ({0}): {1}".format(e.errno, e.strerror)) 
