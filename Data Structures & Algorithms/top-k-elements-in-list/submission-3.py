class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val  = {}
        d = []

        for num in nums:
            val[num] = val.get(num, 0) + 1

        for y in val.items():
            d.append(y)
            
        d.sort(reverse=True, key=lambda x:x[1])
        data = []
        
        for y in range(k):
            data.append(d[y][0])
        
        return data
