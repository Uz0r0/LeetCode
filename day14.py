# 509 Fibonacci Number
# Runtime: 4ms
# Memory: 12.35MB

def fib(n):
  a, b = 0, 1
  ans = 0

  for i in range(n):
    ans = a + b
    b = a
    a = ans
            
  return ans