from pygl.math import *

POINTS = 0  # 已实现
LINES = 1
LINE_STRIP = 2
TRIANGLES = 3
TRIANGLES_STRIP = 4


class Model:
    vertexes = []  # 此为储存顶点数据的容器，每一个元素都要是Vertex类型
    position = None
    disPlayType = None
    pointSize = 1

    def __init__(self, position, vertexes, displayType):
        """
            参数：
                position        代表模型在世界中的位置
                vertexes        请注意格式：每一个元素都是一列表，每一个列表都有三个值，依次代表x y z。格式错误将不会添加vertex。
                displayType     这个代表显示图元的类型，至于每个代表什么，您可以自己带入看看，或借鉴一下OpenGL，因为pygl的命名借用的就是OpenGL的命名
        """

        if type(position) != Vertex3:
            logs(ERROR, "你的position参数不可以使用除了Vertex以外的类型传入此函数")
            return
        else:
            self.position = position

        for i in vertexes:
            if type(i) != Vertex3:
                logs(ERROR, "你的vertex参数中的元素的类型不可以使用除了Vertex以外的类型传入此函数")
                return
            else:
                self.vertexes.append(i)

        self.disPlayType = displayType

    def set_pointSize(self, pointSize):
        if type(pointSize) != int:
            logs(ERROR, "你的pointSize不可以使用除了int以外的类型传入此函数")
            return False
        else:
            self.pointSize = pointSize
            return True
