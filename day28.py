# 118 Pascal's Triangle
# Runtime: 0ms
# Memory: 12.07MB

def generate(numRows):
  ans = []

  for i in range(numRows):
    a = [1] * (i + 1)
            
    for j in range(1, i):
      a[j] = ans[i - 1][j - 1] + ans[i - 1][j]

    ans.append(a)

  return ans