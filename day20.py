# 67 Add Binary
# Runtime: 3ms
# Memory: 12.27MB

def addBinary(a, b):
  i = len(a) - 1
  j = len(b) - 1
  c = 0
  ans = []
        
  while i >= 0 or j >= 0 or c:
    t = c
    if i >= 0:
      t += int(a[i])
      i -= 1
    if j >= 0:
      t += int(b[j])
      j -= 1
            
    c = t // 2
    ans.append(str(t % 2))

  return ''.join(ans[::-1])
