def hello(data):
	for x in range(len(data)):
		return data[x]

g = hello('hello')
print (g)
for i in g:
	print (i)#最后结果只返回一个h,因为return只会返回的是值，不能被迭代

def hello_b(data):
	for x in range(len(data)):
		yield data[x]

g = hello_b('hello')
print (g)
for i in g:
	print (i)#最后结果返回的是一个迭代器，可以被迭代