def append(list1, list2):
    list1.extend(list2)
    return list1


def concat(lists):
    return list(sum(lists, []))


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    return len(list)


def map(function, list):
    return [function(x) for x in list]


def foldl(function, list, initial):
    acc = initial
    for el in list:
        acc = function(acc, el)
    return acc


def foldr(function, list, initial):
    acc = initial
    for el in reversed(list):
        acc = function(acc, el)
    return acc

def reverse(list):
    return list[::-1]
