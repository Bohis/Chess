from __future__ import annotations
from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from chess_desk import Chess_desk
from constant import *


class Abstract_figure:
    
    def __init__(self, name: str, color: Literal["W","B"]):
        
        if color not in [WHITE, BLACK]:
            raise ValueError("color must be equals W or B")
        
        self._color = color
        self._name = self._modify_name_figure_from_color(name,color)
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def color(self) -> Literal["W","B"]:
        return self._color
    
    def _sign(self, value: int):
        if value > 0:
            return 1
        elif value < 0:
            return -1
        else:
            return 0
    
    def _modify_name_figure_from_color(self,name:str, color: Literal["W","B"])->str:
        return name.lower() if color == BLACK else name.upper()
    
    def can_move(self, chess_desk: Chess_desk, start_pos: tuple[int,int], end_pos: tuple[int,int]) -> bool:
        return False
    
    def __str__(self):
        return self._name
    
    
    
    
    