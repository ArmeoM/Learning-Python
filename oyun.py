import random
class oyun():
    global bitim
    bitim=0
    def __init__(self,isim,rakipisim="rakip",health=100,energy=2,zirh=0):
        self.isim=isim
        self.health=health
        self.energy=energy
        self.zirh=zirh
        self.rkisim=rakipisim
        self.rhealth=100
        self.pusu=0

    def zirhgiyme(self):
        if self.zirh<1:
            self.zirh +=1
            if 12!=random.randint(8,23):
                pass
            else:
                hasar=random.randint(5,15)
                print(f"rakip oyuncu tarafindan pusuya düşürüldünüz. {hasar} can kaybettiniz")
                self.health -= hasar            
                self.cankontrol()
        else:
            if 12!=random.randint(8,13):
                pass
            else:
                hasar=random.randint(5,15)
                print(f"rakip oyuncu tarafindan pusuya düşürüldünüz. {hasar} can kaybettiniz")
                self.health -= hasar
                self.cankontrol()
    def zirhkirma(self):
        x=random.randint(1,7)
        if x==3:
            self.zirh -=1
    def dinlen(self):
        x=random.randint(1,3)
        if 7 == random.randint(1,10):
            hasar=random.randint(10,20)
            print(f"rakip oyuncu tarafindan pusuya düşürüldünüz. {hasar} can kaybettiniz")
            self.energy += x-1
            self.health -=hasar 
            self.cankontrol()
        else:
            self.energy += x  
            self.health += random.randint(5,10)      
    def mevcutdurum(self):
        print(f"Canınız {self.health} kadar")
        print(f"Enerjiniz {self.energy} kadar")
        print(f"zirhiniz {self.zirh} kadar")
        print(f"Rakipinizin canı {self.rhealth} kadar")
        if self.pusu==1:
            print("pusudasiniz")
    def pusukur(self):
        if 2!=random.randint(1,10):
            self.pusu +=1
    def cankontrol(self):
        if self.health <= 0:
            print(f"Kaybettiniz {self.rkisim} kazandı")
            global bitim
            bitim=1
        elif self.rhealth <=0 :
            
            bitim=1
            print("kazandiniz tebrikler")
    def saldır(self):
        x=random.randint(1,3)
        if self.energy > 0:
            self.energy -=1
            print("⚔️ "*15,"⚔️ "*15,"⚔️ "*15,"⚔️ "*15,"⚔️ "*15,sep="\n")
            if x==2:
                print("saldiriyi başariyle gerçekleştirdiniz")
                if self.pusu>=1:
                    hasar=random.randint(20,40)
                    self.rhealth -= hasar
                    print(f"rakip oyuncuyu pusuya düşürdünüz. Rakip {hasar} can kaybetti ")
                    self.cankontrol()
                    self.pusu-=1
                else:
                    hasar=random.randint(10,30)
                    self.rhealth -= hasar
                    print(f"Rakip {hasar} can kaybetti")
                    self.cankontrol()
                
            elif x==1 :
                print("saldiriyi başaramadınız")
            else :
                print("iki tarafta hasar almadı")
                if self.zirh ==1:
                    hasar=random.randint(0,10)
                    self.health -= hasar
                    self.zirhkirma()
                    print(f"zırhla birlikte {hasar} can kaybettiniz")
                    self.cankontrol()
                elif self.zirh==0:
                    hasar=random.randint(5,20)
                    self.health -= hasar
                    self.zirhkirma()
                    print(f" {hasar} can kaybettiniz")
                    self.cankontrol()
                else:
                    hasar=random.randint(15,30)
                    self.health -= hasar
                    self.zirhkirma()
                    print(f"Zırhsız {hasar} can kaybettiniz")
                    self.cankontrol()
                    
        else:
            print("yeterli enejiniz yok")
def çalıştır(isim="oyuncu"):
    z=oyun(isim)
    while True:
        if bitim==1:
            break
        x=input("         Ne yapmak istersiniz       \nSaldır               == 1\nPusu kur             == 2\nZırhınızı giyin      == 3\nMevcut durumu göster == 4\nDinlen               == 5\nÇıkmak için          == q\n")    
        if x =="1":
            z.saldır()
        elif x=="2":
            z.pusukur()
        elif x=="3":
            z.zirhgiyme()
        elif x=="4":
            z.mevcutdurum()
        elif x=="5":
            z.dinlen()
        elif x=="q":
            print("erken çıkış yapıldı")
            break
        else:
            print("geçerli bir değer giriniz")        
çalıştır("hasan")               
                 
                
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    