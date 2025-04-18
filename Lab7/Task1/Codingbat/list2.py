def count_evens(nums):
  count = 0
  for x in nums:
    if x%2 == 0:
      count += 1
  return count

def big_diff(nums):
    return max(nums) - min(nums)

def centered_average(nums):
    nums.sort()
    return sum(nums[1:-1]) // len(nums[1:-1])

def sum13(nums):
    total = 0
    skip = False
    for num in nums:
        if num == 13:
            skip = True
            continue
        if skip:
            skip = False
            continue
        total += num
    return total

def sum67(nums):
    total = 0
    ignore = False
    for num in nums:
        if num == 6:
            ignore = True
        elif num == 7 and ignore:
            ignore = False
        elif not ignore:
            total += num
    return total

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False

