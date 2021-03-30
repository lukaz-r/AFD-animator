from files.readText import *
from files.generateDot import *
from states.generatestates import *

states = readFile('entry/teste.txt')

statei, statef = generatestates.getInitialFinal(states)
ltrans = generatestates.getTransitions(states)
gerarDotInitial(statei, statef, ltrans)
