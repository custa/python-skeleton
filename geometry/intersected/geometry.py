import numpy as np
from enum import Enum, unique


@unique
class Direction(Enum):
    """ 进出方向 """
    ENTRY = "ENTRY"
    EXIT = "EXIT"
    PENDING = "PENDING"


# 点
class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y


# 向量
class Vector(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.x = end.x - start.x
        self.y = end.y - start.y


def negative(v):
    """ 向量取反 """
    return Vector(v.end, v.start)


def cross_product(va, vb):
    """ 向量叉积 """
    # np.cross([va.x, va.y], [vb.x, vb.y]) 结果为 int32，可能导致整数溢出
    # 这里改为直接计算，缺点是只能计算两个向量的叉积，不能计算向量组
    return va.x * vb.y - va.y * vb.x


def intersected(a, b, c, d):
    """ 判断 a->b、c->d 两个线段是否相交 """
    ac = Vector(a, c)
    ad = Vector(a, d)
    bc = Vector(b, c)
    bd = Vector(b, d)
    ca = negative(ac)
    cb = negative(bc)
    da = negative(ad)
    db = negative(bd)

    c1 = cross_product(ac, ad)
    c2 = cross_product(bc, bd)
    c3 = cross_product(ca, cb)
    c4 = cross_product(da, db)

    # https://segmentfault.com/a/1190000004457595
    return (c1 * c2 <= 0) and (c3 * c4 <= 0)


def collinear(a, b, p):
    """ a b p 三点是否共线 """
    ap = Vector(a, p)
    ab = Vector(a, b)
    return cross_product(ap, ab) == 0


def on_line_segment(a, b, p):
    """ 判断 p 是否在 a->b 线段上 """
    # 先判断 a p b 三点是否共线
    if not collinear(a, b, p):
        return False
    # p 是否在 a-b 为对角线的矩形内
    return (min(a.x, b.x) <= p.x <= max(a.x, b.x)) if a.x != b.x else (
        min(a.y, b.y) <= p.y <= max(a.y, b.y))


def entry_or_exit(start, end, previous, current):
    """
    start->end 表示有向边界线，start 在上 end 在下，如果 previous 从边界线左侧穿到右侧 current 表示出，反之表示进

    Parameters
    ----------
    start: Point
        边界线起点
    end: Point
        边界线终点
    previous: Point
        上次位置
    current: Point
        当前位置

    Returns
    -------
        进出方向
    """

    # 如果当前位置在边界线上，无法判断
    if collinear(start, end, current):
        return Direction.PENDING

    # 如果移动线路 previous->current 跟边界线 start->end 没有交叉，只在边界线一侧移动
    if not intersected(start, end, previous, current):
        return Direction.PENDING

    # 注意图像坐标系 y 轴向下，所以向量旋转顺、逆时针方向与一般坐标系相反
    #
    # previous->current 顺时针旋转到 start->end 方向的角度小于 180 度
    # 即 previous 从左侧穿过 start->end 到右侧 current
    # 表示出
    if cross_product(Vector(start, end), Vector(previous, current)) < 0:
        return Direction.EXIT
    else:
        return Direction.ENTRY


# plt.figure()
# plt.plot([p_.x for p_ in p], [p_.y for p_ in p], "ro")
# plt.plot([p[0].x, p[1].x], [p[0].y, p[1].y])
# plt.plot([p[2].x, p[3].x], [p[2].y, p[3].y])
# plt.show()
#
# print(is_intersected(*p))
#
# print(on_line_segment(p[2], p[3], p[1]))
# print(on_line_segment(Point(5, 12), Point(5, 25), Point(5, 15)))

if __name__ == "__main__":
    a = Point(0, 0)
    b = Point(2, 2)
    c = Point(0, 2)
    d = Point(1, 1)
    print(entry_or_exit(a, b, c, d))

    a = Point(3, 1)
    b = Point(3, 10)
    c = Point(1, 1)
    d = Point(5, 5)
    print(entry_or_exit(a, b, c, d))

    a = Point(0, 0)
    b = Point(1, 1)
    c = Point(1, 3)
    d = Point(3, 1)
    print(entry_or_exit(a, b, c, d))

    a = Point(2, 2)
    b = Point(2, 2)
    c = Point(1, 3)
    d = Point(3, 1)
    print(entry_or_exit(a, b, c, d))

    a = Point(0, 0)
    b = Point(1920, 1080)
    c = Point(0, 500)
    d = Point(500, 0)
    print(entry_or_exit(a, b, c, d))
