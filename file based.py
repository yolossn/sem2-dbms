import sys
file=open(r"C:\Users\SANTHOSH NAGARAJ\Desktop\elec.csv")
count=0
print('countries which produced above 5000 units per capita')
for line in file:
    (cou,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19)=line.split(",")
    a=float(y19)
    if(a>5000):
        print(cou)
        count=count+1
print (count)

