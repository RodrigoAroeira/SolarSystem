from vpython import color, vector
from Assets import Body

class CenterMass(Body):
    """ CenterMass class """

    def __init__(self, pos: vector, radius: float) -> None:
        super().__init__(0, radius)
        self.pos = pos
        self.radius = radius

    def create(self):
        return super().create(color = color.green,
                              emissive = True,
                              trail_type = 'points')