s=input().strip()
n=len(s)
p,mod=31,10**9+7
h,hr,pow_w=[0]*(n+1),[0]*(n+1),[1]*(n+1)
for i in range(n):
    h[i+1]=(h[i]*p+ord(s[i]))%mod
    hr[i+1]=(hr[i]*p+ord(s[n-i-1]))%mod
    pow_w[i+1]=(pow_w[i]*p)%mod
for L in range(n,0,-1):
    hash_1=(h[L]-h[0]*pow_w[L])%mod
    hash_2=(hr[n]-hr[n-L]*pow_w[L])%mod
    if hash_1==hash_2:
        print(L)
        break
