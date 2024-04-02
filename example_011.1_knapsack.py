# A naive recursive implementation of 0-1 Knapsack Problem
# A Brute Force Approach

def recursive_knapsack(values, weights, n, cap_weight):
  
    # Base Case
    if n == 0 or cap_weight == 0 :
        return 0

    if (weights[n-1] > cap_weight):
        return recursive_knapsack(values, weights, n-1, cap_weight)

    else:
        return max(values[n-1] + recursive_knapsack(values, weights, n-1, cap_weight-weights[n-1]), \
          recursive_knapsack(values, weights, n-1, cap_weight))
        

#TODO for students. Develop the above recursive approach with memoziation technique. 


# Here is the DP solution Bottom-UP, Iterative using DP table
def knapsack(values, weights, n, cap_weight):
  
  dp = [[0 for x in range(cap_weight+1)] for x in range(n+1)]

  
  for i in range(n+1):
    for w in range(cap_weight+1):
      if(i == 0 or w ==0):
       dp[i][w]=0   
      elif(weights[i-1]<= w):
        dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
      else:
        dp[i][w] = dp[i-1][w]
  
  return dp, dp[n][cap_weight]


# Here is the DP solution Bottom-UP, Iterative using DP table
def knapsack_with_keep(values, weights, n, cap_weight):
  
  dp = [[0 for x in range(cap_weight+1)] for x in range(n+1)]
  keep = [[0 for x in range(cap_weight+1)] for x in range(n+1)]

  
  for i in range(n+1):
    for w in range(cap_weight+1):
      if(i == 0 or w ==0):
       dp[i][w]=0   
      elif(weights[i-1]<= w):
        dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
        keep[i][w] = 1
      else:
        dp[i][w] = dp[i-1][w]
        keep[i][w] = 0
  
  # # Now we print out which items are selected
  # k = cap_weight
  # for i in range(n+1, 0, -1):
  #   if keep[i][k] == 1:
  #     print(i)
  #     k = k - weights[i]


  # Now we print out which items are selected 
  # 
  opt=dp[n][cap_weight]
  w = cap_weight
  for i in range(n, 0, -1):
    if opt <= 0:
      break
    if opt == dp[i][w]:
      continue
    else:
      # This item is included.
      print((i, weights[i], values[i]))
        
      # Since this weight is included
      # its value is deducted
      opt = opt - values[i ]
      w = w - weights[i]
 
  return dp, dp[n][cap_weight]


            
# A print function to print 2D Matrix 
def print2D(a):
  for i in range(len(a)):
    for j in range(len(a[i])):
      print(a[i][j], end=',')
    print()
      

#######################
### Main Function #####
#######################

def main():
  v = [10, 40, 30, 50]
  w = [5, 4, 6, 3]
  print(v)
  print(w)
  
  n=len(v)
  weight=8
  
  value = recursive_knapsack(v, w , n, weight)
  print("Recursive Implementation, Maximum Value: ", value)

  print("\n\n DP Solution")
  value, optimal = knapsack(v, w , n, weight)
  print2D(value)
  print("DP Implementation, Maximum Value: ", optimal)
  
  print("\n\n DP Solution with Keep")
  value, optimal = knapsack_with_keep(v, w , n, weight)
  print("DP Implementation, Maximum Value: ", optimal)


# Call the main function. 
if __name__ == "__main__":
    main()
