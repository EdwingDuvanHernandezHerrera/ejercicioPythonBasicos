cantidadDias = int(input("Ingrese el número de días a analizar: "))
preciosDolar = []
alzas = []
for _ in range(cantidadDias):
    alzas.append([0] * cantidadDias)



def ingresoDatos(cantidadDias, preciosDolar):
    for i in range(0, cantidadDias):
        precioDolar = float(input("Ingrese el precio del día "+ str(i) +": "))
        preciosDolar.append(precioDolar)
    print(preciosDolar)

def calcularAlzas(cantidadDias, preciosDolar, alzas):
    for i in range(0, cantidadDias-1):
        alzas[0][i] = preciosDolar[(i+1)] - preciosDolar[i]
        alzas[1][i] = i
    return alzas

def ordenarAlzas(cantidadDias,alzas):
    for i in range(0,cantidadDias):
        for j in range(0,cantidadDias-1):
            if alzas[0][j]<alzas[0][j+1]:

                aux = alzas[0][j]
                alzas[0][j] = alzas[0][j+1]
                alzas[0][j+1] = aux

                ind = alzas[2][j]
                alzas[1][j] = alzas[1][j+1]
                alzas[1][j+1] = ind
    print("Las alzas ordenadas de manera descendente fueron: ", alzas[0][:])


ingresoDatos(cantidadDias, preciosDolar)
calcularAlzas(cantidadDias, preciosDolar, alzas)
ordenarAlzas(cantidadDias,alzas)

if alzas[0][0] == 0:
    print("No se presentaron alzas en el precio del dólar para el periodo estimado")
else:
    mostrar = alzas[1][1] + 1
    print("En el cambio del día ",alzas[1][0]," para el día ",mostrar," se presentó la mayor alza en el precio del dólar por valor de ", alzas[0,0])












