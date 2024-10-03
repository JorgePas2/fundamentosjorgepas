#reaizar el programa de las horas extras

Horas= int(input ("digite un numero: "))

if Horas>8:
    pagojo= 8*200
    horaex=Horas-8
    pagoex=horaex*350
    pagoto=pagojo + pagoex
    print(pagoto)
else:
    pagojo= Horas * 200
    pagoto=pagojo
    print (pagoto)

print ("fin del programa")
