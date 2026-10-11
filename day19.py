# 2778 Sum of Squares of Special Elements 
# Runtime: 0ms
# Memory: 12.30MB

def sumOfSquares( nums):
  n = len(nums)
  ans = nums[0]**2

  for i in range(1, n):
    if n % (i + 1) == 0:
      ans += nums[i]**2
            
  return ans
