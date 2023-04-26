# tributar

edad = int(input("Escriba su edad: "))
ingresos = float(input("Escriba sus ingresos: "))

if edad >= 16 and ingresos >= 1000:
    print("Puede tributar impuestos")
else:
    print("No puede tributar")
    