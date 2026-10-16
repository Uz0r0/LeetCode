# 263 Ugly Number
# Runtime: 0ms
# Memory: 12.29MB

def isUgly( n):
  if (n <= 0): return False
        
  while n % 2 == 0: n /= 2
  while n % 3 == 0: n /= 3
  while n % 5 == 0: n /= 5

  return n == 1