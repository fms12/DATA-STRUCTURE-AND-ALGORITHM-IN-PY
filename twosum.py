from collections import deque
def solve(n, nums, target):
    h={}
    for i,e in enumerate(nums):
        if target - e in h:
            return [h[target-e],i]
        h[e]=i

if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	target = int(input())
	out = solve(n, nums, target)
	print(*out)
