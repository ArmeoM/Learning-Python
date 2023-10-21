class Solution(object):
    def longestCommonPrefix(self, strs):
        
        sayac=0
        elemansayi=99999
        durdurgac=0
        for i in strs:
            if len(i)<elemansayi:
                elemansayi= len(i)
            if i=="":
                return ""
        elemansayi-=1

        if  len(strs)==1: 
            return strs[0]
        
        else:
            print(elemansayi)
            while True:
                for i in strs:
                    if strs[0][sayac]==i[sayac]:
                        pass   
                    else:
                        durdurgac=1
                if durdurgac==1:
                    break

                if elemansayi!=sayac:
                    sayac +=1
                else:
                    sayac +=1
                    durdurgac=1
                if durdurgac==1:
                    break                
            return strs[0][:sayac]
        

        