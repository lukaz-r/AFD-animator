from bash.generateBash import run_script
from copy import deepcopy
from automata.generateDestination import *


# Gera automato inicial
def gerarDotInitial(lstadosi: list, lstadosf: list, ltrans: list):

    arquivo = open('dotfiles/arq_.dot', 'w')
    arquivo.write("digraph maquina_de_estados { \n\t")
    arquivo.write("rankdir=LR;\n\t")
    arquivo.write("size=\"10\"\n\t")
    arquivo.write("node [shape = doublecircle];\n\t")
    for i in lstadosf:
        arquivo.write(i + "\n\t")
    arquivo.write("node [shape = point];\n\t")
    arquivo.write("p\n\t")
    arquivo.write("node [shape = circle];\n\t")
    arquivo.write("error [style=filled, fillcolor=white];\n\t")
    for j in lstadosi:
        arquivo.write("p -> " + j + "\n\t")
    arquivo.write("node [shape = circle];\n\t")
    for j in ltrans:
        arquivo.write(j.origem + " -> " + j.destino + " [label = " + "\"" +
                      j.trans + "\"" + "]" + "[color=black];" + "\n\t")

    arquivo.write("}")
    arquivo.close()
    #Gerar imagem
    script = "dot -Tjpeg dotfiles/arq_.dot -o images/saida.jpg"
    run_script(script)


def estadosCorrentes(lstadosi: list, lstadosf: list, ltrans: list, simb: list):
    tam = 0
    gerarDotTransicoes2(lstadosi, lstadosf, ltrans, lstadosi, tam, simb[0])

    trans = []
    converte = []
    converte2 = []
    currentS0 = []
    verifica = ["ok"]
    #verifica = ["ok"]
    #Copia profunda no python
    currentS = deepcopy(lstadosi)
    simb.append('ok')

    for l in simb:
        tam += 1
        trans.clear()

        #pega os destinos do estado corrente
        for m in currentS:  # estado corrente
            for i in ltrans:  # transicoes
                if m == i.origem:
                    trans.append(i)

        currentS.clear()
        for k in trans:
            if l == k.trans:
                currentS.append(k.destino)

        currentS0 = list(set(currentS))
        print(currentS0)

        if (tam == 1):
            gerarDotTransicoes2(lstadosi, lstadosf, ltrans, currentS0, tam,
                                verifica)

        # elif (tam != 1):
        #     print(l)
        #     gerarDotTransicoes2(lstadosi, lstadosf, ltrans, currentS, tam, l)

        gerarDotTransicoes2(lstadosi, lstadosf, ltrans, currentS0, tam, l)


def gerarDotTransicoes(lstadosi: list, lstadosf: list, ltrans: list,
                       estado: list, tam: int):
    currentState = estado
    tam = str(tam)

    arquivo = open('dotfiles/arq_' + tam + '.dot', 'w')
    arquivo.write("digraph maquina_de_estados { \n\t")
    arquivo.write("rankdir=LR;\n\t")
    arquivo.write("size=\"10\"\n\t")
    arquivo.write("node [shape = doublecircle];\n\t")
    for i in lstadosf:
        arquivo.write(i + "\n\t")
    arquivo.write("node [shape = point];\n\t")
    arquivo.write("p\n\t")
    arquivo.write("node [shape = circle];\n\t")
    arquivo.write("error [style=filled, fillcolor=white];\n\t")
    for j in lstadosi:
        arquivo.write("p -> " + j + "\n\t")
    arquivo.write("node [shape = circle];\n\t")
    #adicionar condicao de transicao
    arquivo.write(str(currentState[0]) + "[style=filled, fillcolor=gray]\n\t")
    for k in ltrans:

        if (currentState[0] == k.origem):
            arquivo.write(k.origem + " -> " + k.destino + "[label = " + "\"" +
                          k.trans + "\"" + "]" + "[color=magenta];" + "\n\t")
        else:
            arquivo.write(k.origem + " -> " + k.destino + "[label = " + "\"" +
                          k.trans + "\"" + "]" + "[color=black];" + "\n\t")

    arquivo.write("}")
    arquivo.close()
    #Gerar imagem
    script = 'dot -Tjpeg dotfiles/arq_' + tam + '.dot -o images/saida' + tam + '.jpg'
    run_script(script)


def gerarDotTransicoes2(lstadosi: list, lstadosf: list, ltrans: list,
                        estado: list, tam: int, simb: list):
    currentState = deepcopy(estado)
    tam = str(tam)
    tamT = 0

    arquivo = open('dotfiles/arq_' + tam + '.dot', 'w')
    arquivo.write("digraph maquina_de_estados { \n\t")
    arquivo.write("rankdir=LR;\n\t")
    arquivo.write("size=\"10\"\n\t")
    arquivo.write("node [shape = doublecircle];\n\t")
    for i in lstadosf:
        arquivo.write(i + "\n\t")
    arquivo.write("node [shape = point];\n\t")
    arquivo.write("p\n\t")
    arquivo.write("node [shape = circle];\n\t")
    arquivo.write("error [style=filled, fillcolor=white];\n\t")
    for j in lstadosi:
        arquivo.write("p -> " + j + "\n\t")
    arquivo.write("node [shape = circle];\n\t")
    for l in currentState:
        arquivo.write(str(l) + "[style=filled, fillcolor=gray]\n\t")


#arquivo.write(str(currentState[0]) + "[style=filled, fillcolor=gray]\n\t")

#adicionar condicao de transicao
    for k in ltrans:
        tamT = 0
        for t in currentState:

            tamT += 1

            # if (t == k.origem and simb == k.trans):
            #     arquivo.write(k.origem + " -> " + k.destino + "[label = " +
            #                   "\"" + k.trans + "\"" + "]" + "[color=lime];" +
            #                   "\n\t")

            if (t == k.origem):
                arquivo.write(k.origem + " -> " + k.destino + "[label = " +
                              "\"" + k.trans + "\"" + "]" +
                              "[color=magenta];" + "\n\t")
                if (tamT == currentState.index(currentState[-1])):
                    break

            else:
                if (tamT == currentState.index(currentState[-1])):
                    arquivo.write("")
                else:
                    arquivo.write(k.origem + " -> " + k.destino + "[label = " +
                                  "\"" + k.trans + "\"" + "]" +
                                  "[color=black];" + "\n\t")

            # else:
            #     if (tamT == currentState.index(currentState[-1])):
            #         arquivo.write(k.origem + " -> " + k.destino + "[label = " +
            #                       "\"" + k.trans + "\"" + "]" +
            #                       "[color=black];" + "\n\t")

    arquivo.write("}")
    arquivo.close()
    #Gerar imagem
    script = 'dot -Tjpeg dotfiles/arq_' + tam + '.dot -o images/saida' + tam + '.jpg'
    run_script(script)
