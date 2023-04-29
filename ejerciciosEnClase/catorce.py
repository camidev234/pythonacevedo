for i in range(100, 1000):
    num=i
    unidades= num %10
    num=num//10
    d=num%10
    c=num//10
    cubo = (unidades**3)+(d**3)+(c**3)
    if cubo == i:
        print(f"{i}son iguales")