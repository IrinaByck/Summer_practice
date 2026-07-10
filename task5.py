N = int(input())
d = [int(input())]
for i in range(1, N):
    rows = list(map(int, input().split()))
    new_rows=[]
    for j in range(0, i+1):
        if j==0:
            best = d[0]
        elif j==i:
            best=d[-1]
        else:
            best=max(d[j-1], d[j])
        new_rows.append(rows[j]+best)
    d=new_rows
print(max(d))
        
