import random
tam= random.randrange(5,15)
t=()
for i in range(tam):
    elemeto=random.randrange(1,100)
    t+=(elemeto,)

print(t)

partido=len(t)//2

print(partido)

t2=t[ :partido]
print(t2)
t3=t[partido: ]
print(t3)
