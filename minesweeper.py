from random import sample
from pprint import pprint


class Cell:
    
    def __init__(self, mines_around=0):
        self.mines_around = mines_around
        self.__is_pressed = False
    
    def __repr__(self):
        return "C" if self.__is_pressed else f"{self.mines_around}"


class Mine:    
    def __repr__(self):
        return "M"
    

class GameBoard:
    
    def __init__(self, x=10, y=10, mines_count=8):
        
        self.__x = x
        self.__y = y
        self.__mines_count = mines_count
    
    def create_mines_list(self):
        #create a list NxM and choice sublist with corresponding mine indexes
        
        tmp = [self.__x * i + j for i in range(self.__x) for j in range(self.__y)]
        return sample(tmp, self.__mines_count)
    
    def create_pole(self):
        #create game pole
        
        pole = [[Cell(mines_around=0) for _ in range(self.__x)] for _ in range(self.__y)]
        mines = self.create_mines_list()
        
        def _get_indexes_to_increment_mines_count(self, mine_index):
            y = mine_index // self.__y
            x = mine_index - self.__y * y 
            if y == 0:           
                if x == 0:
                    return [ mine_index + 1, mine_index + self.__x, mine_index + self.__x + 1 ]
                elif x + 1 == self.__x:
                    return [ mine_index - 1, mine_index + self.__x - 1, mine_index + self.__x ]
                return [mine_index - 1, mine_index + 1, self.__x + mine_index - 1, self.__x + mine_index, self.__x + mine_index + 1]
            elif y == self.__y - 1:    
                if x == 0:
                    return [ mine_index - self.__x, mine_index - self.__x + 1, mine_index + 1 ]
                elif x + 1 == self.__x:
                    return [ mine_index - self.__x - 1, mine_index - self.__x, mine_index - 1]
                return [mine_index - self.__x - 1, mine_index - self.__x, 
                        mine_index - self.__x + 1, mine_index - 1, mine_index + 1 ]
            elif x == 0:
                return [ mine_index - self.__x, mine_index - self.__x + 1, mine_index + 1,
                        mine_index + self.__x, mine_index + self.__x + 1 ]
            elif x == self.__x - 1:
                return [ mine_index - self.__x - 1, mine_index - self.__x, mine_index - 1,
                        mine_index + self.__x - 1, mine_index + self.__x]
            return [mine_index - self.__x - 1, mine_index - self.__x, mine_index - self.__x + 1,
                    mine_index - 1, mine_index + 1, mine_index + self.__x - 1, mine_index + self.__x,
                    mine_index + self.__x + 1]
    
        for index in mines: 
            pole[index // self.__y][index - self.__y * (index // self.__y)] = Mine()
            for cell in _get_indexes_to_increment_mines_count(self, index):
                Cell_y = cell // self.__y
                Cell_x = cell - self.__y * Cell_y
                if isinstance(pole[Cell_y][Cell_x], Cell):
                    pole[Cell_y][Cell_x].mines_around += 1
        return pole
        
g = GameBoard(x=20, y=20, mines_count=30)
pprint(g.create_pole())
        