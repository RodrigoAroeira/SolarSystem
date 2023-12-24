from vpython import vector, sphere, textures
from dataclasses import dataclass
from Objects import Body

@dataclass
class Planet(Body):

    pos: vector
    texture: str = textures.earth

    def __post_init__(self):
        super().__post_init__()
        if self.texture not in textures.__dict__.values() or not self.texture.endswith('.jpg'):
            print('Invalid texture, using default')

    def create(self) -> None:
        return super().create(texture = self.texture)