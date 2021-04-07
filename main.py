import time
from leet_code.two_num_sum import two_sum, two_sum_dict
from leet_code.remove_element import remove_element_two, remove_element
from leet_code.first_missing_positive import first_missing_positive, first_missing_positive_two
from leet_code.running_sum import running_sum, running_sum_two
from leet_code.max_wealth import max_wealth, max_wealth_two


def main():
    # two_num_sum_test()
    # remove_element_test()
    # first_missing_positive_test()
    # running_sum_test()
    max_wealth_test()


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


if __name__ == "__main__":
    main()
