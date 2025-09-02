from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from chess_desk import Chess_desk
from constant import *
from abstract_figure import Abstract_figure

class Cell:
    def __init__(self, color:Literal["W","B"], index_row:int, index_column:int):
        self._color = color
        self._index_row = index_row
        self._index_column = index_column
        self._figure = None    
    
    @property
    def figure(self):
        return self._figure
    
    @figure.setter
    def figure(self, new_figure: Abstract_figure) -> None:
        if new_figure == None:
            self._figure = None
            return
        
        if not isinstance(new_figure, Abstract_figure):
            raise ValueError("new_figure must be figure sub class Abstract_figure")
        
        if self.is_contains_figure:
            raise ValueError("cell already contains figure")
        
        self._figure = new_figure
        
    @property
    def is_empty(self)->bool:
        return self._figure == None
    
    @property
    def is_contains_figure(self)->bool:
        return self._figure != None
    
    @property
    def color(self):
        return self._color
    
    @property
    def index_row(self):
        return self._index_row
    
    @property
    def index_column(self):
        return self._index_column
    
    def __str__(self) -> str:
        
        if self.is_empty:
            return  "▢" if self._color == BLACK else "◼"
        else:
            return str(self._figure)


