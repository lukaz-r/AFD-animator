from automata.generateTransition import *


class generatestates:
    def getInitialFinal(lstates: list):
        states = lstates[0]
        listai = []
        listaf = []
        lista = []
        listai = states.split(";")
        listaf.append(listai[1])
        del lstates[0]  #Deleta elemento de estados iniciais e finais
        del listai[1]
        listaf = [x.strip(' ') for x in listaf]  # tira espaços dos elementos
        listaf = listaf[0].split(' ')
        listai = [x.strip(' ') for x in listai]  # tira espaços dos elementos
        listai = listai[0].split(' ')
        return listaf

    def getTransitions(lstates: list):
        tam = len(lstates)
        transit = []
        transit = lstates[:tam - 1]  #todos as transiçoes
        del lstates[:tam - 1]  #palavra
        #print(transit)

        automata = []
        for i in transit:
            divide = i.split('>')
            chaves = divide[0].split(' ')
            origem = chaves[0]
            trans = chaves[1]
            destino = divide[1].strip()
            automata.append(addTransition(origem, destino, trans))
        #print(automata[0].trans)
        return automata

    #Verifica transicoes
    # for j in automata:
    #     print(j.origem + "," + j.trans + "," + j.destino)
