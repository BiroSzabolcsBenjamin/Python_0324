import math
class Haromszog:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def kerulet(self):
        return self.a+self.b+self.c
    def terulet(self):
        s=(a+b+c)/2   
        return (s*(s-a)*(s-b)*(s-c))**0.5
    def szerkeszthetoseg(self):
        if a<b+c and b<a+c and c<b+a:
            return "Szerkeszthető!"
        else:
            return "Ez a háromszög nem szerkeszthető!"

haromszog=[]
a=int(input("a oldal hossza(cm): "))
b=int(input("b oldal hossza(cm): "))
c=int(input("c oldal hossza(cm): "))                         
szog=Haromszog(a,b,c)
haromszog.append(szog)

print("A háromszog kerülete: ", szog.kerulet(),"cm")
print("A háromszog területe: ", round(szog.terulet(),2),"cm")
print(szog.szerkeszthetoseg())