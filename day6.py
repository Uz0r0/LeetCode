# 1614 Maximum Nesting Depth of the Parentheses
# Runtime: 2ms
# Memory: 12.3MB

def maxDepth(s):
  c, x = 0, 0

  for i in s:
    if i == "(":
      c+=1
    elif i == ")":
      c-=1

    if x < c:
      x = c

  return x 
        