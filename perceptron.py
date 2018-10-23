# -*-coding: utf-8-*-

import numpy as np

def get_data():
	return [[0, 0, 0, 1],
			[1, 0, 0, 1],
			[1, 0, 1, 1],
			[1, 1, 0, 1],
			[0, 0, -1, -1],
			[0, -1, -1, -1],
			[0, -1, 0, -1],
			[-1, -1, -1, -1]]

def calculate(dataset):
	c=0.5
	w=[-1, -2, -2, 0]
	time=1
	wtime=1
	while(True):
		stop=True
		print "Round: %r\\\\"%(time)
		for vector in dataset:
			result=map(lambda (a, b):a*b, zip(w, vector))
			value=get_value(result)
			#print "Vecor: %r"%(vector)
			#print "W%r: %r"%(wtime, w)
			#print "Value: %r"%(value)
			if not value>0:
				w=increment(w, vector, c)
				stop=False
				print_content="W(%r)^TX_%r=%r \\leq 0 \\Rightarrow W(%r)=W(%r)+cX_%r=%r\\\\"%(wtime, wtime, value, wtime+1, wtime, wtime, w)
				print print_content
			else:
				w=w
				print_content="W(%r)^TX_%r=%r > 0 \\Rightarrow W(%r)=W(%r)=%r\\\\"%(wtime, wtime, value, wtime+1, wtime, w)
				print print_content
			wtime+=1
		if stop:
			break
		time+=1

def get_value(vector):
	result=0
	for value in vector:
		result+=value
	return result

def increment(w, vector, c):
	return map(lambda (a, b): a+b*c, zip(w, vector))