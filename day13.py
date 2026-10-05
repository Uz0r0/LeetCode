# 26 Remove Duplicates from Sorted Array
# Runtime: 3ms
# Memory: 13.84MB

def removeDuplicates(nums):
  k = 1

  for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
      nums[k] = nums[i]
      k += 1

  return k