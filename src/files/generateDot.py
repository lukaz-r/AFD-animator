from bash.generateBash import run_script


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
    arquivo.write("error [styled=filled, fillcolor=white];\n\t")
    for j in lstadosi:
        arquivo.write("p -> " + j + "\n\t")
    arquivo.write("node [shape = circle];\n\t")
    for j in ltrans:
        arquivo.write(j.origem + " -> " + j.destino + " [label = " + "\"" +
                      j.trans + "\"" + "];"
                      "\n\t")

    arquivo.write("}")
    arquivo.close()
    #Gerar imagem
    script = "dot -Tjpeg dotfiles/arq_.dot -o images/saida.jpg"
    run_script(script)
