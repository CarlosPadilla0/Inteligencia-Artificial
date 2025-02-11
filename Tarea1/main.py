import arbolBinario as arbol

arbol = arbol.arbolBinario(1)
arbol.agregar(2)
arbol.agregar(3)
arbol.agregar(4)
arbol.agregar(5)
arbol.agregar(6)
arbol.agregar(7)
arbol.agregar(8)

# Búsqueda
busqueda = int(input("Busca algo en el árbol: "))
nodo = arbol.buscar(arbol.raiz, busqueda)
if nodo is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} sí existe")

mostrar = input("¿Desea mostrar el árbol? (s/n): ")
if mostrar == "s":
    arbol.mostrar(arbol.raiz)
else:
    print("¡Hasta luego!")
    