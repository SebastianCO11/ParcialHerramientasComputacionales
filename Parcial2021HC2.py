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
while Programa == 1:
    Rol = int(input("¿Es usted estudiante o profesor?: "))
    if Rol == 1:
        Rol = "Estudiante"
        
    else:
        Rol = "Profesor"    
    ID = int(input("Digite su ID de ciudadania: "))
    print()
    
    ##print("Codigos")
    ##print("173. Gaseosa = 1800")
    ##print("234. Galleta = 800")
    ##print("345. Chicle = 450")
    ##print("21. Banana = 900")
    ##print("34. Manzana = 700")
    ##print("2. Papitas = 1500")
    ##print()
    
    Cont = 1
    Productos = int(input("¿Cuantos productos desea llevar?: "))
    ListaPrecio = []
    ListaProducto = []
    ListaCodigo = []
    PrecioCont = 0
    while Cont <= Productos:
        Producto = input("¿Que producto desea llevar?: ")
        ListaProducto.append(Producto)
        print()
        Codigo = int(input("Digite el codigo del producto: "))
        ListaCodigo.append(Codigo)
        print()
        Cantidad = int(input("Digite la cantidad del prodcuto: "))
        print()
        Precio = int(input("Digite el precio de ese producto: "))
        ListaPrecio.append(Precio)
        PrecioCont += Precio * Cantidad
        print()
        Cont += 1
    print(Rol,"Con ID",ID,"eh aqui su lista de compra")
    print()
    print("Eh aqui la lista productos en orden")
    print(ListaProducto)
    print("Eh aqui la lista de Precios en orden")
    print(ListaPrecio)
    print("Eh aqui la lista de Codigos en orden")
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
    Programa = int(input("¿Desea finalizar el programa?: "))
print()
print("Mañana sera otro dia fantastico")
