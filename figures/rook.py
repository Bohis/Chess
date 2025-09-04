from __future__ import annotations
from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from chess_desk import Chess_desk
from constant import *
from move import Move
from .abstract_figure import Abstract_figure


class Rook(Abstract_figure):
    def __init__(self, color: Literal["W","B"]):
        Abstract_figure.__init__(self,"r", color)
        
    def can_move(self, chess_desk: Chess_desk, move: Move) -> bool:
        start_pos = move.start_pos
        end_pos = move.end_pos
        
        delta_row = end_pos[0] - start_pos[0]
        delta_column =  end_pos[1] - start_pos[1]
        
        if delta_row != 0 and delta_column != 0:
            return False
        
        step_row = self._sign(delta_row)
        step_column = self._sign(delta_column)
        
        row,column = start_pos
        
        row += step_row
        column += step_column
            
        while (row, column) != end_pos:
            if chess_desk.get_cell(row,column).is_contains_figure:
                return False

            row += step_row
            column += step_column
            
        return True
    
    def get_current_move(self, chess_desk: Chess_desk, start_pos: tuple[int,int]) -> list[tuple[int,int]]:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        correct_moves = []
        
        for direction in directions:
            
            pos_row, pos_column = start_pos
            
            while True:
                
                pos_row += direction[0]
                pos_column += direction[1]
                
                if chess_desk.get_cell(pos_row, pos_column).figure != None and chess_desk.get_cell(pos_row, pos_column).figure.color == self._color:
                    break
                
                if not (chess_desk._is_correct_index(pos_row) and chess_desk._is_correct_index(pos_column)):
                    break
                
                if self.can_move(chess_desk, start_pos, (pos_row, pos_column)):
                    break
            
                correct_moves.append((pos_row, pos_column))

        return correct_moves