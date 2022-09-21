from solucion import Solucion

instanciaSol= Solucion()
instancia2= Solucion()
instancia3= Solucion()
instanciaSol.llenar_estructura()
instancia2.llenar_estructura()
instancia3.llenar_estructura()

listaSol=[]
listaSol.append(instanciaSol)
listaSol.append(instancia2)
listaSol.append(instancia3)
#punto a
nombre = input()
listaSeries=[]
for i in listaSol:
        listaSeries.append(i.buscar_actor(nombre))

print(listaSeries)

#punto b
'''lenguaje= input("ingresa el lenguaje ")
for i in listaSol:
    if 
    '''