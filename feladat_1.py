import math
f=open("eredmeny.txt","w",encoding="UTF-8")

class Haromszog:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def kerulet(self):
        return self.a+self.b+self.c
    def terulet(self):
        s=(a+b+c)/2         #háromszög kerületének fele  
        return math.sqrt(s*(s-a)*(s-b)*(s-c))
    def szerkeszthetoseg(self):
        if a<b+c and b<a+c and c<b+a:
            return "Szerkeszthető!"
        else:
            return "Ez a háromszög nem szerkeszthető!"
    def korsugar(self):
        s=(a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))/((a+b+c)/2)

haromszog=[]
a=int(input("a oldal hossza(cm): "))
b=int(input("b oldal hossza(cm): "))
c=int(input("c oldal hossza(cm): "))                         
szog=Haromszog(a,b,c)
haromszog.append(szog)

print("A háromszog kerülete: ", szog.kerulet(),"cm")
print("A háromszog területe: ", round(szog.terulet(),2),"cm")
print(szog.szerkeszthetoseg())
print("Háromszögbe írható kör sugara: ",round(szog.korsugar(),2),"cm")

lines=[["A háromszog kerülete:",szog.kerulet(),"cm"],'\n',["A háromszog területe: ",round(szog.terulet(),2),"cm"],'\n',[szog.szerkeszthetoseg()],'\n',["Háromszögbe írható kör sugara: ",round(szog.korsugar(),2),"cm"]]

for line in lines:
    f.writelines(str(line))
    f.writelines('\n')
f.close()