from __future__ import annotations
from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from chess_desk import Chess_desk
from constant import *
from abstract_figure import Abstract_figure

class Knight(Abstract_figure):
    def __init__(self, color: Literal["W","B"]):
        Abstract_figure.__init__(self,"n", color)
        
    def can_move(self, chess_desk: Chess_desk, start_pos: tuple[int,int], end_pos: tuple[int,int]) -> bool:
        delta_row = end_pos[0] - start_pos[0]
        delta_column =  end_pos[1] - start_pos[1]
        
        if abs(delta_row) == 2 and abs(delta_column) == 1 or abs(delta_column) == 2 and abs(delta_row) == 1:
            return True
        
        return False