# 2089 Find Target Indices After Sorting Array
# Runtime: 1ms
# Memory: 11.86MB

def targetIndices(nums, target):
  less = equal = 0

  for n in nums:
    if n < target:
      less += 1
    elif n == target:
      equal += 1
        
  return list(range(less, less + equal))