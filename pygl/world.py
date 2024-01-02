import pygl.model
from pygl.logs import *


class World:
    isRightHand: bool = None  # 是否是右手坐标系
    models = []  # 储存模型的容器，每一个元素都是Model类型

    def __init__(self, isRightHand=True):
        """
            参数：
                isRightHand     此类型应该为布尔型，True代表右手坐标系，False代表左手坐标系
        """
        if type(isRightHand) != bool:
            logs(ERROR, "你的isRightHand参数不可以使用除了bool意外的类型传入此函数")
            logs(INFO, "由于参数类型错误，pygl将使用右手坐标系")
            self.isRightHand = True
        else:
            self.isRightHand = isRightHand

    def add_model(self, model: pygl.model.Model):
        """
            你可以用这个函数去添加你自己的模型
            此函数会返回布尔值来表示是否添加成功，如果是True则代表成功，反之则失败

            参数：
                model   此为你的模型，请注意，请使用pygl提供的Model类型传参，否则此函数会直接失败
            返回：
                True    此函数成功
                False   此函数失败
        """
        if type(model) != pygl.model.Model:
            logs(ERROR, "你的model参数的类型不可以使用除了model以外的类型传入此函数")
            return False
        else:
            self.models.append(model)
            return True

    def change_coord_system(self, isRightHand: bool):
        """
            你可以用这个函数去改变坐标系，你可以把他变成左手或右手坐标系
            参数：
                isRightHand     此类型应该为布尔型，True代表右手坐标系，False代表左手坐标系
            返回：
                True            此函数成功
                False           此函数失败
        """
        if type(isRightHand) != bool:
            logs(ERROR, "你的isRightHand参数不可以使用除了bool意外的类型传入此函数")
            return False
        else:
            self.isRightHand = isRightHand
            return True
