# 20 Valid Parentheses
# Runtime: 3ms
# Memory: 12.45MB

def isValid(s):
  a = []
  b = {
    '(': ')',
    '[': ']',
    '{': '}',
  }
  for i in s:
    if i in b:
      a.append(i)
    else:
      if a and b[a[-1]] == i:
        a.pop()
      else:
        return False
        
  return not a

