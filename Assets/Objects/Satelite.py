from Assets import Body, Planet
from dataclasses import dataclass, field
from vpython import color

@dataclass
class Satelite(Body):

    """ Satelite class """

    parent: Planet = field(repr=False)

    def __post_init__(self):
        raise NotImplementedError('Satelites are not yet implemented')


    def create(self) -> None:
        return super().create(color = color.white)