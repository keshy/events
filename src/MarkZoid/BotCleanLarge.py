'''
Problem: https://www.hackerrank.com/challenges/botcleanlarge
Created on Jul 8, 2013

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
    CLEAN = "CLEAN";
    NONE = "NONE";


'''
Takes in two points on the grid and returns the set of moves required based on the shortest path algorithm
@param bot: Bot co-ordinates on the grid
@param princess: Princess co-ordinates on the grid

@return: the shortest set of moves for the bot to reach the princess   
'''
def next_move(x, y, dimx, dimy, grid):
    
    bot, dirtyCells = getCordinates(dimx, dimy, grid);
    
    if bot == None or dirtyCells == None or dirtyCells.__len__() == 0:
        return None;
    
    ' this problem inverts the row and column index'
    bot_y, bot_x = x, y;
    princess_x, princess_y = dirtyCells[0];
    
    if bot_x == princess_x and bot_y == princess_y:
        return Moves.CLEAN;
        
    
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
@param dimx: x-dimesion of the grid
@param dimy: y-dimension of the grid
@param grid: character array containing the placements of the bot and the princess.
@return: min set of moves required for the bot to reach the princess 
'''  
def getCordinates(dimx, dimy, grid):
    'basic input validation'
    if dimx < 1 or grid == None:
        return None;
    
    bot = ();
    dirtyCells = [];
    i = 0;
    for arr in grid:
        if arr.__len__() != dimx:
            return None;
        else:
            # get index of bot and princess
            j = 0;
            for ch in arr:
                if ch == 'b':
                    bot = (i, j);
                elif ch == 'd':
                    dirtyCells.append((i, j));
                j += 1;
                
        i += 1;
     
    return bot, dirtyCells;           
                    
        
    
    
    
# Tail starts here
# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    print(next_move(pos[0], pos[1], dim[0], dim[1], board))
