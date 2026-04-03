class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_result = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in final_result:
                final_result[sorted_word].append(word)
            else:
                final_result[sorted_word] = [word]
        return list(final_result.values())