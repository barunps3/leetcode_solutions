class Solution:
    def climbStairs(self, n: int) -> int:
        # Find the number of pairs of x, y in the equation 2x + 1y = 5, x = (5-1y)/2
        number_of_ways_to_top = 0
        number_of_pairs_of_one_two = 0


        for y in range(n+1):
            # only when values of x and y exists such that 2x + 1y = n, only then count number of ways to the top
            if (n - 1*y)%2 == 0:
                x = (n - 1*y)/2
                #print("pair value of x and y are:", [x, y]) # values of x and y 
                # find number of ways the 1 step climb and 2 step climb can be combined to reach the top
                number_of_different_arrangement_of_one_two_pairs = math.factorial(x + y)/(math.factorial(x) * math.factorial(y))
                # add the combinations of pair to the final total number of ways to reach the top
                number_of_ways_to_top = number_of_ways_to_top + number_of_different_arrangement_of_one_two_pairs
                
        return int(number_of_ways_to_top)

    




