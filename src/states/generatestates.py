def getInitialFinal(lstates: list):
    states = lstates[0]
    listai = []
    listaf = []
    listai = states.split(";")
    listaf.append(listai[1])
    del lstates[0]  #Deleta elemento de estados iniciais e finais
    del listai[1]
    listaf = [x.strip(' ') for x in listaf]  # tira espaços dos elementos
    listai = [x.strip(' ') for x in listai]  # tira espaços dos elementos
