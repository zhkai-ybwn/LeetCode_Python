import time
from typing import List


def remove_element_test():
    """
    测试方法
    :return: 无返回
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    val = 2
    start = time.perf_counter_ns()
    result = remove_element(nums, val)
    print(result)
    end = time.perf_counter_ns()
    print(end - start)
    start_two = time.perf_counter_ns()
    result_two = remove_element_two(nums, val)
    print(result_two)
    end_two = time.perf_counter_ns()
    print(end_two - start_two)


def remove_element(nums: List[int], val: int) -> int:
    """
    给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
    不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
    元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
    :param nums: 数组
    :param val: 判断值
    :return: 新数组的长度
    """
    n = len(nums)
    for i in range(n):
        if nums[i] == val:
            for j in range(n - 1):
                nums[j] = nums[j + 1]
            i -= 1
            n -= 1
    return i


def remove_element_two(nums: List[int], val: int) -> int:
    """
    给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
    不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
    元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
    :param nums: 数组
    :param val: 判断值
    :return: 新数组的长度
    """
    n = len(nums)
    i = 0
    for j in range(n):
        if nums[j] == val:
            continue
        else:
            nums[i] = nums[j]
            i += 1
    return i
