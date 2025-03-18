# Backtracking

#1
#We wish to build strings of zeros and ones with some restrictions.

#Consider integers low, high that define the minimum and maximum size of a string, and integers zeros and ones that define the amount of zeros and ones that must be appended each time we add one of those digits.

#For instance, given low=4, high=6, zeros=2, ones=3, the valid strings are '0000', '000000', '00111', '11100', '111111'. The string '000000' results from the concatenation of three pairs of zeros, and string '111111' of two triples of ones.

#Define function strings that, given low, high, zeros, ones returns a list with all possible solutions. Return the list sorted.

def strings(low, high, zeros, ones):
    def backtrack(low, high, zeros, ones, path):
        if len(path) >= low and len(path) <= high:
            res.append(path) # found a valid string
        if len(path) > high: # string is too long
            return
        if zeros > 0:
            backtrack(low, high, zeros, ones, path + '0' * zeros)
        if ones > 0:
            backtrack(low, high, zeros, ones, path + '1' * ones)
        
    res = []
    backtrack(low, high, zeros, ones, '')
    return sorted(res)


#2
#Some numbers can be represented as a sum of distinct powers of integers (with a minimum base and exponent of 2).

#For eg, 87 = 2^2 + 2^3 + 2^4 + 2^5 + 3^3 (87 has another four solutions)

#Define function sum_powers that, given a positive n returns a list with all possible sum of distinct powers that result in n. Each element of the list should be a string with the format of the previous solution given for 87 (check also the examples). Return the list of solutions sorted.

def sum_powers(n):
    def backtrack(n, path, path_value, base, power, default_power):
        if path_value > n:  # sum is too big
            return
        if path_value == n:  # found a valid solution
            res.append(" + ".join(sorted(path)))  # remove the first ' + ' from the path
            return
        
        while (base ** default_power) + path_value <= n: # check if the base is not too big already        
            while (base ** power) + path_value <= n: # check if the power is not too big already
                path.append(f"{base}^{power}")
                backtrack(n, path, path_value + (base ** power), base, power+1, default_power)
                path.pop()
                power += 1
            power = default_power # reset power to 2 for the next base
            base += 1 # try the next base

    if n < 4:
        return []
    res = []
    power, base = 2, 2 # set the default values for power and base
    backtrack(n, [], 0, base, power, power)
    return sorted(res)

print(sum_powers(500))