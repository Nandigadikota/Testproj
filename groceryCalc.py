"""Nandu
Date Items Expenditure
2016-01-01,Grocessry,100
2016-01-01	Sturdy 20
2016-02-01	Grocessrt 30
#year lo highest expenditure item
#which month u spent more
#find out unique items
#for every item-how much u spend"""

from datetime import datetime
myfile = open("groceryCal.txt","r")
k=myfile.readlines()
print k


#highest expenditure item
z={}
for line in k:
    x=line.split(",")
    #print x
    date,item,price=x
    if z.has_key(item):
        z[item].append(int(price))
       # print z
        #break
    else:
        z[item]=[int(price)]
        #print z
        #break
#print "Z is",z
e={}
for r,t in z.items():
    e[r]=sum(t)
#print e
import operator
exp=max(e.items(), key=operator.itemgetter(1))
print "Highest expenditure item",exp

"""
#which month u spent more
y={}
for i in k:
    x2=i.split(",")
    #print x
    date,item,price=x2
    #print x[0],x[1]
    date=datetime.strptime(date,"%Y-%m-%d")
    d=date.month
    if y.has_key(d):
        y[d].append(int(price))
        #print y
       # break
    else:
        y[d]=[int(price)]
        #break
#print y

m={}       #break
for k,v in y.items():
    m[k]=sum(v)
print m

#o=max(m, key=lambda j:m[j])
#print "Largest month expense :",o
import operator
o=max(m.items(),key=operator.itemgetter(1))
print "Largest month expense :",o
"""
#find out unique items
p={}
for rows in k:
    x1=rows.split(",")
    date,item,price=x1
    #date=datetime.strptime(date,"%Y-%m-%d")
    #print date
    if p.has_key(date):
        inner_dict=p[date]
        if inner_dict.has_key(item):
            p[date][item].append(item)
        else:
            p[date][item]=[price]
    else:
        p[date]={}
        p[date][item]=[price]
#print "P is ",p
f=[]
for j in p.values():
    f.append(j.keys())
#print f
g=[]
for l in f:
    for m in l:
        g.append(m)
#print g
s=set(g)
print "Unique items:",s

#for every item-how much u spend"{}
w={}
for row in k:
    x=row.split(",")
    #print x
    date,item,price=x
    if w.has_key(item):
        w[item].append(int(price))
    else:
        w[item]=[int(price)]
        #print w

#print "w is",w
it={}
for k,v in w.items():
    it[k]=sum(v)
print "Each item and value",it

