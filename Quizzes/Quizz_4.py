# Define function ins_to_palin that receives a string and returns the minimum number of letter insertions (at any position) needed to make the string a palindrome.

def ins_to_palin(s):
    """
    This function calculates the minimum number of insertions required to make a string a palindrome.
    
    :param s: The input string
    :return: The minimum number of insertions needed
    """
    # Initialize a 2D array to store the lengths of longest palindromic subsequences
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Fill the diagonal with 1s since single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the dp table
    for length in range(2, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    # The minimum insertions needed is the difference between the string length and the longest palindromic subsequence
    return n - dp[0][n - 1]


s = "ujrjotvu"
print(ins_to_palin(s))

# Given a positive integer n≤200, consider the following game:
# You need to find the winning number that is between 1 and n (inclusive)
# Say you pick x: 
# If you pick the right number, you win
# If not, you must pay x euros and then be told if it is larger or smaller than the winning number
# If you run out of money, you lose the game, otherwise you repeat the process

# Define function min_win_game that receives the positive integer n and returns the smallest amount of money that guarantees winning the game no matter what the winning number is.

def min_win_game(n):
    """
    This function calculates the minimum amount of money needed to guarantee a win in the game.
    
    :param n: The upper limit of the range
    :return: The minimum amount of money needed
    """
    # Initialize a 2D array to store the minimum costs
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Fill the dp table
    for length in range(2, n + 1):  # length of the range
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')
            for x in range(i, j + 1):
                cost = x + max(dp[i][x - 1], dp[x + 1][j] if x + 1 <= j else 0)
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[1][n]

print(min_win_game(100))
