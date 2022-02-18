#Laboratorio 1 de python
#Modelación y simulación 2022
#Chahim Vicenta Imelda Teny Puac

#Variables
print("LECTURA DE INECUACIONES DE PRIMER GRADO")

menuPrincipal = int(input("Menu: \n 1- (n, n) \n 2- [n, n) \n 3- (n, n] \n 4- [n, n] \n 0- salir \n"))
while menuPrincipal != 0:
    
    if menuPrincipal == 1:
        print("Primer valor abierto, segudo abierto")
        
        valor1 =(input("Ingrese el valor inicial "))
        valor2 = (input("Ingrese el valor final "))
        
        print("(",valor1,",",valor2,")")
        print()
        #if valor2 > 0: 
        print("X Pertenece a los limites de ",valor1, "abierto a ", valor2, " abierto donde nunca llega a ser ", valor1, " y donde nunca llega a ser ", valor2)
        #else:
            #print("X Pertenece a los limites de ",valor1, "abierto a ", valor2, " abierto donde nunca llega a ser ", valor1, " y donde nunca llega a ser ", valor2,"Negativo")
             
        print()
        
    elif menuPrincipal == 2:
        print("Primer valor cerrado, segundo abierto")
        
        valor1 = (input("Ingrese el valor inicial "))
        valor2 = (input("Ingrese el valor final "))
        
        print("[",valor1,",",valor2,")")
        print()
        
       # if valor2 > 0:
        print("X Pertenece a los limites de ",valor1, "cerrado a ", valor2, " abierto donde el limite de llegada es de ", valor1, " y donde nunca llega a ser ", valor2)
        print()
            
        
    elif menuPrincipal ==3:
        print("Primer valor abierto, segundo cerrado")
        
        valor1 = (input("Ingrese el valor inicial "))
        valor2 = (input("Ingrese el valor final "))
        
        print("(",valor1,",",valor2,"]")
        print()
        
        print("X Pertenece a los limites de ",valor1, " abierto a ", valor2, " cerrado donde nunca llega a ser ", valor1, " y el limite de llegada máximo es de ", valor2)
        print()

    elif menuPrincipal ==4:
        print("Primer valor cerrado, segundo cerrado")
        
        valor1 = (input("Ingrese el valor inicial "))
        valor2 = (input("Ingrese el valor final "))
        
        print("[",valor1,",",valor2,"]")
        print()
        
        print("X Pertenece a los limites de ",valor1, "cerrado a ", valor2, " cerrado donde nunca llega a ser ", valor1, " y el limite de llegada máximo es de ", valor2)
        print()
        
    else: 
        print("Escriba una opcion valida")
    
    menuPrincipal = int(input("Menu: \n 1- (-n, n) \n 2- [n, n) \n 3- (n, n] \n 4- [n, n] \n 0- salir"))
    