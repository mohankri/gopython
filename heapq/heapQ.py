#!/usr/bin/env python3
import heapq

nums = []
heapq.heappush(nums, 1)
heapq.heappush(nums, 8)
heapq.heappush(nums, 2)
heapq.heappush(nums, 23)
heapq.heappush(nums, 7)
heapq.heappush(nums, -4)
heapq.heappush(nums, 18)
heapq.heappush(nums, 23)
heapq.heappush(nums, 42)
heapq.heappush(nums, 37)
heapq.heappush(nums, 2)

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
 {'name': 'IBM', 'shares': 100, 'price': 91.1},
 {'name': 'AAPL', 'shares': 50, 'price': 543.22},
 {'name': 'FB', 'shares': 200, 'price': 21.09},
 {'name': 'HPQ', 'shares': 35, 'price': 31.75},
 {'name': 'YHOO', 'shares': 45, 'price': 16.35},
 {'name': 'ACME', 'shares': 75, 'price': 115.65},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda kv: kv['price'])
print (cheap)
largest = heapq.nlargest(3, portfolio, key=lambda kv: kv['shares'])
print (largest)

nums = [1, 8, -4]
heap=heapq.heapify(nums)
print(nums[0])
