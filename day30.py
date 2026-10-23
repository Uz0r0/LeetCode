# 169 Majority Element
# Runtime: 18ms
# Memory: 13.42MB

def majorityElement(nums):
  n = len(nums)
  m = dict()
        
  for num in nums:
    if num not in m:
      m[num] = 1
    else:
      m[num] += 1
        
  n = n // 2
        
  for key, value in m.items():
    if value > n:
      return key
        
  return 0