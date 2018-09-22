from random import randint
cp_calc = int()	

def type():
	operation = randint(1,4)
	return operation	
	
def niveau(cp_calc):
	if cp_calc <= 5: lvl = 1
	elif cp_calc > 5 and cp_calc <= 10: lvl = 2
	else: lvl = 3
	print("lvl",lvl)
	return lvl
	
def calcul(operation,lvl):
	if operation == 1:
		signe = '+'
		if lvl == 1:	
			n1 = randint(1,100)
			n2 = randint(1,100)
		elif lvl == 2:	
			n1 = randint(100,200)
			n2 = randint(100,200)
		else:	
			n1 = randint(200,500)
			n2 = randint(200,500)			
		result = n1+n2
	elif operation == 2:
		signe = '-'
		if lvl == 1:
			n1 = randint(1,100)
			n2 = randint(1,100)
		elif lvl == 2:
			n1 = randint(100,200)
			n2 = randint(100,200)
		else:
			n1 = randint(200,500)
			n2 = randint(200,500)
		if n2 >= n1:
			n1,n2 = n2,n1
		result = n1-n2
	elif operation == 3:
		signe = '*'
		if lvl == 1:
			n1 = randint(1,7)
			n2 = randint(1,7)
		elif lvl == 2:
			n1 = randint(7,12)
			n2 = randint(7,12)
		else:
			n1 = randint(12,20)
			n2 = randint(12,20)
		result = n1*n2
	else:
		signe = '/'
		n = []
		n1 = 1
		n2 = 1		
		test = []
		fr = 0
		if lvl == 1:		
			for i in range(0,2):
				r = randint(2,11)
				n.append(r)
				n1 = n1*r	
			for i in range(0,1):
				while fr in test:
					fr = randint(0,2)
				test.append(fr)
				if fr == 0:
					n2 = n2*n[0]
				else:
					n2 = n2*n[1]
		elif lvl == 2:
			for i in range(0,3):
				r = randint(2,11)
				n.append(r)
				n1 = n1*r	
			for i in range(0,randint(1,2)):
				while fr in test:
					fr = randint(0,3)
				test.append(fr)
				if fr == 0:
					n2 = n2*n[0]
				elif fr == 1:
					n2 = n2*n[1]
				else:
					n2 = n2*n[2]
		else:
			for i in range(0,3):
				r = randint(5,15)
				n.append(r)
				n1 = n1*r	
			for i in range(0,randint(1,2)):
				while fr in test:
					fr = randint(0,3)
				test.append(fr)
				if fr == 0:
					n2 = n2*n[0]
				elif fr == 1:
					n2 = n2*n[1]
				else:
					n2 = n2*n[2]
		result = n1/n2
	return n1,signe,n2,result

def verification(rep,correction):
	try:
		rep = int(rep)
	except ValueError:
		victory = False
	except EOFError:
		victory = False
	else:
		if rep == correction:
			victory = True
		else:
			victory = False
	return victory