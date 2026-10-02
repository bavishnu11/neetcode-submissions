class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        a={}
        for i, b in counts.items():
            if b in a:
                a[b].append(i)
            else:
                a[b]=[i,]
        b=[]
        for i in range(len(nums)):
            b.append([])
        for i in a:
            b[i-1]=a[i]
        c=[]
        b=b[::-1]
        for i in range(len(nums)):
            for j in b[i]:
                c.append(j)
            if len(c)==k:
                return c