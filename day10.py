# 70 Climbing Stairs
# Runtime: 0ms
# Memory: 12.34MB

def climbStairs(n):
  if n <= 2: return n

  first = 1
  second = 2

  for i in range(3, n + 1):
    curr = second + first
    first = second
    second = curr
        
  return second 