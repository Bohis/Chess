from __future__ import annotations
from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from chess_desk import Chess_desk
from constant import *
from move import Move
from .abstract_figure import Abstract_figure


class Knight(Abstract_figure):
    def __init__(self, color: Literal["W","B"]):
        Abstract_figure.__init__(self,"n", color)
        
    def can_move(self, chess_desk: Chess_desk, move: Move) -> bool:
        start_pos = move.start_pos
        end_pos = move.end_pos
        
        delta_row = end_pos[0] - start_pos[0]
        delta_column =  end_pos[1] - start_pos[1]
        
        if abs(delta_row) == 2 and abs(delta_column) == 1 or abs(delta_column) == 2 and abs(delta_row) == 1:
            return True
        
        return False
    
    def get_current_move(self, chess_desk: Chess_desk, start_pos: tuple[int,int]) -> list[tuple[int,int]]:
        offsets = [(-2,1),(-2,-1),
                   (2,1),(2,-1),
                   (1,2),(-1,2),
                   (1,-2),(-1,-2)]
        
        correct_moves = []
        
        for offset in offsets:
            end_pos = (offset[0]+start_pos[0], offset[1] + start_pos[1])
            
            if not chess_desk._is_correct_index(end_pos[0]) or\
                not chess_desk._is_correct_index(end_pos[1]):
                    continue
            
            if chess_desk.get_cell(*end_pos).figure != None and chess_desk.get_cell(*end_pos).figure.color == self._color:
                continue
            
            if not self.can_move(chess_desk, start_pos, end_pos):
                continue
            
            correct_moves.append(end_pos)

        return correct_moves
                