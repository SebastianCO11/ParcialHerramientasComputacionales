print("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}")
print("{}{}                                    {}{}")
print("{}{}      Bienvenido a JaveTienda       {}{}")
print("{}{}                                    {}{}")
print("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}")
print()
print("1. Estudiante")
print("2. Profesor")
print()
Programa = 1

#El codigo quedo algo largo para lo que es, sin embargo hay que evaluar los diferentes casos de error
#Bonus incluido
while Programa == 1:
    
    bandera = 0
    while bandera == 0:
        try:
            Rol = int(input("¿Es usted estudiante o profesor?: "))
            if Rol == 1:
                Rol = "Estudiante"
                bandera = 1
            elif Rol == 2:
                Rol = "Profesor"
                bandera = 1
            else:
                print("Esa variable no existe en los datos")
                print()
        except:
            print("Digitaste algo mal")
            print()
            
    bandera1 = 0  
    while bandera1 == 0:
        try:
            ID = int(input("Digite su ID de ciudadania: "))
            bandera1 = 1
            print()
        except:
            print("Haz digitado algo mal")
    
    ##print("Codigos")
    ##print("173. Gaseosa = 1800")
    ##print("234. Galleta = 800")
    ##print("345. Chicle = 450")
    ##print("21. Banana = 900")
    ##print("34. Manzana = 700")
    ##print("2. Papitas = 1500")
    ##print()
    

    bandera2 = 0  
    while bandera2 == 0:
        try:
            Productos = int(input("¿Cuantos productos desea llevar?: "))
            bandera2 = 1
            print()
        except:
            print("Haz digitado algo mal")

    Cont = 1
    ListaPrecio = []
    ListaProducto = []
    ListaCodigo = []
    PrecioCont = 0
    
    while Cont <= Productos:
        bandera3 = 0  
        while bandera3 == 0:
            try:
                Producto = input("¿Que producto desea llevar?: ")
                ListaProducto.append(Producto)
                bandera3 = 1
                print()
            except:
                print("Haz digitado algo mal")

        bandera4 = 0  
        while bandera4 == 0:
            try:
                Codigo = int(input("Digite el codigo del producto: "))
                ListaCodigo.append(Codigo)
                bandera4 = 1
                print()
            except:
                print("Haz digitado algo mal")

        bandera5 = 0  
        while bandera5 == 0:
            try:
                Cantidad = int(input("Digite la cantidad del prodcuto: "))
                bandera5 = 1
                print()
            except:
                print("Haz digitado algo mal")

        bandera6 = 0  
        while bandera6 == 0:
            try:
                Precio = int(input("Digite el precio de ese producto: "))
                ListaPrecio.append(Precio)
                PrecioCont += Precio * Cantidad
                bandera6 = 1
                print()
            except:
                print("Haz digitado algo mal")
        Cont += 1
        
    print(Rol,"Con ID",ID,"eh aqui su lista de compra")
    print()
    print("Eh aqui la lista productos en orden")
    print(ListaProducto)
    print("Eh aqui la lista de precios en orden")
    print(ListaPrecio)
    print("Eh aqui la lista de codigos en orden")
    print(ListaCodigo)
    print("Total a pagar")
    
    if Rol == "Estudiante":
        PrecioCont = (PrecioCont-(PrecioCont*0.5))
    elif Rol == "Profesor":
        PrecioCont = (PrecioCont-(PrecioCont*0.2))   
    print(PrecioCont)
    
    print()
    print("1. No")
    print("2. Si")
    print()
    
    bandera7 = 0
    while bandera7 == 0:
        try:
            Programa = int(input("¿Desea finalizar el programa?: "))
            bandera7 = 1
            print()
        except:
            print("Haz digitado algo mal")
    
    
print()
print("Mañana sera otro dia fantastico")
