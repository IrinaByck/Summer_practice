from itertools import combinations


n, k = map(int, input().split())
a_i=list(map(int, input().split()))
maximum=0
for comb in combinations(a_i, k):
    summa=0
    for x in comb:
        summa^=x
    maximum=max(maximum, summa)
print(maximum)
