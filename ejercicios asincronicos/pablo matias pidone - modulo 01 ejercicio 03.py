nota_01 = int(input("Primera calificación "))
nota_02 = int(input("Segunda calificación "))
nota_03 = int(input("Tercera calificación "))

nota = nota_01 + nota_02 + nota_03
promedio = nota / 3

if promedio >= 6:
    print ('Felicitaciones estas aprobado')
else:
    print ('Reprobado, debes recursar')