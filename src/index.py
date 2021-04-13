from files.readText import *
from files.generateDot import *
from states.generatestates import *
from bash.generateBash import *

states = readFile('entry/teste.txt')

#Gerei estados iniciais e finais
statei, statef = generatestates.getInitialFinal(states)
#Gerei a palavra
word = generatestates.getWord(states)
#Gerei as transicoes
ltrans = generatestates.getTransitions(states)
#gerei automato inicial
gerarDotInitial(statei, statef, ltrans)
#Gerei transicao
#gerarDotTransicoes(statei, statef, ltrans, word, 0)
estadosCorrentes(statei, statef, ltrans, word)

script2 = 'convert -delay 60 -loop 0 images/*.jpg giff.gif'
run_script(script2)