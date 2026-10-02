# 35 Search Insert Position
# Runtime: 0ms
# Memory: 19.82MB

def searchInsert(nums, target):
  n = len(nums)
  left, right = 0, n - 1
  while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return right + 1
        