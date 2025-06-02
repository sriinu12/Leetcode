class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0

        # Step 1: Initialize all candies to 1
        candies = [1] * n

        # Step 2: Left -> Right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right -> Left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # Ensure the child has more candies than right neighbor 
                # without violating the left-pass assignment
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Step 4: Return the sum
        return sum(candies)
        