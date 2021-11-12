# Code for Number of Cuts for a Given Rod Size:

def cut_rod(p, n):
  r = []
  s = []

  for i in range(n + 1):
    r.append(0)
    s.append(0)

  for j in range(1, n + 1):
    max_price = -1

    for k in range(1, j + 1):
      new_price = 0

      if (k < len(p)):
        new_price = p[k] + r[j - k]
      else:
        new_price = r[j - k]
      if (new_price > max_price):
        max_price = new_price
        # remember the best value of the cut
        s[j] = k
        
    r[j] = max_price

  print(r)
  print(s)

  return r, s



def main():
  dim = int(input("Enter dimension of grid: "))

  cuts = []

  for i in range(dim + 1):
    row = []
    for j in range(dim + 1):
      row.append(0)
    cuts.append(row)

  for i in range(dim + 1):
    for j in range(dim + 1):
      if (i == 0) and (j == 0):
        cuts[i][j] = 1
      else:
        if (i > j):
          cuts[i][j] = cuts[i - 1][j]
        else:
          cuts[i][j] = cuts[i - 1][j] + cuts[i][j - i]

  # now print the grid
  for i in range(dim + 1):
    for j in range(dim + 1):
      print(cuts[i][j], end="  ")
    print()

  print()


# Call the main function. 
if __name__ == "__main__":
    main()
