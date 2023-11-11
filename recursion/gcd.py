def gcf(a, b):
    """ calculate the GCF using the euclidean algorithm. """
    if b == 0:
        return abs(a)
    return gcf(b, a%b)

print(gcf(int(input()), int(input())))
