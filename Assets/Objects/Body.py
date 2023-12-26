from dataclasses import dataclass
from typing import Any

from Assets import Vector, BodyNotInitializedException
from vpython import vector, sphere

@dataclass
class Body:

    """ Base class for celestial bodies """

    mass: float
    radius: float

    _init = False

    def __post_init__(self):
        self.arrowFg: Vector
        self.arrowP: Vector
        
        self._startVel = vector(0, 0, 0)
        self._startPos = vector(0, 0, 0)

        self.__vel = vector(0, 0, 0)
        self.__pos = vector(0, 0, 0)
        self.__p = vector(0, 0, 0)
        self.__Fg = vector(0, 0, 0)

    def __setattr__(self, __name: str, __value: Any) -> None:
        pass

    def create(self, **kwargs):
        if not self._init:
            self.obj = sphere(
                pos = self.pos,
                radius = self.radius,
            )

    def delete(self):
        if not self._init:
            raise BodyNotInitializedException

        self.obj.visible = False
        self.obj.delete()
        self._init = False
        del self.obj

    @property
    def vel(self):
        return self.__vel
    
    @vel.setter
    def vel(self, value: vector):
        if not self._startVel.mag and value.mag:
            self._startVel = value  
        self.__vel = value
    
    @property
    def pos(self):
        return self.__pos
    
    @pos.setter
    def pos(self, value: vector):
        if not self._startPos.mag and value.mag:
            self._startPos = value
        self.__pos = value

    @property
    def p(self):
        return self.__p
    
    @p.setter
    def p(self, value: vector):
        self.__p = value

    @property
    def Fg(self):
        return self.__Fg
    
    @Fg.setter
    def Fg(self, value: vector):
        self.__Fg = value

