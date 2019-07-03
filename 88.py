import math
ks=[int(i) for i in input().split()]
print(int(((ks[0]*ks[1])/(math.gcd(ks[0],ks[1])))))
