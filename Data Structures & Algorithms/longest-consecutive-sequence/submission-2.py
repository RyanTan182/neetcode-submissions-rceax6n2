class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashSet = {}
        for v in nums:
            hashSet[v] = 1
        print(hashSet)
        count = 1
        smallest_key = min(hashSet)
        largest_key = max(hashSet)

        curr = smallest_key
        max_count = 1
        for i in range(smallest_key,largest_key+1):
            print(i)
            if i in hashSet:
                if i - curr == 1:
                    print("Yes")
                    count +=1
                    curr = i
                else:
                    if count > max_count:
                        max_count = count
                    count = 1
                    curr = i
        
        larger_value = max_count if max_count > count else count
        return larger_value
        
        