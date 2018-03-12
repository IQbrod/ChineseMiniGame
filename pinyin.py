#!/usr/bin/env python
# -*- coding: utf-8 -*-
from parser import ChineseParser
import random

nb = 5

c = ChineseParser("dico.iq")
gameData = c.splitPinYin()

print("Translate these "+str(nb)+" PinYin (in Chinese):")
giv = []
sol = []
for i in range(5):
	# Select an element
	rd = random.choice(gameData)
	sol.append(rd[0])
	val = rd[1]
	gameData.pop(gameData.index(rd))

	giv.append(raw_input("\t"+val+":"))
print giv
print sol
