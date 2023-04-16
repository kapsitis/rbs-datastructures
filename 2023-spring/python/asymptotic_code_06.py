import itertools

def f6(n):
    allPairs = list(itertools.combinations(range(n), 2))
    for (a, b) in allPairs:
        for i in range(1, a+1):
            print(i*b)

f6(10)

