"""
Write a function, dictdiff, that takes two dicts as arguments. The function returns
a new dict that expresses the difference between the two dicts.
If there are no differences between the dicts, dictdiff returns an empty dict. For
each key-value pair that differs, the return value of dictdiff will have a key-value pair
in which the value is a list containing the values from the two different dicts. If one of
the dicts doesn't contain that key (my note: i think it should be value), it should contain None.
"""
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
d3 = {'a': 1, 'b': 2, 'd': 3}
d4 = {'a': 1, 'b': 2, 'c': 4}
d5 = {'a': 1, 'b': 2, 'd': 4}


# first solution - for dicts of equal length
# naive solution
def dictdiff(dict_1: dict, dict_2: dict) -> dict:
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
            diffdict[items_2[0]] = [dict_1.get(items_2[0]), dict_2.get(items_2[0]),]

    return diffdict

print(dictdiff(d1, d1))
print(dictdiff(d1, d2))
print(dictdiff(d3, d4))
print(dictdiff(d1, d5))


def diffdict(dict_1: dict, dict_2: dict) -> dict:
    diff = dict()
    diff_list = list()
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

print(diffdict(d1, d1))
print(diffdict(d1, d2))
print(diffdict(d3, d4))
print(diffdict(d1, d5))



"""
Planning notes for solution 1: 
What I want to do:
- compare both keys and values and check if there is a difference
- if there is a difference - save it in dict 
- difference is stored as key = key that we are comparing
- if under this index there are 2 different keys, then store 2 different dicts 
- values = list(value_dict_1, value_dict_2) 
- if there is no difference - return empty dict 

What I need:
- key values pairs - items() and get()
- for loop or while loop - both solutions :)?
"""
