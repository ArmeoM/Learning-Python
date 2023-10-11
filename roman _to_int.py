class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
      
        
        
        deger=0
        k={"IM":999,"VM":995,"XM":990,"LM":950,"CM":900,"DM":500}
        for i,y in k.items():
            if i in s:
                deger +=y
                s=s.replace(i,"")
        k={"ID":499,"VD":495,"XD":490,"LD":450,"CD":400}
        for i,y in k.items():
            if i in s:
                deger += y
                s=s.replace(i,"")
        k={"IC":99,"VC":95,"XC":90,"LC":50}
        for i,y in k.items():
            if i in s:
                deger += y
                s=s.replace(i,"")
        k={"IL":49,"VL":45,"XL":40}
        for i,y in k.items():
            if i in s:
                deger += y
                s=s.replace(i,"")
        k={"IX":9,"VX":5}
        for i,y in k.items():
            if i in s:
                deger += y
                s=s.replace(i,"")
        k={"IV":4}
        for i,y in k.items():
            if i in s:
                deger += y
                s=s.replace(i,"")
            
        for i in s:
            if i=="I":
                deger +=1
            elif i =="V":
                deger +=5
            elif i=="X":
                deger +=10
            elif i=="L":
                deger +=50
            elif i=="C":
                deger +=100
            elif i =="D":
                deger +=500
            elif i == "M":
                deger +=1000      
         
        return deger
        
        
