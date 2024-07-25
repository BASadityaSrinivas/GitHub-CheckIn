class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = k
        countt = {}
        for i in nums:
            countt[i] = 1 + countt.get(i, 0)

        freq = [[] for _ in range(len(nums) + 1)]
        for key, v in countt.items():
            freq[v].append(key)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return []