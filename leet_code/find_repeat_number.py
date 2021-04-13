import time
from typing import List


def find_repeat_number_test():
    """
    测试方法
    :return: 无返回
    """
    nums = [2, 3, 1, 0, 2, 5, 3]
    start = time.perf_counter_ns()
    result = find_repeat_number(nums)
    end = time.perf_counter_ns()
    print(end - start)
    print(result)

    start_two = time.perf_counter_ns()
    result_two = find_repeat_number_two(nums)
    end_two = time.perf_counter_ns()
    print(end_two - start_two)
    print(result_two)

    start_three = time.perf_counter_ns()
    result_three = find_repeat_number_three(nums)
    end_three = time.perf_counter_ns()
    print(end_three - start_three)
    print(result_three)

    start_four = time.perf_counter_ns()
    result_four = find_repeat_number_four(nums)
    end_four = time.perf_counter_ns()
    print(end_four - start_four)
    print(result_four)

    start_five = time.perf_counter_ns()
    result_five = find_repeat_number_five(nums)
    end_five = time.perf_counter_ns()
    print(end_five - start_five)
    print(result_five)


def find_repeat_number(nums: List[int]) -> int:
    """
    在一个长度为 n 的数组 nums 里的所有数字都在 0~n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字
    :param nums: 数组
    :return: 任意一个重复的数字
    """
    nums_len = len(nums)
    for i in range(nums_len):
        for j in range(nums_len):
            if i != j and nums[i] == nums[j]:
                return nums[i]

    return -1


def find_repeat_number_two(nums: List[int]) -> int:
    """
    在一个长度为 n 的数组 nums 里的所有数字都在 0~n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字
    :param nums: 数组
    :return: 任意一个重复的数字
    """
    temp = set()
    for num in nums:
        if num not in temp:
            temp.add(num)
        else:
            return num
    return -1


def find_repeat_number_three(nums: List[int]) -> int:
    """
    在一个长度为 n 的数组 nums 里的所有数字都在 0~n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字
    :param nums: 数组
    :return: 任意一个重复的数字
    """
    nums.sort()
    nums_len = len(nums)
    for i in range(1, nums_len):
        if nums[i] == nums[i - 1]:
            return nums[i]
    return -1


def find_repeat_number_four(nums: List[int]) -> int:
    """
    在一个长度为 n 的数组 nums 里的所有数字都在 0~n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字
    :param nums: 数组
    :return: 任意一个重复的数字
    """
    nums_len = len(nums)
    temp = [0 for i in range(nums_len)]
    for num in nums:
        temp[num] += 1
        if temp[num] > 1:
            return num
    return -1


def find_repeat_number_five(nums: List[int]) -> int:
    """
    在一个长度为 n 的数组 nums 里的所有数字都在 0~n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字
    :param nums: 数组
    :return: 任意一个重复的数字
    """
    nums_len = len(nums)
    for i in range(nums_len):
        if nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
    return -1
