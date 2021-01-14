temp = int(input('Temp? '))
unit = input("'C' or 'F'? ")

if(unit.upper() == 'C'):
	converted = temp * 9 / 5 + 32
elif(unit.upper() == 'F'):
	converted = (temp - 32) * 5 / 9
else:
	print("Incorrect input")
print(f'Converted temp is {converted} degrees')
