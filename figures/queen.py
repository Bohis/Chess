from __future__ import annotations
from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from chess_desk import Chess_desk
from constant import *
from move import Move
from .abstract_figure import Abstract_figure
from .rook import Rook
from .bishop import Bishop


class Queen(Bishop, Rook):
    def __init__(self, color: Literal["W","B"]):
        Abstract_figure.__init__(self,"q", color)
        
    def can_move(self, chess_desk: Chess_desk, move: Move) -> bool:
        return Bishop.can_move(self, chess_desk, move) or Rook.can_move(self, chess_desk, move)
    
    def get_current_move(self, chess_desk: Chess_desk, start_pos: tuple[int,int]) -> list[tuple[int,int]]:
        return Bishop.get_current_move(self, chess_desk, start_pos) + Rook.can_move(self, chess_desk, start_pos)