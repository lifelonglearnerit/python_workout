"""
Write a function, dictdiff, that takes two dicts as arguments. The function returns
a new dict that expresses the difference between the two dicts.
If there are no differences between the dicts, dictdiff returns an empty dict. For
each key-value pair that differs, the return value of dictdiff will have a key-value pair
in which the value is a list containing the values from the two different dicts. If one of
the dicts doesn't contain that key (my note: i think it should be value), it should contain None.
"""
from typing import Callable
from typing import Dict

DICTS = {
    'd1': {'a': 1, 'b': 2, 'c': 3},
    'd2': {'a': 1, 'b': 2, 'c': 4},
    'd3': {'a': 1, 'b': 2, 'd': 3},
    'd4': {'a': 1, 'b': 2, 'c': 4},
    'd5': {'a': 1, 'b': 2, 'd': 4}
}

TESTS = {
    ('d1', 'd1'): {},
    ('d1', 'd2'): {'c': [3, 4]},
    ('d3', 'd4'): {'c': [None, 4], 'd': [3, None]},
    ('d1', 'd5'): {'c': [3, None], 'd': [None, 4]}
}


def test(f: Callable[[dict, dict], dict], f_param: tuple, tests: dict) -> bool:
    """
    Function for testing functions for exercise 16 from
    Python Workout book.
    :param f: function comparing 2 dictionaries
    :param f_param: parameters of function f
    :param tests: dictionary of test cases
    :return: bool value where True: Test passed; False: Test failed
    """
    print(f'Test: {f_param}\nExpected result: {tests[f_param]}\nResult: {f}\nPassed: ')
    return True if f == tests[f_param] else False


# first solution - for dicts of equal length
# naive solution
def dictdiff1(dict_1: dict, dict_2: dict) -> dict:
    kv_dict_1 = dict_1.items()
    kv_dict_2 = dict_2.items()
    diffdict = dict()
    for items_1, items_2 in zip(kv_dict_1, kv_dict_2):
        if items_1 == items_2:
            continue
        elif items_1[0] == items_2[0]:
            diffdict[items_1[0]] = [dict_1.get(items_1[0]), dict_2.get(items_1[0])]
        elif items_1[0] != items_2[0]:
            diffdict[items_1[0]] = [dict_1.get(items_1[0]), dict_1.get(items_2[0])]
            diffdict[items_2[0]] = [dict_1.get(items_2[0]), dict_2.get(items_2[0]), ]
    return diffdict


def diffdict2(dict_1: dict, dict_2: dict) -> dict:
    diff = dict()
    if dict_1 == dict_2:
        return diff
    else:
        for dict_1_key, dict_2_key in zip(dict_1.keys(), dict_2.keys()):
            if dict_1.get(dict_1_key) != dict_2.get(dict_1_key):
                diff[dict_1_key] = [dict_1.get(dict_1_key), dict_2.get(dict_1_key)]
            elif dict_1_key != dict_2_key:
                diff[dict_1_key] = [dict_1.get(dict_1_key), dict_2.get(dict_1_key)]
                diff[dict_2_key] = [dict_1.get(dict_1_key), dict_2.get(dict_1_key)]

    return diff


# solution after getting hint about using set .union() to gather keys that
# are in both sets
def diffdict3(dict_1: dict, dict_2: dict) -> dict:
    diff = dict()
    common_keys = dict_1.keys() | dict_2.keys()
    for key in common_keys:
        if dict_1.get(key) != dict_2.get(key):
            diff[key] = [dict_1.get(key),
                         dict_2.get(key)]
    return diff

# -------------------------------------------TESTING-------------------------------------------------


FUNCTIONS = {
    1: dictdiff1,
    2: diffdict2,
    3: diffdict3
}

def run_all():
    for key in TESTS:
        for function in FUNCTIONS.values():
            print(f'----------------------{function}----------------------')
            print(test(function(DICTS[key[0]], DICTS[key[1]]), (key[0], key[1]), TESTS))

run_all()

