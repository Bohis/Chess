from __future__ import annotations
from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from chess_desk import Chess_desk
from constant import *
from .abstract_figure import Abstract_figure


class Pawn(Abstract_figure):
    def __init__(self, color: Literal["W","B"]):
        Abstract_figure.__init__(self,"p", color)
        
    def can_move(self, chess_desk: Chess_desk, start_pos: tuple[int,int], end_pos: tuple[int,int]) -> bool:
        delta_row = end_pos[0] - start_pos[0]
        delta_column =  end_pos[1] - start_pos[1]
        
        if abs(delta_column) > 1:
            return False
        
        if delta_row == 0:
            return False
        
        if abs(delta_row) > 2:
            return False
           
        if abs(delta_row) == 2 and delta_column != 0:
            return False
        
        if delta_column == 0 and chess_desk.get_cell(*end_pos).is_contains_figure:
            return False
        
        if delta_column != 0 and chess_desk.get_cell(*end_pos).is_empty:
            return False
        
        if self._color == BLACK:
            if delta_row < 0:
                return False
         
            if delta_row == 2 and start_pos[0] != 1:
                return False
        
            return True
        else:
            if delta_row > 0:
                return False
         
            if delta_row == -2 and start_pos[0] != 6:
                return False
        
            return True
            