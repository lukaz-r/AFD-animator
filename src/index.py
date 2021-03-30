from files.readText import *
from files.generateDot import *
from states.generatestates import *

states = readFile('entry/teste.txt')

statef = generatestates.getInitialFinal(states)
ltrans = generatestates.getTransitions(states)
gerarDotInitial(statef, ltrans)
