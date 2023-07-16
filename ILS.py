import random

#Función que evalua los unos o ceros dentro de un arreglo
def sumar(sol):
    laSuma = 0
    for i in sol:
        laSuma = laSuma + i
    return laSuma

#Función que se encarga de hacer la busqueda local en la solución inicial
#Necesita el pase de tres elementos: Solucion-Inicial, fitness y cantidad de
#iteraciones que se realice la búsqueda
def busquedaLocal(solInicial, fit,cantidadIteraciones):
    contador=0
    while(contador<cantidadIteraciones):
        solmodificada= solInicial
        posicion = random.randrange(len(solInicial))
        st = 0
        if(solmodificada[posicion]==0):
            solmodificada[posicion]=1
        else:
            solmodificada[posicion]=1
        st=sumar(solmodificada)
        if(st>fit):
            solInicial=solmodificada
            fit=st
        contador= contador+1
    return solmodificada, fit

#Función princial (main) del algoritmo de busqueda local iterada
def principal():
    #Valores por default
    itera=0;
    # Tercer experimento: "25" iteracionesMax
    iteracionesMax=25;
    # Tamaño de la solución inicial: "15" elementos
    solucionInicial=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fitnes= sumar(solucionInicial)
    # Tercer experimento: "3" cantidadIteraciones
    cantidadIteraciones=3;
    print(fitnes)
    print(solucionInicial)
        
    while(itera<iteracionesMax):
        itera= itera+1
        solucionprima,fitsp = busquedaLocal(solucionInicial,fitnes,1)
        solucionestrella, fitse=busquedaLocal(solucionprima,fitsp,cantidadIteraciones)
        if(fitse>fitsp):
            solucionprima=solucionestrella
            fitsp=fitse
        print(solucionprima)
        print(fitsp)

    print(solucionprima)
    print(fitsp)

# Reto 3
# Identificando una metaheurística
# Julio Alberto Larrea Crisóstomo

#Llamada a función del (main)
principal()

    





        

        
