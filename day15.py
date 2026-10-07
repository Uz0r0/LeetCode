# 136 Single Number
# Runtime: 0ms
# Memory: 13.84MB

def singleNumber(nums):
  s = 0

  for n in nums:
    s = s ^ n
        
  return s