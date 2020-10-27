nums = [int(x) for x in input().strip().split(' ')]
print(sum(nums) - max(nums), sum(nums) - min(nums))
# her sum is sum(iterable, start) iterable can be anything list , tuples or dictionaries ,
 but most importantly it should be numbers.
