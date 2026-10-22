class Solution:
    def minOperations(self, a):
        k,b = a.index(0),[*range(len(a))]
        return min(a[k:]+a[:k]==b and (k,len(a)-k+2) or 
            a[k::-1]+a[:k:-1]==b and (k+2,len(a)-k) or [-1])