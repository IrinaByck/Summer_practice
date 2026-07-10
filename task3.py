import sys
def solve():
    input=sys.stdin.readline
    n,m = map(int, input().split())
    dp=[0]*(m+1)
    for i in range(n):
        row=list(map(int,input().split()))
        new_dp=[0]*(m+1)
        for j in range(1,m+1):
            new_dp[j]=max(dp[j],new_dp[j-1],dp[j-1])+row[j-1]
        dp=new_dp
    print(dp[m])
if __name__=="__main__":
    solve()
