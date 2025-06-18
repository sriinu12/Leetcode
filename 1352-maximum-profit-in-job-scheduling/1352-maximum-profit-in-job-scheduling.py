class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Step 1: combine and sort
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        starts = [s for s, e, p in jobs]
        n = len(jobs)
        
        # dp[i] = max profit from jobs[i:]
        dp = [0] * (n + 1)
        
        # Step 2: fill dp bottom-up
        for i in range(n - 1, -1, -1):
            s_i, e_i, p_i = jobs[i]
            # option1: skip this job
            skip = dp[i + 1]
            # option2: take this job + best from the next non-overlapping
            j = bisect.bisect_left(starts, e_i)
            take = p_i + dp[j]
            dp[i] = max(skip, take)
        
        return dp[0]
        