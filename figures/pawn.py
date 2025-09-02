from __future__ import annotations
from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from chess_desk import Chess_desk
from constant import *
from abstract_figure import Abstract_figure

class Pawn(Abstract_figure):
    def __init__(self, color: Literal["W","B"]):
        Abstract_figure.__init__(self,"p", color)
        
    def can_move(self, chess_desk: Chess_desk, start_pos: tuple[int,int], end_pos: tuple[int,int]) -> bool:
        return True