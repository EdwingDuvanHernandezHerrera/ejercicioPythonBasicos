from  os import system
import math
alimentos = [["A", "B", "C"], [270,340,390]]
con = 0
opc = 0
efectivo = 0
bandera = True

while(bandera):
    
    system("cls")
    print("BIENVENIDO")
    print("PRODUCTOS DISPONIBLES")
    for i in alimentos[0]:
        print(f"\t{con}. {i}")
        con+=1
    try:
        opc = int(input("Por favor seleccione la opción correspondiente al producto que desea comprar: "))
        if opc <= len(alimentos[0])-1 and opc>=0: 
            bandera = False
            print("Usted ha elegido el proucto ", alimentos[0][opc], "por valor de ", alimentos[1][opc])
            print("Ahora, por favor ingrese el efectivo, solo se acepta monedas de $10, $50 y $100")
            while efectivo < alimentos[1][opc]:    
                moneda = int(input("\n"))

                if moneda == 10 or moneda==50 or moneda==100:
                    efectivo+=moneda
                    print("CRÉDITO INGRESADO: ", efectivo)
                    print("SALDO RESTANTE: ", alimentos[1][opc] - efectivo)
                else:
                    print("La moneda ingresada no es válida, solo se aceptan monedas de $10, $50 o $100")
            if efectivo > alimentos[1][opc]:
                cambio = efectivo - alimentos[1][opc]
                print("Su cambio es de ",  cambio)
            else: 
                print("Ha pagado el valor exacto")
            print("Gracias por su compra")        
        else: raise
    except:
        print("El valor ingresado no es válido, intente nuevamente")
        bandera = True
    finally:
        con=0

