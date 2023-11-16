import itertools


def combos(lst):
    lst_combs = []
    for n in range(12, len(lst)+1):
        lst_combs += list(itertools.combinations(lst, n))
    print(len(lst_combs))
    return lst_combs
