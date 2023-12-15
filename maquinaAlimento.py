from  os import system
alimentos = [["A", "B", "C"], [270,340,390]]
con = 0
opc = 0
bandera = True
while(bandera):
    system("cls")
    print("Elegir el producto")
    for i in alimentos[0]:
        print(f"\t{con}. {i}")
        con+=1
    try:
        opc = int(input("\n"))
        if opc <= len(alimentos[0])-1 and opc>=0: bandera = False
        else: raise
    except:
        print("usuario en serio sea serio >:(")
        bandera = True
    finally:
        con=0