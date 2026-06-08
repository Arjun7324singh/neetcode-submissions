class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        
        top_k_pairs = count.most_common(k)
        
        return [item[0] for item in top_k_pairs]
        