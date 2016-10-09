import sys,sqlite3
con=sqlite3.connect("electricity")
cur=con.cursor()
cur.executescript("drop table if exists elec;CREATE TABLE elec(country string,y1 int,y2 int,y3 int,y4 int,y5 int,y6 int,y7 int,y8 int,y9 int,y10 int,y11 int,y12 int,y13 int,y14 int,y15 int,y16 int,y17 int, y18 int,y19 int);")
file=open(r"C:\Users\SANTHOSH NAGARAJ\Desktop\elec.csv")
for line in file:
    (cou,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19)=line.split(",")
    val=(cou,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19)
    cur.execute("insert into elec(country,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",val)
    con.commit()
count=0
print('countries which produced above 5000 units per capita')
a=cur.execute("select country from elec where y19>5000;")
for pro in a:
    print(pro[0])
    count=count+1
print(count)      
con.close
