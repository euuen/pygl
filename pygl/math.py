from pygl.logs import *


class Vertex2:
    x, y = 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vertex3:
    x, y, z = 0, 0, 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Vertex4:
    x, y, z, w = 0, 0, 0, 0

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def v3_to_v4(self, vertex: Vertex3):
        if type(vertex) != Vertex3:
            logs(ERROR, "你的vertex参数不可以使用除Vertex3以外的类型传入此函数")
            return False
        else:
            self.x = vertex.x
            self.y = vertex.y
            self.z = vertex.z
            self.w = 1
            return True


class Matrix:
    value = [
        Vertex4(0, 0, 0, 0),
        Vertex4(0, 0, 0, 0),
        Vertex4(0, 0, 0, 0),
        Vertex4(0, 0, 0, 0)
    ]

    def __init__(self, matrix: list):
        if len(matrix) != 4:
            logs(ERROR, "你的矩阵格式不对")

        self.value = matrix


def ver_mul_ver(vertexA: Vertex4, vertexB: Vertex4):
    return vertexA.x * vertexB.x + vertexA.y * vertexB.y + vertexA.z * vertexB.z + vertexA.w * vertexB.w


def mat_mul_ver(matrix: Matrix, vertex: Vertex4) -> Vertex4:
    _vertex = Vertex4(
        matrix.value[0].x,
        matrix.value[1].x,
        matrix.value[2].x,
        matrix.value[3].x
    )
    x = ver_mul_ver(_vertex, vertex)

    _vertex = Vertex4(
        matrix.value[0].y,
        matrix.value[1].y,
        matrix.value[2].y,
        matrix.value[3].y
    )
    y = ver_mul_ver(_vertex, vertex)

    _vertex = Vertex4(
        matrix.value[0].z,
        matrix.value[1].z,
        matrix.value[2].z,
        matrix.value[3].z
    )
    z = ver_mul_ver(_vertex, vertex)

    _vertex = Vertex4(
        matrix.value[0].w,
        matrix.value[1].w,
        matrix.value[2].w,
        matrix.value[3].w
    )
    w = ver_mul_ver(_vertex, vertex)

    return Vertex4(x, y, z, w)


def mat_mul_mat(matrixA: Matrix, matrixB: Matrix):
    vertex1 = mat_mul_ver(matrixA, matrixB.value[0])
    vertex2 = mat_mul_ver(matrixA, matrixB.value[1])
    vertex3 = mat_mul_ver(matrixA, matrixB.value[2])
    vertex4 = mat_mul_ver(matrixA, matrixB.value[3])
    res = [vertex1, vertex2, vertex3, vertex4]
    return Matrix(res)


def translate(vertex: Vertex3):
    res = Matrix([
        Vertex4(1, 0, 0, 0),
        Vertex4(0, 1, 0, 0),
        Vertex4(0, 0, 1, 0),
        Vertex4(vertex.x, vertex.y, vertex.z, 1)
    ])
    return res
