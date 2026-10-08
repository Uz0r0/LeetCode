# 1021 Remove Outermost Parentheses
# Runtime: 4ms
# Memory: 12.60MB

def removeOuterParentheses(s):
  ans = []
  depth = 0

  for i in s:
    if i == '(':
      if depth > 0:
        ans.append(i)
      depth += 1
    else:
      if depth != 1:
        ans.append(i)
      depth -= 1

  return ''.join(ans)