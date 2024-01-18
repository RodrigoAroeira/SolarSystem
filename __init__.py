from os import system
from Assets import *

from Assets.Objects.System import G


def _example():
    
    star1 = Star(2e30, 1e10, vector(0, 0, 0), vector(0, 0, 0))

    planet1 = Planet(5e24, 1e9, vector(0, 0, 0), vector(0,0,0))

    planet1.vel = sqrt(G * star1.mass / planet1.pos.mag) * vector(0, 1, 0)

    system = System([star1, planet1], viewVectors=True)

    system.start()