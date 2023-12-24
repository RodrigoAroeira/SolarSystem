from vpython import vector, sphere
from dataclasses import dataclass
from Objects import Body


@dataclass
class Star(Body):

    """ Star class """

    pos: vector
    vel: vector
    color: vector

    def create(self):
        return super().create(color = self.color,
                              emissive = True,
                              trail_type = 'points')