#librerias
import random

def greedy_randomized_algorithm(beneficios, pesos, capacidad_max, alpha=0.5, max_iter=100):
  
    n = len(beneficios)
    mejor_solucion = None
    mejor_valor = 0
    for i in range(max_iter):
        #lista de candidatos
        candidatos = []
        for j in range(n):
            if pesos[j] <= capacidad_max:
                candidatos.append(j)
        if not candidatos:
            break
        #eligiendo la lista de los mejores candidatos
        rcl = []
        max_valor = 0
        for j in candidatos:
            valor = beneficios[j]
            if valor > max_valor:
                max_valor = valor
            rcl.append(j)
        for j in candidatos:
            if beneficios[j] >= max_valor - alpha * (max_valor - beneficios[j]):
                rcl.append(j)
        objeto_elegido = random.choice(rcl)
        #se va rellenando vector binario
        solucion = [0] * n
        solucion[objeto_elegido] = 1
        valor = beneficios[objeto_elegido]
        peso = pesos[objeto_elegido]
        for j in range(n):
            if j != objeto_elegido and peso + pesos[j] <= capacidad_max:
                solucion[j] = 1
                valor += beneficios[j]
                peso += pesos[j]
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_solucion = (solucion, peso)
    return mejor_solucion

beneficios = [33,24,36,37,12]
pesos = [15,20,17,8,31]
capacidad_max = 80
solucion, peso = greedy_randomized_algorithm(beneficios, pesos, capacidad_max)
#para poder hacer comparacion de las soluciones optimas
valor_total = sum(beneficios[i] for i in range(len(solucion)) if solucion[i] == 1)
print("Solución óptima:", solucion)
print("Peso de la solución:", sum(pesos[i] for i in range(len(solucion)) if solucion[i] == 1))
print("Valor total de la solución:", valor_total)
