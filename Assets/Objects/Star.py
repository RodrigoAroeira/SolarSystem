from vpython import vector, color
from dataclasses import dataclass
from Assets import Body


@dataclass
class Star(Body):

    """ Star class """

    pos: vector
    vel: vector
    color: vector = color.yellow

    def create(self):
        return super().create(color = self.color,
                              emissive = True,
                              trail_type = 'points')