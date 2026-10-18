class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[]
        b=nums.count(0)
        if b>1:
            c=0
        else:
            c=1
            for i in nums:
                if i!=0:
                    c*=i
        for i in nums:
            if b>0 and i!=0 and b!=len(nums):
                a.append(0)
            elif b==len(nums):
                a.append(0)
            elif b<1:
                a.append(int(c/i))
            else:
                a.append(c)
        return a