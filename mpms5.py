# flag = 0
#
# for day1 in range(1, 100000):
# 	for day2 in range(day1, 100000):
# 		a, b = day1, day2
# 		balance = a + b
# 		while balance < 1000000:
# 			if balance == 1000000:
# 				flag = 1
# 			temp = balance
# 			balance = balance + b
# 			b = temp
# 		if flag == 1:
# 			break
# 	print(day1, day2, balance)
# 	if flag == 1:
# 		break


#
def fib(a, b, count):
	# if b == 1000000:
	# 	return False
	# sum = a + b
	# print(count, sum)
	# count += 1
	# fib(b, sum, count)
	# return False
	sum = a + b
	while count < 100:
		print(count, sum)

		temp = b
		b = sum
		sum = sum + temp
		count += 1

fib(10000, 10001, 2)
#
# 51+2621
# 2672+2621
# 5293+2672
