

def add_num(a, b):
	return a+b

def mul_num(a, b):
	return a*b

def div_num(a, b):
	return a/b

def sub_num(a, b):
	return a-b

chk='c'
result = 0
a = int(input("Enter first number: "))

while(chk=='c'):
	op = input("Enter operation: ")
	b = int(input("Enter second number: "))

	if(op == '+'):
		result = add_num(a,b)
		print(result)
	elif(op == '-'):
		result = sub_num(a,b)
		print(result)
	elif(op == '/'):
		try:
			result = div_num(a,b)
			print(result)
		except ZeroDivisionError:
			print("Can not divide by 0")
	elif(op == '*'):
		result = mul_num(a,b)
		print(result)
	else:
		print("Invalid operation")

	a = result
