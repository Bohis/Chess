from __future__ import annotations
from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from chess_desk import Chess_desk
from constant import *
from .abstract_figure import Abstract_figure


class King(Abstract_figure):
    def __init__(self, color: Literal["W","B"]):
        Abstract_figure.__init__(self,"k", color)
        
    def can_move(self, chess_desk: Chess_desk, start_pos: tuple[int,int], end_pos: tuple[int,int]) -> bool:
        delta_row = end_pos[0] - start_pos[0]
        delta_column =  end_pos[1] - start_pos[1]
        
        if abs(delta_row) != abs(delta_column) and (delta_row == 0 or delta_column == 0):
            return True
        
        return False
        
        
        
    