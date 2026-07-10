t=int(input())
for _ in range(t):
    n,c,d=map(int, input().split())
    b=list(map(int,input().split()))
    a11=min(b)
    sp=[]
    for i in range(n):
        for j in range(n):
            sp.append(a11+i*c+d*j)
    sp.sort()
    b.sort()
    print("YES" if sp==b else "NO")
