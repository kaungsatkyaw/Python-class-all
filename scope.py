# def scope_test():
# 	def do_local():
# 		spam = "local spam"

# 	def do_nonlocal():
# 		nonlocal spam
# 		spam = "nonlocal spam"

# 	def do_global():
# 		global spam
# 		spam = "global spam"

# 	spam = "test spam"
# 	do_local()
# 	print("After local assignment:", spam)
# 	do_nonlocal()
# 	print("After nonlocal assignment:",spam)
# 	do_global()
# 	print("After global assignment:",spam)
# _____________________________________
# scope_test()
# print("In global scope:",spam)
# a = input('please enter A value: ')
# b = input('Please enter B value: ')
# def print_max(a,b):
# 	if a > b:
# 		print(a , 'is maxium')
# 	elif a == b :
# 		print(a,'is equal to'. b)
# 	else:
# 		print(b, 'is maxium') 

# print_max(a, b)
# print(20 > 10)
# print(20 == 10)
# print(20 < 10)
# print(bool("Hello World"))
# print(bool(20))
# _____________________________________
#local variables
# def func(x):
# 	print('x is',x)
# 	x = 2
# 	print('Changed local x to', x)

# x = 10
# func(x)
# print('x is still', x)
# _____________________________________
# def func(y):
# 	print('y is', y)
# 	y=50
# 	print('changed local y to',y)

# def funx(y):
# 	print('y is', y)
# 	y = x + y
# 	print('Y is changed x + y', y)

# x=40
# y=20
# func(y)
# funx(y)
# print('y is still',y)
# _____________________________________

#global Statement

# def func():
# 	global x

# 	print('x is',x)
# 	x=2
# 	print('changed global x to', x)

# x = 50
# func()
# print('value of x is:', x)
#_________________________
# def func():
# 	global y

# 	print('y is',y)
# 	y=2
# 	print('changed global y to', y)

# y = 50
# func()
# print('value of x is:', y)
#__________________________

# def do_global():
# 	global spam
# 	spam = "global spam"

# spam = "test spam"
# do_global()
# print("After global assignment: ", spam)

x=10
def func():
	nonlocal x
	print('x is', x)

	x=5
	print("Value of x is:" , x)

x=10
func()
print("Real Value of x is:" , x)