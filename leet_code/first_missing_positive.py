import time
from typing import List


def first_missing_positive_test():
    """
    测试方法
    :return: 无返回
    """
    nums = [1, 3, 6, 7, 9]
    start = time.perf_counter_ns()
    result = first_missing_positive(nums)
    end = time.perf_counter_ns()
    print(end - start)
    print(result)
    start_two = time.perf_counter_ns()
    result_two = first_missing_positive_two(nums)
    end_two = time.perf_counter_ns()
    print(end_two - start_two)
    print(result_two)


def first_missing_positive(nums: List[int]) -> int:
    """
    给你一个未排序的整数数组 nums，请你找出其中没有出现的最小的正整数
    :param nums: 未排序的整数数组
    :return: 没有出现的最小的正整数
    """
    n = len(nums)
    res = [0 for i in range(n + 1)]
    for x in nums:
        if 0 < x < len(res):
            res[x] = x
    for i in range(len(res)):
        if res[i] != i:
            return i
    return len(res)


def first_missing_positive_two(nums: List[int]) -> int:
    """
    给你一个未排序的整数数组 nums，请你找出其中没有出现的最小的正整数
    :param nums: 未排序的整数数组
    :return: 没有出现的最小的正整数
    """
    n = len(nums)
    for i in range(n):
        if 0 < nums[i] < n + 1 and nums[1] != i + \
                1 and nums[i] != nums[nums[i] - 1]:
            swap(nums, i, nums[i] - 1)
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


def swap(nums: List[int], i: int, j: int):
    if i != j:
        nums[i] ^= nums[j]
        nums[j] ^= nums[i]
        nums[i] ^= nums[j]
