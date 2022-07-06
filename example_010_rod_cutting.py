def cut_rod (p, n):

  # Initialize two lists of zeros with size n 
  r = []
  s = []

  for i in range (n + 1):
    r.append (0)
    s.append (0)

  for j in range (1, n + 1):
    max_price = -1

    for k in range (1, j + 1):

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

  print (r)
  print (s)

  return r, s


def main():
  # define the price per length of rod
  p = [0, 1, 5, 8, 9, 10, 17, 17, 20]

  # prompt the user to enter the size of the rod to be cut
  n = int(input ("Enter size of rod: "))

  # get the optimal price for cutting a rod of length n
  r, s = cut_rod(p, n)

  # print the optimal price
  print("Optimal price = ", r[n])

  # print the cuts of the rod
  while (n > 0):
    print ("One Cut with size :", s[n])
    n = n - s[n]



# Call the main function. 
if __name__ == "__main__":
    main()
