import time
from typing import List

from leet_code.ListNode import ListNode


def reverse_print_test():
    head = ListNode(0)
    nextNode = head
    nums_list = [2, 3, 1]
    nums_list_len = len(nums_list)
    for i in range(nums_list_len):
        node = ListNode(nums_list[i])
        nextNode.next = node
        nextNode = nextNode.next
    nextNode = head
    start = time.perf_counter_ns()
    result = reverse_print(nextNode)
    end = time.perf_counter_ns()
    print(str(end - start) + "ns")
    print(result)

    start_two = time.perf_counter_ns()
    result_two = reverse_print_two(nextNode)
    end_two = time.perf_counter_ns()
    print(str(end_two - start_two) + "ns")
    print(result_two)

    start_three = time.perf_counter_ns()
    result_three = reverse_print_three(nextNode)
    end_three = time.perf_counter_ns()
    print(str(end_three - start_three) + "ns")
    print(result_three)


def reverse_print(head: ListNode) -> List[int]:
    """
    输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
    :param head: 链表头结点
    :return: 从尾到头反过来返回每个节点的值（用数组返回）
    """
    head_list = []
    temp = head
    while temp is not None:
        head_list.append(temp)
        temp = temp.next
    list_len = len(head_list)
    result = [0 for i in range(list_len)]
    for i in range(list_len):
        result[i] = head_list[list_len - i - 1].val
    return result


def reverse_print_two(head: ListNode) -> List[int]:
    """
    输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
    :param head: 链表头结点
    :return: 从尾到头反过来返回每个节点的值（用数组返回）
    """
    return reverse_print_two(head.next) + [head.val] if head else []


def reverse_print_three(head: ListNode) -> List[int]:
    """
    输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
    :param head: 链表头结点
    :return: 从尾到头反过来返回每个节点的值（用数组返回）
    """
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    return stack[::-1]
