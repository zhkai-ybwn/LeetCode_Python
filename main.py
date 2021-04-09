import time
from leet_code.two_num_sum import two_sum, two_sum_dict
from leet_code.remove_element import remove_element_two, remove_element
from leet_code.first_missing_positive import first_missing_positive, first_missing_positive_two
from leet_code.running_sum import running_sum, running_sum_two
from leet_code.max_wealth import max_wealth, max_wealth_two
from leet_code.sub_rectangle_queries import SubRectangleQueries
from leet_code.find_repeat_number import find_repeat_number, find_repeat_number_two, find_repeat_number_three, \
    find_repeat_number_four, find_repeat_number_five
from leet_code.find_number_in_two_dimen_array import find_number_in_two_dimen_array, find_number_in_two_dimen_array_two


def main():
    # two_num_sum_test()
    # remove_element_test()
    # first_missing_positive_test()
    # running_sum_test()
    # max_wealth_test()
    # sub_rectangle_queries_test()
    # find_repeat_number_test()
    find_number_in_two_dimen_array_test()


def two_num_sum_test():
    nums = [1, 3, 5, 7, 9, 12, 13, 19, 20]
    target = int(23)
    start = time.perf_counter_ns()
    result = two_sum(nums, target)
    end = time.perf_counter_ns()
    print(end - start)
    start_dict = time.perf_counter_ns()
    result_dict = two_sum_dict(nums, target)
    end_dict = time.perf_counter_ns()
    print(end_dict - start_dict)


def remove_element_test():
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


def first_missing_positive_test():
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


def running_sum_test():
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


def max_wealth_test():
    accounts = [[1, 2, 3], [1, 4, 5], [1, 4, 7]]
    start = time.perf_counter_ns()
    result = max_wealth(accounts)
    end = time.perf_counter_ns()
    print(end - start)
    print(result)

    start_two = time.perf_counter_ns()
    result_two = max_wealth_two(accounts)
    end_two = time.perf_counter_ns()
    print(end_two - start_two)
    print(result_two)


def sub_rectangle_queries_test():
    sub_rectangle_queries = SubRectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    result = sub_rectangle_queries.get_value(0, 2)
    print(result)
    sub_rectangle_queries.update_sub_rectangle(0, 0, 3, 2, 5)
    print(sub_rectangle_queries.data)


def find_repeat_number_test():
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


def find_number_in_two_dimen_array_test():
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


if __name__ == "__main__":
    main()
