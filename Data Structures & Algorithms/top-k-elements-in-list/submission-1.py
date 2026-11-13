class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_dict = defaultdict(int)

        for n in nums:
            frequency_dict[n] += 1
        
        sorted_items = sorted(frequency_dict.items(), key = lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]

        