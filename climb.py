class Solution :
    def climbStairs(self, n):
        """
        楼梯只能向上一步或者两步
        假设第n层楼梯，则可走的方法为n-1层向上一步，n-2层向上两步。则到第n层的方法为f（n）=f（n-1）+f（n-2）
        第一层有一种方法
        第二层有两种
        第三层=f（1）+f（2）
        f（4）=f（3）+f（2）
        从第n层向下计算需要使用递归算法，超时
        改为从第一层向上计算
        """
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








