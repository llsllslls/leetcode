class Solution:
    """
    动态规划问题
    先创建一个最优结果数组，然后从0~len（nums）算最优结果。
    """
    def rob(self, nums):
        import numpy as np
        m=np.zeros(len(nums))
        if len(nums)==0:return 0
        def opt(x):
            if x==0:
                result = nums[x]
                m[x] = result
            elif x==1:
                result = max(nums[:2])
                m[x] = result
            else:
                result = max(nums[x]+m[x-2],m[x-1])
                m[x] = result
        for i in range(len(nums)):
            opt(i)
        return m[len(nums)-1]

if __name__ =="__main__":
    s=Solution()
    print(s.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))
