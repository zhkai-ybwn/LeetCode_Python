from typing import List


def two_sum_dict(nums: List[int], target: int) -> List[int]:
    """
   给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标
   :param nums: 整数数组
   :param target: 目标值
   :return: 数组中和为目标值的两个整数的数组下标
   """
    dict_item = dict()
    for i, num in enumerate(nums):
        if target - num in dict_item:
            return [dict_item[target - num], i]
    return []


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标
    :param nums: 整数数组
    :param target: 目标值
    :return: 数组中和为目标值的两个整数的数组下标
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
