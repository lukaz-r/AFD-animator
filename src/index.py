from files.readText import *
from states.generatestates import *

states = readFile('entry/teste.txt')
statesif = getInitialFinal(states)
