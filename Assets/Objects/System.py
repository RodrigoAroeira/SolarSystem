from Assets import Body, CenterMass, Arrow, SystemNotInitializedException
from dataclasses import dataclass
from vpython import vector


G = 6.67408e-11

@dataclass
class System:
    """ System class """

    bodies: list[Body]
    radius: float = .2e10
    
    viewVectors: bool = False

    __init = False

    def __post_init__(self):
        self.mass = sum([body.mass for body in self.bodies])
        self.CenterMass = CenterMass(self.Baricenter, self.mass)

    def add_body(self, body: Body):
        self.bodies.append(body)
        self.mass += body.mass
    
    @property
    def Baricenter(self):
        
        pos = vector(0, 0, 0)
        for body in self.bodies:
            pos += body.pos * body.mass

        return pos / self.mass

    def make_arrows(self):
        self.arrows = []
        nullVec = vector(0, 0, 0)
        for body in self.bodies:
            arrowFg = Arrow(body.pos, nullVec, vector(1,0,0))
            arrowP = Arrow(body.pos, nullVec, vector(0,1,0))

            self.arrows.extend([arrowFg, arrowP])

            body.arrowFg = arrowFg
            body.arrowP = arrowP

        for arrow in self.arrows:
            arrow.create()

    def start(self):
        if self.radius > 0:
            self.CenterMass.create()
        for body in self.bodies:
            body.p = body.mass * body.vel
            body.create()

        if self.viewVectors:
            self.make_arrows()

        self.__init = True

    def calculateFg(self):
        
        for body in self.bodies:
            body.Fg = vector(0, 0, 0)

        for i in range(len(self.bodies)):
            body = self.bodies[i]
            for ii in range(i + 1, len(self.bodies)):
                body2 = self.bodies[ii]
                r = body2.pos - body.pos
                Fg = (G * body.mass * body2.mass * r.norm()) / r.mag2
                body.Fg += Fg
                body2.Fg -= Fg

    def updateP(self, t):
        for body in self.bodies:
            body.p += body.Fg * t

    def updatePos(self, t):
        for body in self.bodies:
            body.pos += (body.p / body.mass) * t

        if self.viewVectors:
            self.updateArrow()

    def updateArrow(self):
        max_radius = max([body.radius for body in self.bodies])

        scale = max_radius * 4

        for body in self.bodies:
            body.arrowFg.update(body.pos, body.Fg * scale)
            body.arrowP.update(body.pos, body.p * scale/body.p.mag)


    def stop(self):
        if not self.__init:
            raise SystemNotInitializedException("System not initialized")
        
        if self.radius > 0:
            self.CenterMass.delete()
        for body in self.bodies:
            if not body._init:
                continue

            body.vel = body._startVel
            body.pos = body._startPos
            body.p = body.mass * body.vel

        if self.viewVectors:
            for arrow in self.arrows:
                arrow.delete()

        self.__init = False