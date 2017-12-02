# -*- coding: utf-8 -*-
"""
Created on Friday Oct 20 20:16:48 2017

@author: helto
"""

from random import random
import math


geracoes = 3000
tam_populacao = 20

limite_inferior = -10
limite_superior = 10
precisao = 2

quantidade_possibilidades = (limite_superior - limite_inferior) * (10 ** precisao)
tam_cromossomo  =  math.ceil(math.log(quantidade_possibilidades, 2))

print("Intevalos de ", [limite_inferior], " a ", [limite_superior])
print ("Tamanho cromossomo (bits): ", tam_cromossomo) 
print ("Quantidade de possibilidades: ", quantidade_possibilidades)
 

class Solucao(object):
    """
    Uma solução para o problema dado, é composto por um valor binário e seu valor físico
    """
    def __init__(self, value):
        self.value = value
        self.fitness = 0

    def calcular_fitness(self, funcao_fitness):
        
        ''' Valores decimais dos individuos (fitness) '''
        val_decimal = limite_inferior + funcao_fitness(self.value) * ((limite_superior - (limite_inferior)) / (quantidade_possibilidades))
        
        ''' Valores decimais dos individuos na funcao de X^2 '''    
        self.fitness = math.pow (val_decimal,2)
        
#        self.fitness = funcao_fitness(self.value)

        
def gerar_cromossomo(vector):
    """
    Gera uma nova solução candidata com base no vetor de probabilidade
    """
    value = ""

    for p in vector:
        value += "1" if random() < p else "0"

    return Solucao(value)


def gerar_vetor(tam_cromossomo):
    """
    Inicializa um vetor de probabilidade com tamanho determinado
    """
    return [0.5] * tam_cromossomo


def competicao(a, b):
    """
    Retorna uma tupla com a solução do vencedor
    """
    if a.fitness < b.fitness:
        return a, b
    else:
        return b, a


def atualizar_vetor(vector, vencedor, perdedor, tam_populacao):
    for i in range(len(vector)):
        if vencedor[i] != perdedor[i]:
            if vencedor[i] == '1':
                vector[i] += 1.0 / float(tam_populacao)
            else:
                vector[i] -= 1.0 / float(tam_populacao)

    """
    Percorre o vetor de probabilidade vericando o 100% ou 0%
    """
def converge(vector):
    for i in range(len(vector)):
        if (vector[i] > 0) and (vector[i] < 1) :
            return False
        else:
            return True

def CGA(geracoes, tam_cromossomo, tam_populacao, funcao_fitness):
    # esta é a probabilidade de cada bit de solução ser 1
    vector = gerar_vetor(tam_cromossomo)
    best = None
    
#    convergencia = False;
    # Para pelo número de gerações
    for i in range(geracoes): # and (convergencia == False)) :
#        convergencia = True

        # gerar duas soluções candidatas, é como a seleção em um GA convencional
        cromossomo1 = gerar_cromossomo(vector)
        cromossomo2 = gerar_cromossomo(vector)

        # calcular fitness para cada
        cromossomo1.calcular_fitness(funcao_fitness)
        cromossomo2.calcular_fitness(funcao_fitness)

        # deixe-os competir, para que possamos saber quem é o melhor do par
        vencedor, perdedor = competicao(cromossomo1, cromossomo2)

        if best:
            if vencedor.fitness < best.fitness:
                best = vencedor
        else:
            best = vencedor
        
        
        # atualiza o vetor de probabilidade com base no sucesso de cada bit
        atualizar_vetor(vector, vencedor.value, perdedor.value, tam_populacao)
        
        print(vector) 
        print ("Geração: %d Cromossomo --> %s Fitness --> %f" % (i + 1, best.value, (best.fitness)))

        
        
        # Paro pelo número de convergencia
        if (converge (vector) == True):
            break
        else:
            continue


#geracoes, tam_cromossomo, tam_populacao, funcao_fitness
if __name__ == '__main__':
    f = lambda x: int(x, 2)
    
    CGA(geracoes, tam_cromossomo, tam_populacao, f)

    "Conf Original"
#    CGA(1000, 32, 10, f)
   