# 119 Pascal's Triangle II
# Runtime: 0ms
# Memory: 12.17MB

def getRow(rowIndex):
  tr = []

  for i in range(rowIndex + 1):
    row = [1] * (i + 1)

    for j in range(1, i):
      row[j] = tr[i - 1][j - 1] + tr[i - 1][j]

    tr.append(row)
            
  return tr[rowIndex]