class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_num = 0

        freq_count = {}
        left = 0

        maxFreq = 0

        for right in range(len(s)):
            freq_count[s[right]] = 1 + freq_count.get(s[right],0)

            maxFreq = max(maxFreq, freq_count[s[right]])

            while (right - left + 1) - maxFreq > k:
                # checking whether it is a valid window
                # Overall, we want to replace the number of characters possible that is not the max Freq
                freq_count[s[left]] -= 1
                left += 1
            max_num = max(max_num, right - left + 1)

        return max_num 