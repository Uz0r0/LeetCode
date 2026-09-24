# Roman to Integer (Easy)
# Runtime: 4ms
# Memory: 12.30MB

def romanToInt(s):
  r = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }

  total = 0
  total += r[s[len(s) - 1]]

  for i in range(len(s) - 1):
    if r[s[i]] < r[s[i+1]]:
      total -= r[s[i]]
    else:
      total += r[s[i]]
    
  return total
