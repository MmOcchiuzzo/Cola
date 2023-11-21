from cola_prioridad import ColaPrioridad

cola = ColaPrioridad()

def download():
    cola.arrive("Fabian", 1)
    cola.arrive("Enzo", 1)
    cola.arrive("Brock", 1)

# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
def getDocument(cola):
    print()
    print('imprimo el primero (solo el nombre)')
    print(cola.atention()[1])

# c. cargue dos documentos del staff de TI.
def downloadStaffTI(cola):
    cola.arrive("Liset", 2)
    cola.arrive("Melina", 2)


# d. cargue un documento del gerente.
def downloadGerent(cola):
    cola.arrive("Lance", 3)

# e. imprima los dos primeros documentos de la cola.
def deleteTwoFirst(cola):
    print()
    print('imprimo los 2 primeros')
    print(cola.atention())
    print(cola.atention())

# f. cargue dos documentos de empleados y uno de gerente.
def twoAndTreedownload(cola):
    cola.arrive("Sofia", 3)
    cola.arrive("Daniel", 1)
    cola.arrive("Jorge", 1)

# g. imprima todos los documentos de la cola de impresión.
def allDelete(cola):
    print()
    print('imprimo todos')
    for i in range(0, cola.size()):
        print(cola.atention())
    

download()
getDocument(cola)
downloadStaffTI(cola)
downloadGerent(cola)
deleteTwoFirst(cola)
twoAndTreedownload(cola)
allDelete(cola)