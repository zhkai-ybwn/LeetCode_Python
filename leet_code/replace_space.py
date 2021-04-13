import time


def replace_space_test():
    """
    测试方法
    :return: 无返回
    """
    s = "We are happy"
    start = time.perf_counter_ns()
    result = replace_space(s)
    end = time.perf_counter_ns()
    print(end - start)
    print(result)
    start_two = time.perf_counter_ns()
    result_two = replace_space_two(s)
    end_two = time.perf_counter_ns()
    print(end_two - start_two)
    print(result_two)


def replace_space(s: str) -> str:
    """
    把字符串 s 中的每个空格替换成"%20"。
    :param s: 原字符串
    :return: 替换后字符串
    """
    return s.replace(" ", "%20")


def replace_space_two(s: str) -> str:
    """
    把字符串 s 中的每个空格替换成"%20"。
    :param s: 原字符串
    :return: 替换后字符串
    """
    res = []
    for c in s:
        if c == ' ':
            res.append("%20")
        else:
            res.append(c)
    return "".join(res)
