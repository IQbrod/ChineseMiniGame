#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class ChineseParser():
	def __init__(self,fileName):
		self.data = self._parse_(fileName)

	def _parse_(self,fileName):
		with open(fileName, "r") as gFile:
			content = gFile.readlines()
			arr = []
			for ln in content:
				arr.append(ln.split("-"))
			for i in range(len(arr)):
				for j in range(3):
					arr[i][j] = arr[i][j].strip().split(" ")
		return arr
