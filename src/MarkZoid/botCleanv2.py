'''
Created on Jun 27, 2013

Problem: https://www.hackerrank.com/challenges/botcleanv2
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



'''
Takes in two points on the grid and returns the set of moves required based on the shortest path algorithm
@param x: Bot co-ordinates on the grid - x
@param y: Bot co-ordinates on the grid - y
@param grid: the matrix

@return: the next step for the bot to move 
'''
def next_move(x, y, grid):
    bot = x, y
    dirtyCells = getVisibleCordinates(x, y, 5, grid);
    
    if bot == None or dirtyCells == None: 
        return None;
    
    if dirtyCells.__len__() == 0:
        # tell where to move next
        if x < 4:
            return Moves.DOWN;
        elif y < 4:
            return Moves.RIGHT;
        if x > 0: 
            return Moves.UP;
        elif y > 0:
            return Moves.LEFT; 
        
    bot_x, bot_y = x, y;
    princess_x, princess_y = dirtyCells[0];
    
    
    if bot_x == princess_x and bot_y == princess_y:
        return Moves.CLEAN;
        
    
    # Case 1: Same column, move rows
    elif bot_y == princess_y:
        if bot_x < princess_x:
            return Moves.DOWN;
        elif bot_x > princess_x:
            return Moves.UP;
    
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
@param x: x coordinate of the bot
@param y: y coordinate of the bot
@param n: Number of rows and columns in the grid
@param grid: character array containing the placements of the bot and the princess.
@return: co-ordinates of dirty cells visible in the immediate neighbourhood for the bot 
'''  
def getVisibleCordinates(x, y, n, grid):
    'basic input validation'
    if n < 1 or grid == None:
        return None;
    elif n == 1:
        return Moves.NONE;
    bot = (x, y);
    dirtyCells = [];

    if grid[x][y] == 'd':
        dirtyCells.append((x, y));
        
    if y - 1 >= 0:
            if grid[x][y - 1] == 'd':
                dirtyCells.append((x, y - 1));    
    if y + 1 < (n - 1):
            if grid[x][y + 1] == 'd':
                dirtyCells.append((x, y + 1));
                
    if x - 1 >= 0:
        if y - 1 >= 0:
            if grid[x - 1][y - 1] == 'd':
                dirtyCells.append((x - 1, y - 1));
        if y + 1 < (n - 1):
            if grid[x - 1][y + 1] == 'd':
                dirtyCells.append((x - 1, y + 1));
        if grid[x - 1][y] == 'd':
            dirtyCells.append((x - 1, y));
                
    if x + 1 < (n - 1):
        if y - 1 >= 0:
            if grid[x + 1][y - 1] == 'd':
                dirtyCells.append((x + 1, y - 1));
        if y + 1 < (n - 1):
            if grid[x + 1][y + 1] == 'd':
                dirtyCells.append((x + 1, y + 1));
        if grid[x + 1][y] == 'd':
            dirtyCells.append((x + 1, y));
            
    return dirtyCells;           
                    
        
    
    
    
# Tail starts here
# Tail starts here
if __name__ == "__main__":
    dirtyCells = []
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], board))
