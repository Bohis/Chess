from constant import *

class Move:
    def __init__(self, value: str):
        if type(value) != str:
            raise TypeError("value is not str")
        
        if len(value) != 4:
            raise ValueError("This value not is correct chess move")
        
        start_letter, start_digit, end_letter, end_digit = value
        
        if not (start_letter+end_letter).isalpha():
            raise ValueError("This value not is correct chess move")
        
        if not (start_digit+end_digit).isdigit():
            raise ValueError("This value not is correct chess move")
        
        self._value = value
        self._start_pos = self._convert_chess_pos_to_index(value[:2])
        self._end_pos = self._convert_chess_pos_to_index(value[2:])
        
    @property
    def value(self) -> str:
        return self._value
    
    @property
    def start_pos(self) -> tuple[int,int]:
        return self._start_pos
    
    @property
    def end_pos(self) -> tuple[int,int]:
        return self._end_pos
        
    def _convert_chess_pos_to_index(self, chess_pos:str)->tuple[int,int]:
        if len(chess_pos) != 2:
            raise ValueError("Incorrect letter")
        
        letter, number = chess_pos[0], int(chess_pos[1])
        
        if not (ord("a") <= ord(letter) <= ord("h")+1):
            raise ValueError("Incorrect letter")
        if not (1 <= number <= BOARD_SIZE):
            raise ValueError("Incorrect number")
        
        row = BOARD_SIZE - number
        column = ord(letter) - ord("a")
        
        return (row, column)
    
    def __str__(self) -> str:
        return f"{self._value} start_pos: {self._start_pos}, end_pos: {self._end_pos}"
    

if __name__ == "__main__":
    pos = Move("e2e4")
    print(pos)
            
    
        
