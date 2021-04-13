import time
from typing import List


def running_sum_test():
    """
    测试方法
    :return: 无返回
    """
    nums = [1, 2, 3, 4]
    start = time.perf_counter_ns()
    result = running_sum(nums)
    end = time.perf_counter_ns()
    print(end - start)
    print(result)

    start_two = time.perf_counter_ns()
    result_two = running_sum_two(nums)
    end_two = time.perf_counter_ns()
    print(end_two - start_two)
    print(result_two)


def running_sum(nums: List[int]) -> List[int]:
    """
    给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
    请返回 nums 的动态和
    :param nums: 数组
    :return: 数组的动态和
    """
    nums_len = len(nums)
    result = [0 for i in range(nums_len)]
    for i in range(nums_len):
        for j in range(i + 1):
            result[i] += nums[j]
    return result


def running_sum_two(nums: List[int]) -> List[int]:
    """
    给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
    请返回 nums 的动态和
    :param nums: 数组
    :return: 数组的动态和
    """
    nums_len = len(nums)
    res = [nums[0]]
    for i in range(1, nums_len):
        total = res[i - 1] + nums[i]
        res.append(total)
    return res
