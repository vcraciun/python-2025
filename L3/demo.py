a=(1,5,'a')
b=[1,2,3,4,'a',0.4]
c=[1,2,[5,6,[5,5]]]
d=[]
d += [7]
d.append(7)
dd = sorted(d)
e=list()
f=set()
g={
    'xyz': 200,
    'tyq': 7
}
f.add(100)
g['abc'] = 100

print(a,b,c,d,e,f,g)
gg = dict(sorted(g.items(), key = lambda x: x[1], reverse=True))
print(gg)

for i, (k, v) in enumerate(g.items()):
    print(i, k, v)

x = [f for f in range(10) if f%2==0]
print(x)

col = list()

dd = {f:g for (f,g) in list(zip([5,6,7], ['a','b','c']))}
print(dd)

u = "1234567"
uu = "--".join(u)
print(u)
print(uu)
