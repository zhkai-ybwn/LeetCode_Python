from typing import List


def sub_rectangle_queries_test():
    """
    测试方法
    :return: 无返回
    """
    sub_rectangle_queries = SubRectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    result = sub_rectangle_queries.get_value(0, 2)
    print(result)
    sub_rectangle_queries.update_sub_rectangle(0, 0, 3, 2, 5)
    print(sub_rectangle_queries.data)


class SubRectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.data = rectangle

    def update_sub_rectangle(
            self,
            row1: int,
            col1: int,
            row2: int,
            col2: int,
            new_value: int):
        """
        用 newValue 更新以(row1,col1)为左上角且以(row2,col2)为右下角的子矩形。
        :param self:
        :param row1: 子矩形左上角行坐标
        :param col1:子矩形左上角列坐标
        :param row2:子矩形右下角行坐标
        :param col2:子矩形右下角列坐标
        :param new_value:子矩形新值
        """
        if self.data is not None:
            for i in range(row1, row2 + 1):
                for j in range(col1, col2 + 1):
                    self.data[i][j] = new_value

    def get_value(self, row, col) -> int:
        """
        回矩形中坐标(row,col)的当前值
        :param self:
        :param row: 行坐标
        :param col: 列坐标
        :return: 当前值
        """
        if self.data is not None:
            return self.data[row][col]
        else:
            return -1
