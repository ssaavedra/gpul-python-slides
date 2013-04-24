#!/usr/bin/python
# -*- coding: utf8 -*-

def square(n):
	"""
	>>> square(4)
	2.0

	>>> square(-1)
	Traceback (most recent call last):
		...
	ValueError: n ten que ser >= 0
	"""
	from math import sqrt
	if not n >= 0:
		raise ValueError("n ten que ser >= 0")
	return sqrt(n)


if __name__ == '__main__':
	import doctest
	doctest.testmod()