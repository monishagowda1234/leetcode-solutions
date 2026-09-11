class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        l=[]
        mp=[0]*10
        for d in digits:
            mp[d] +=1

        for i in range(1,10):
            if mp[i]==0:
                continue
            else:
                mp[i] -= 1
            for j in range(0,10):
                if mp[j]==0:
                    continue
                else:
                    mp[j] -=1
                for k in range(0,10,2):
                    if mp[k]>0:
                        l.append(i*100+j*10+k)

                mp[j] +=1
            mp[i] +=1

        return len(l)

        