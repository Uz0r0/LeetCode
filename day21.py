# 191 Number of 1 Bits
# Runtime: 0ms
# Memory: 12.39MB

def hammingWeight(n):
  ans = 0

  while n:
    if n % 2 == 1:
      ans += 1

    n = n // 2
    
  return ans