class unitconvert():
    def __init__(self):
        pass
    @classmethod
    def girilendeger(self):
        try:
            girilendeger1=int(input("değeri giriniz\n"))
            return girilendeger1
        except ValueError:
            print("geçerli bir değer giriniz")
    @classmethod
    def consıcaklık(self):
        deger=input("C/K 1 K/C 2 C/F3 F/C 4 F/K 5 K/F 6 ")
        if deger=="1":
            girilen=self.girilendeger()
            sonuç= girilen + 273
            sayaç=len(str(int(sonuç)))
            sonuç=str(sonuç)
            print(f"sonuç {sonuç[:sayaç+3]} kelvindir")
        elif deger=="2":
            girilen=self.girilendeger()
            sonuç=girilen-273
            sayaç=len(str(int(sonuç)))
            sonuç=str(sonuç)
            print(f"sonuç {sonuç[:sayaç+3]} derecedir")
        elif deger=="3":
            girilen=self.girilendeger()
            sonuç=girilen/10*18+32
            sayaç=len(str(int(sonuç)))
            sonuç=str(sonuç)
            print(f"sonuç {sonuç[:sayaç+3]}  fahrenayttır")
        elif deger=="4":
            girilen=self.girilendeger()
            sonuç=(girilen-32)/1.8
            sayaç=len(str(int(sonuç)))
            sonuç=str(sonuç)
            print(f"sonuç {sonuç[:sayaç+3]} derecedir")
        elif deger=="5":
            girilen=self.girilendeger()-273
            sonuç=girilen/10*18+32
            sayaç=len(str(int(sonuç)))
            sonuç=str(sonuç)
            print(f"sonuç {sonuç[:sayaç+3]} fahrenayttır")
        elif deger=="6":
            girilen=self.girilendeger()
            sonuç=(girilen-32)/1.8 +273
            sayaç=len(str(int(sonuç)))
            sonuç=str(sonuç)
            print(f"sonuç {sonuç[:sayaç+3]} kelvindir")
    @classmethod
    def conagırlık(self):
        deger=input("kg/lbs için 1 lbs/kg için 2 yi yazınız")
        if deger=="1":
            girilen=self.girilendeger()
            sonuç=girilen*2.2
            sayaç=len(str(int(sonuç)))
            sonuç=str(sonuç)
            print(f"sonuç {sonuç[:sayaç+3]} kilomgramdır")
        elif deger=="2":
            girilen=self.girilendeger()
            sonuç=girilen/2.2
            sayaç=len(str(int(sonuç)))
            sonuç=str(sonuç)
            print(f"sonuç {sonuç[:sayaç+3]} lbsdir")
    @classmethod
    def conuzunluk(self):
        deger=input(
            "km/mil ise 1 mil/km ise 2 yi  metre/feet ise 3 feet/metre ise 4 ü seçiniz \n")
        if deger=="1":
            girilen=self.girilendeger()
            sonuç=girilen/1.6
            sayaç=len(str(int(sonuç)))
            sonuç=str(sonuç)
            print(f"sonuç {sonuç[:sayaç+3]} mildir")
        elif deger=="2":
            girilen=self.girilendeger()
            sonuç=girilen*1.6
            sayaç=len(str(int(sonuç)))
            sonuç=str(sonuç)
            print(f"sonuç {sonuç[:sayaç+3]} kilometredir")
        elif deger=="3":
            girilen=self.girilendeger()
            sonuç= girilen*3.28
            sayaç=len(str(int(sonuç)))
            sonuç=str(sonuç)
            print(f"sonuç {sonuç[:sayaç+3]} feetdir")
        elif deger=="4":
            girilen=self.girilendeger()
            sonuç=girilen/3.28
            sayaç=len(str(int(sonuç)))
            sonuç=str(sonuç)
            print(f"sonuç {sonuç[:sayaç+3]} feetdir")
        else:
            print("geçerli bir değer giriniz")
    @classmethod
    def başlat(self):
        while True:
            variable=input(
            "Hangi değeri çevirmek istersiniz\nSıcaklık:\nUzunluk:\nAğırlık\nÇıkış:\n")
            if variable.capitalize()=="Ağırlık" :
                self.conagırlık()
            elif variable.capitalize()=="Sıcaklık":
                self.consıcaklık()
            elif variable.capitalize()=="Uzunluk":
                self.conuzunluk()
            elif variable.capitalize()=="Çıkış":
                print("çıkış yapıldı")
                break
            else:
                print("geçerli bir değer giriniz")   
unitconvert.başlat()
