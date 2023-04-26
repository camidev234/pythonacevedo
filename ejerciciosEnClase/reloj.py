hora = int(input("Escriba la hora: "))
minutos = int(input("Escriba los minutos: "))
segundos = int(input("Escriba los segundos: "))

resetSegundos = 0
resetMinutos = 0
resetHora = 0
         

if segundos < 59:
    segundos+=1
elif minutos >=59:
    if segundos >=59:
        segundos = resetSegundos
    minutos=resetMinutos
    hora+=1   
elif segundos >= 59:
    segundos = resetSegundos
    minutos+=1
elif minutos >=59:
    if segundos <=59:
        segundos+=1
    minutos+=0

           
if hora == 24:
    hora= resetHora
    
print(f"{hora}: {minutos}: {segundos}")