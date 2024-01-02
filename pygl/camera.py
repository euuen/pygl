import pygl.world
import pygl.model
import math
from pygl.math import *
from tkinter import Tk, Canvas


class Camera:
    position = None  # 当前相机坐标，是Vertex类型
    viewField = math.pi / 3
    znear = 0.1
    zfar = 1000

    world = None
    window = None
    canvas = None
    frameLimits = math.pi / 3
    isShouldClose = False
    width, height = None, None

    def __init__(self, world: pygl.world.World, position: pygl.model.Vertex3, width, height, title="pygl"):
        self.world = world
        self.position = position
        self.window = Tk()
        self.window.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.window, width=width, height=height)
        self.canvas.pack()
        self.window.title(title)
        self.width, self.height = width, height

        self.window.after(int(1000/self.frameLimits), self.display)

        self.window.mainloop()

    def set_world(self, world: pygl.world.World):
        if type(world) != pygl.world.World:
            logs(ERROR, "你的world参数不可以使用除了World以外的类型传入此函数")
            return False
        else:
            self.world = world
            return True

    def set_frameLimits(self, frameLimits):
        self.frameLimits = frameLimits

    def should_close(self):
        return self.isShouldClose

    def display(self):
        vmat = translate(
            Vertex3(
                -self.position.x,
                -self.position.y,
                -self.position.z
            )
        )
        q = 1 / math.tan(self.viewField / 2)
        A = q / (self.height / self.width)
        B = (self.znear + self.zfar) / (self.znear - self.zfar)
        C = (2 * self.znear * self.zfar) / (self.znear - self.zfar)
        pmat = Matrix(
            [Vertex4(A, 0, 0, 0),
             Vertex4(0, q, 0, 0),
             Vertex4(0, 0, B, -1),
             Vertex4(0, 0, C, 0)]
        )

        for model in self.world.models:
            if model.disPlayType == pygl.model.POINTS:
                res = []
                mmat = translate(model.position)
                pmv = mat_mul_mat(mat_mul_mat(pmat, mmat), vmat)
                for vertex in model.vertexes:
                    tempVertex = Vertex4(0, 0, 0, 0)
                    tempVertex.v3_to_v4(vertex)
                    _vertex = mat_mul_ver(pmv, tempVertex)
                    # 接下来进行透视处罚
                    w = _vertex.w
                    if _vertex.z/w > 1 or _vertex.z/w < -1:
                        continue
                    vertexRes = Vertex2(
                        _vertex.x / w,
                        _vertex.y / w
                    )
                    res.append(vertexRes)

                for i in res:
                    x = self.width / 2 + i.x * self.width / 2
                    y = self.height / 2 - i.y * self.height / 2  # 这里写成减号的原因是pygame的y轴是向下的，而非向上
                    # 缺少显示

                    self.canvas.create_rectangle(x, y, x+model.pointSize, y+model.pointSize, fill="red", outline="red")
