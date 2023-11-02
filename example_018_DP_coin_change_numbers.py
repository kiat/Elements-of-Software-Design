# A top-down recursive implementation
import sys

# Amount is amount = 4 and Coins are coins = {1, 2, 3},  
# 4 solutions: {1, 1, 1, 1}, {1, 1, 2}, {2, 2}, {1, 3}

# Some documentation about the problem  
# https://algorithmist.com/wiki/Coin_change

def coin_solution_recursive(coins, number_of_coins, amount):
    # ''' Recursive Top Down method  '''
	# check if the amount is zero, if yes, one solution, i.e., include no coin. 
	if (amount == 0):
		return 1

	# check if the amount 
	if (amount < 0):
		return 0

	# If there are no coins and n is greater than 0, then no solution exist
	if (number_of_coins <= 0 and amount >= 1):
		return 0

	return coin_solution_recursive(coins, number_of_coins - 1, amount) + \
           coin_solution_recursive(coins, number_of_coins, amount - coins[number_of_coins-1])


def coin_solution_with_memoization(coins, number_of_coins, amount):
    ''' Time complexity is O(number_of_coins x amount) '''

    # initialize the dp table
    dp = [[0 for x in range(number_of_coins)] for x in range(amount + 1)]

    # Fill the entries for 0 value case (amount = 0)
    for i in range(number_of_coins):
        dp[0][i] = 1


    # Iterative over combinations and fill the dp table. 
    # We start the amount from 1 and go to amount+1
    for i in range(1, amount + 1):
        for j in range(number_of_coins):                  

            # The solution count includes the specific coin[j]
            x = dp[i - coins[j]][j] if i - coins[j] >= 0 else 0 
            
            # The solution count excules coin[j] 
            y = dp[i][j-1] if j >= 1 else 0 
                
            
            # Calculates the total count for this combination 
            dp[i][j] = x + y
    
    return dp[amount][number_of_coins - 1]



# Call the functions.
if __name__ == "__main__":

	# Driver program to test above function
    coins = [1, 2, 3]
    amount = 5     
    
    print("Number of Solutions for " + str(coins) + " for amount " + str(amount) + " is: ",  coin_solution_recursive(coins, len(coins), amount))
    print("Number of Solutions for " + str(coins) + " for amount " +
          str(amount) + " is: ",  coin_solution_with_memoization(coins, len(coins), amount))
    
