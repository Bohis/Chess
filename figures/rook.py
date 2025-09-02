from __future__ import annotations
from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from chess_desk import Chess_desk
from constant import *
from .abstract_figure import Abstract_figure


class Rook(Abstract_figure):
    def __init__(self, color: Literal["W","B"]):
        Abstract_figure.__init__(self,"r", color)
        
    def can_move(self, chess_desk: Chess_desk, start_pos: tuple[int,int], end_pos: tuple[int,int]) -> bool:
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