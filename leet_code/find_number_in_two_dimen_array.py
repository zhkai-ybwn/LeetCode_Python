import time
from typing import List


def find_number_in_two_dimen_array_test():
    """
    测试方法
    :return: 无返回
    """
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 5
    start = time.perf_counter_ns()
    result = find_number_in_two_dimen_array(matrix, target)
    end = time.perf_counter_ns()
    print(end - start)
    print(result)

    start_two = time.perf_counter_ns()
    result_two = find_number_in_two_dimen_array_two(matrix, target)
    end_two = time.perf_counter_ns()
    print(end_two - start_two)
    print(result_two)


def find_number_in_two_dimen_array(
        matrix: List[List[int]], target: int) -> bool:
    """
    在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
    :param matrix: 二维数组
    :param target: 整数
    :return: 二维数组中是否含有该整数
    """
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
    return False


def find_number_in_two_dimen_array_two(matrix: List[List[int]], target: int) -> bool:
    """
     在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
     :param matrix: 二维数组
     :param target: 整数
     :return: 二维数组中是否含有该整数
     """
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    else:
        rows = len(matrix)
        columns = len(matrix[0])
        row = 0
        column = columns - 1
        while row < rows and column >= 0:
            num = matrix[row][column]
            if num == target:
                return True
            elif num > target:
                column -= 1
            else:
                row += 1
        return False
