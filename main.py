from pygl import *
from pygl import World


class Main:

    def __init__(self):
        world = World()
        vertexes = [
            Vertex3(1, 1, 1),
            Vertex3(1, 1, -1),
            Vertex3(1, -1, -1),
            Vertex3(1, -1, 1),

            Vertex3(-1, 1, 1),
            Vertex3(-1, 1, -1),
            Vertex3(-1, -1, -1),
            Vertex3(-1, -1, 1)
        ]
        model = Model(Vertex3(0, -2, 0), vertexes, POINTS)
        model.set_pointSize(10)

        world.add_model(model)
        camera = Camera(world, Vertex3(0, 0, 8), 600, 600, "pygl")


if __name__ == "__main__":
    Main()
