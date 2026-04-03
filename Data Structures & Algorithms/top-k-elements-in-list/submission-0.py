class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        freq_list = list(count.items())
        freq_list.sort(key=lambda x: x[1], reverse=True)

        top_k_elements = []

        for i in range(k):
            top_k_elements.append(freq_list[i][0])
        
        return top_k_elements
        


        