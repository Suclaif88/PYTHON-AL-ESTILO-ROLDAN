productos =[]
def agregar_producto():
    nombre=input("Digite el nombre del producto: ")
    cantidad=input("Digite el cantidad del producto: ")
    
    if nombre and cantidad:
        print('Nombre\tCantidad')
        productos.append({"nombre":nombre, "cantidad":cantidad})
        print("Producto agregado correctamente")
        
def listar_productos():
    for producto in productos:
        print(f"{producto['nombre']}\t{producto['cantidad']}")
def main():
    while True:
        print("1.Agregar Producto \n2.Listar Producto \n3.Salir ")
        opcion=input("Digite una Opcion")
        if  opcion=="1":
            agregar_producto()
        elif opcion=="2":
            listar_productos()
        elif opcion=="3":
            break
main()

 