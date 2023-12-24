from ..Exceptions import BodyNotInitializedException
from dataclasses import dataclass
from vpython import arrow, vector


@dataclass
class Vector:

    """ Arrow class """

    pos: vector
    axis: vector
    color: vector

    _init = False

    def create(self):
        self.obj = arrow(pos = self.pos, axis = self.axis, color = self.color)
    
    def update(self, axis: vector):
        self.obj.axis = axis
        self.obj.pos = self.pos
    
    def delete(self):
        if not self._init:
            raise BodyNotInitializedException