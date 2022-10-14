# Quicksort Python One-liner 

unsorted = [33, 2, 3, 45, 6, 54, 33]


# The One-Liner
def q(l):
    return q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []


# The Result
sorts = q(unsorted)

print(sorts)
