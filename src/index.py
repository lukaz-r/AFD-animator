from files.readText import *
from states.generatestates import *

states = readFile('entry/teste.txt')

stateif = generatestates.getInitialFinal(states)
generatestates.getTransitions(states)