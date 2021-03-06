'''
Created on Jun 27, 2013

Problem: https://www.hackerrank.com/challenges/saveprincess2
@author: Krishnan_Narayan
'''
'''
Class to implement an enum to keep track of movements of the bot 
'''
class Moves:
    UP = "UP";
    DOWN = "DOWN";
    LEFT = "LEFT";
    RIGHT = "RIGHT";
    NONE = "NULL";


'''
Takes in two points on the grid and returns the set of moves required based on the shortest path algorithm
@param bot: Bot co-ordinates on the grid
@param princess: Princess co-ordinates on the grid

@return: the shortest set of moves for the bot to reach the princess   
'''
def nextMove(n, x, y, grid):
    
    bot, princess = getCordinates(n, grid);
    
    if bot == None or princess == None:
        return None;
    
    bot_x, bot_y = bot;
    princess_x, princess_y = princess;
    
    if bot_x == princess_x and bot_y == princess_y:
        return None;
    
    # Case 1: Same column, move rows
    elif bot_y == princess_y:
        if bot_x < princess_x:
            return Moves.DOWN;
            bot = (bot_x + 1, bot_y);  
        elif bot_x > princess_x:
            return Moves.UP;
            bot = (bot_x - 1, bot_y);
    
    # Case 2: Same row, move columns
    elif bot_x == princess_x:
        if bot_y < princess_y:
            return Moves.RIGHT;    
        elif bot_y > princess_y:
            return Moves.LEFT;
    
    # Case 3: No matching row or column..in this case the path can be traversing either 
    # side of the rectangle formed with the bot and the princess on either end verticies
    else:
        # get to same row as princess i.e. increase or decrease x
        if bot_x < princess_x:
            return Moves.DOWN;
        elif bot_x > princess_x:
            return Moves.UP;
    
        
        
    
    
        
'''
@param n: Number of rows and columns in the grid
@param grid: character array containing the placements of the bot and the princess.
@return: min set of moves required for the bot to reach the princess 
'''  
def getCordinates(n, grid):
    'basic input validation'
    if n < 1 or grid == None:
        return None;
    elif n == 1:
        return Moves.NONE;
    bot = ();
    princess = ();
    i = 0;
    for arr in grid:
        if arr.__len__() != n:
            return None;
        else:
            # get index of bot and princess
            j = 0;
            for ch in arr:
                if ch == 'm':
                    bot = (i, j);
                elif ch == 'p':
                    princess = (i, j);
                j += 1;
                
        i += 1;
     
    return bot, princess;           
                    
        
    
    
    
# print all the moves here
# Tail starts here
n = int(input())
x, y = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, x, y, grid))
