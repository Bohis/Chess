from cell import Cell
from constant import *
from figures import *

class Chess_desk:
    def __init__(self, fen : str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self._board = None
        self._create_cells()
        self._dict_of_figure = {"p": Pawn, "n":Knight, "r": Rook, "b":Bishop, "k":King, "q":Queen}
        self._fill_desk_from_fen(fen)

    def _create_cells(self) -> None:
        self._board = [[Cell(WHITE if row % 2 == column % 2 else BLACK, row, column) for column in range(BOARD_SIZE)]\
            for row in range(BOARD_SIZE)]
        
    def _fill_desk_from_fen(self, fen:str):
        try:
            position_figures, move, castling, captures_on_passage, half_move_amount, move_amount = fen.split()
            
            row = 0
            column = 0
            
            for line in position_figures.split("/"):
                for c in line:
                    if c.isdigit():
                        column += int(c)
                        continue
                    
                    self._board[row][column].figure = self._dict_of_figure[c.lower()](WHITE if c.isupper() else BLACK)
                    column += 1
                row += 1
                column = 0
                    
            
        except Exception as error:
            raise ValueError(f"fen is not correct: {error}")
        
    def _is_correct_index(self, index):
        return 0<=index<BOARD_SIZE
        
    def get_cell(self, row:int, column:int)->Cell:
        if not self._is_correct_index(row) or not self._is_correct_index(column):
            raise ValueError("this indexes not correct")
        
        return self._board[row][column]
    
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
            
    
    def can_move(self, from_cell:str,to_cell:str) -> bool:
        try:
            from_index = self._convert_chess_pos_to_index(from_cell)
            to_index = self._convert_chess_pos_to_index(to_cell)

            start_cell = self.get_cell(*from_index)
            end_cell = self.get_cell(*to_index)
            
            if start_cell.is_empty:
                return False
            
            if end_cell.is_contains_figure and end_cell.figure.color == start_cell.figure.color:
                return False
            
            return start_cell.figure.can_move(self, from_index, to_index)
        except:
            return False
        
        
    def move(self, from_cell:str, to_cell:str) -> bool:
        if not self.can_move(from_cell, to_cell):
            return
        
        from_index = self._convert_chess_pos_to_index(from_cell)
        to_index = self._convert_chess_pos_to_index(to_cell)
        
        self._board[to_index[0]][to_index[1]].figure = self._board[from_index[0]][from_index[1]].figure
        self._board[from_index[0]][from_index[1]].figure = None
            
    def __str__(self):
        result = ""
        
        def add_letter_line():
            result = ""
            for letter_code in range(ord("a"), ord("h")+1):
                result += chr(letter_code) + " "
            return result
        
        result += f"  {add_letter_line()}\n"
        
        for row in range(BOARD_SIZE):
            result += f"{BOARD_SIZE - row} "
            for column in range(BOARD_SIZE):
                result += str(self._board[row][column]) + " "

            result += f"{BOARD_SIZE - row}\n"
        
        result += f"  {add_letter_line()}\n"
        
        return result
    

if __name__ == "__main__":
    board = Chess_desk()
    
    while True:
        print(board)

        from_pos,to_pos = input("enter your move: ").split()
        
        if not board.can_move(from_pos, to_pos):
            print("incorect move")
            continue
        
        board.move(from_pos, to_pos)
    