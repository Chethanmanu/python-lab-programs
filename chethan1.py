
l={1,2,3,4}
try:
	print(l)
	s=len(l)
	if s>5:
		raise TypeError
	print(d[2])

except TypeError:
	print("Error!!!length should be less than or equals to 5")
except NameError:
	print("index out of range")
else:
	for i in l:
		print(i)
finally:
	print("execution done!!!!!!")