from typing import List


def max_wealth(accounts: List[List[int]]) -> int:
    """
    给你一个 m * n 的整数网格 accounts，其中 account[i][j]是第 i 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的资产总量。
    :param accounts: 整数网格
    :return: 最富有客户的资产总量
    """
    accounts_len = len(accounts)
    result = 0
    for i in range(accounts_len):
        len_two = len(accounts[i])
        sum_one = 0
        for j in range(len_two):
            sum_one += accounts[i][j]
            result = max(result, sum_one)
    return result


def max_wealth_two(accounts: List[List[int]]) -> int:
    """
    给你一个 m * n 的整数网格 accounts，其中 account[i][j]是第 i 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的资产总量。
    :param accounts: 整数网格
    :return: 最富有客户的资产总量
    """
    return max(sum(accounts[i]) for i in range(len(accounts)))
