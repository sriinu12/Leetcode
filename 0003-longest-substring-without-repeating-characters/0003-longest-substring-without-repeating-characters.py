class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        i = 0
        max_len = 0
        for j, ch in enumerate(s):
            if ch in last_index and last_index[ch] >= i:
                i = last_index[ch] + 1
            last_index[ch] = j
            current_window_length = j - i + 1
            if current_window_length > max_len:
                max_len = current_window_length
        return max_len
        