from cell import Cell
from constant import *
from figures import *
from move import Move

class Chess_desk:
    def __init__(self, fen : str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self._board = None
        self._move_now = None
        self._move_amount = 0
        self._half_move_amount = 0
        self._castling_white = ""
        self._castling_black = ""
        self._dict_of_figure = {"p": Pawn, "n":Knight, "r": Rook, "b":Bishop, "k":King, "q":Queen}
        self._fall_white = []
        self._fall_black = []
        
        self._create_cells()
        self._fill_desk_from_fen(fen)
        

    def _create_cells(self) -> None:
        self._board = [[Cell(WHITE if row % 2 == column % 2 else BLACK, row, column) for column in range(BOARD_SIZE)]\
            for row in range(BOARD_SIZE)]
        
    def _fill_desk_from_fen(self, fen:str):
        try:
            position_figures, move, castling, captures_on_passage, half_move_amount, move_amount = fen.split()
            
            row = 0
            column = 0
            
            if move.upper() in [WHITE, BLACK]:
                self._move_now = move.upper()
            else:
                raise ValueError("move color is incorect")
            
            if half_move_amount.isdigit():
                self._half_move_amount = int(half_move_amount)
            else:
                raise ValueError("half move amount color is incorect")
            
            if move_amount.isdigit():
                self._move_amount = int(move_amount)
            else:
                raise ValueError("move amount color is incorect")
            
            if 2 <= len(castling) <= 4:
                self._castling_black = "".join(filter(lambda c: c.islower(), castling))
                self._castling_white = "".join(filter(lambda c: c.isupper(), castling))
            else:
                raise ValueError("castling is incorect")
                
            
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
    
    def can_move(self, move: Move) -> bool:
        try:
            start_cell = self.get_cell(*move.start_pos)
            end_cell = self.get_cell(*move.end_pos)
            
            if start_cell.is_empty:
                return False

            if start_cell.figure.color != self._move_now:
                return False
            
            if end_cell.is_contains_figure and end_cell.figure.color == start_cell.figure.color:
                return False
            
            return start_cell.figure.can_move(self, move)
        except Exception as error:
            print(f"Error move {error}")
            return False
        
    def move(self, move: Move) -> bool:
        if not self.can_move(move):
            return
        
        start_cell = self.get_cell(*move.start_pos)
        end_cell = self.get_cell(*move.end_pos)
        
        if end_cell.figure != None:
            
            if end_cell.figure.color == WHITE:
                self._fall_white.append(end_cell.figure.color)
            else:
                self._fall_black.append(end_cell.figure.color)
                
            end_cell.figure = None
            
        end_cell.figure = start_cell.figure
        start_cell.figure = None

        end_cell.figure.figure_move()

        self._half_move_amount += 1
        
        if self._move_now == WHITE:
            self._move_now = BLACK
        else:
            self._move_now = WHITE
            self._move_amount += 1
            
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
    moves = ["e2e4","e7e5","g1f3","b8c6","f1c4","g8f6","d2d3","f8c5","c2c3","d7d6","b1d2","c8g4","h2h3","g4h5"]
    
    while True:
        print(board)

        #position = input("enter your move: ")
        
        position = moves.pop(0)
        print(position)
        
        try:
            move = Move(position)
        except Exception as error:
            print(error)
            continue
        
        if not board.can_move(move):
            print("incorect move")
            continue
        
        board.move(move)
        
        if len(moves) == 0:
            break
    