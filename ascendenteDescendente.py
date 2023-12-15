import random

nums =[]
ordenadosAsc = []
ordenadosDesc = []


def generarNumeros(nums, ordenadosAsc, ordenadosDesc):
    for i in range(0,9):
        nums.append(random.randrange(1,10))
        ordenadosAsc.append(nums[i])
        ordenadosDesc.append(nums[i])
    print("Vector original:", nums)


def ascendentes(ordenadosAsc):
    for i in range(0, 9):
        for j in range(0, 8):
            if ordenadosAsc[j]>ordenadosAsc[j+1]:
                aux = ordenadosAsc[j]
                ordenadosAsc[j] = ordenadosAsc[j+1]
                ordenadosAsc[j+1] = aux
    print("Vector en orden ascendente:", ordenadosAsc)

def descendentes(ordenadosDesc):
    for i in range(0, 9):
        for j in range(0, 8):
            if ordenadosDesc[j]<ordenadosDesc[j+1]:
                aux = ordenadosDesc[j]
                ordenadosDesc[j] = ordenadosDesc[j+1]
                ordenadosDesc[j+1] = aux
    print("Vector en orden descendente:", ordenadosDesc)

generarNumeros(nums, ordenadosAsc, ordenadosDesc)
ascendentes(ordenadosAsc)
descendentes(ordenadosDesc)

