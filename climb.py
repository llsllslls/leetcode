class Solution :
    def climbStairs(self, n):
        def f(x):
            if x ==1:return 1
            elif x==2:return 2
            else:
                a=1
                b=2
                for i in range(3,x+1):
                    temp = a+b
                    a=b
                    b=temp
                return temp

        return f(n)


if __name__ =="__main__":
    s=Solution()
    print(s.climbStairs(15))








