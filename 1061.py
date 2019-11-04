lixo,diainicio = input().split()
diainicio = int(diainicio)
hinicio,minicio,sinicio = input().split(":")
hinicio = int(hinicio)
minicio = int(minicio)
sinicio = int(sinicio)
lixo,diafinal = input().split()
diafinal = int(diafinal)
hfinal,mfinal,sfinal = input().split(":")
hfinal = int(hfinal)
mfinal = int(mfinal)
sfinal = int(sfinal)
dia = diafinal - diainicio
hora = hfinal - hinicio
if(hora < 0):
	hora = 24 + hora
	dia = dia - 1
minuto = mfinal - minicio
if(minuto < 0):
	minuto = 60 + minuto
	hora = hora - 1
segundos = sfinal - sinicio
if(segundos < 0):
	segundos = 60 + segundos
	minuto = minuto - 1
if(dia <= 0):
	dia = 0
print("%d dia(s)"%dia)
print("%d hora(s)"%hora)
print("%d minuto(s)"%minuto)
print("%d segundo(s)"%segundos)